import os

from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from .createmapquestapi import *
from .mapquestclass import *

def help_message():
    help1 = "'set <home or work>;' will set your home address or work address."
    help2 =  " Enter addresses/stops seperated by an '@'. The second-Kth address can be 'home' or 'work' if already set."
    return help1 + help2

def parse_sms(mesg):
    resp = MessagingResponse()
    if mesg[0] == '-help':
        resp.message(help_message())
    elif mesg[0] == 'set':
        if mesg[1] == 'home':
            #put next value in the sms into the database for home
            a = ''
        elif mesg[1] == 'work':
            a = ''
            #put next value in the sms into database for work
    else:
        # Its a location text so generate turns and send the directions via sms
        location_tuples = create_tuples(mesg)
        encoded_routes = url_encode(location_tuples)
        json_data = parse_the_response(http_response(encoded_routes))
        steps = Directions().look_up(json_data)
    
        turn_directions = ""
        for turns in steps:
            turn_directions += turns + '\n'
        resp.message(turn_directions)
    return resp

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'phones.sqlite'),
    )

    from . import db
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/test')
    def test():
        return 'test stuff'

    @app.route('/sms', methods=['GET', 'POST'])
    def sms():
        # number = request.form['From']
        message_body = request.form['Body']
        locations = message_body.split(',')

        response = parse_sms(locations)

        # location_tuples = create_tuples(locations)
        # encoded_routes = url_encode(location_tuples)
        # json_data = parse_the_response(http_response(encoded_routes))
        # steps = Directions().look_up(json_data)
        
        # turn_directions = ""
        # for turns in steps:
        #     turn_directions += turns + '\n'

        # resp = MessagingResponse()
        # resp.message(turn_directions)
        # resp.message("Hello, you said: {}".format(message_body))
        # return str(resp)
        return str(response)


    return app