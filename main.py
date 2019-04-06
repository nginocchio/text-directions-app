from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from createmapquestapi import *
from mapquestclass import *

app = Flask(__name__)

# API_KEY =  	TGt6JoJOd4jhfxxR9fGGTNGsXgsPIuDu
# base_url = f'http://open.mapquestapi.com/directions/v2/route?key={API_KEY}&from='

# asdfafa.com/mcdonalds/subway

# @app.route('/<string: from>/<string: to>/')
# def hello_world(from, to):
    # directions = base_url + from + '&to='+ to
    # requests.get(directions)
    # return 

@app.route('/')
def hello():
    return 'Hi how are you?'

@app.route('/test')
def test():
    return 'test stuff'

@app.route('/sms', methods=['GET', 'POST'])
def sms():
    # number = request.form['From']
    message_body = request.form['Body']
    locations = message_body.split(',')
    # Body -> GatherRoutes
    #Gather
    location_tuples = create_tuples(locations)
    encoded_routes = url_encode(location_tuples)
    json_data = parse_the_response(http_response(encoded_routes))
    steps = Directions().look_up(json_data)
    
    turn_directions = ""
    for turns in steps:
        turn_directions += turns + '\n'

    #print(turn_directions)
    resp = MessagingResponse()
    resp.message(turn_directions)
    # resp.message("Hello, you said: {}".format(message_body))
    return str(resp)