# text-directions-app

## Elevator Pitch
Need directions but don't have a fast internet speed? Send your location and the desired destination to (510) 999-8693 (Server must be up and running) seperated by an '&' then the directions will be sent back to you. (Table 6)

## What it does
Sends directions via sms when texting the number (510) 999-8693 with a message contaning <current location>&<destination> and directions to that location will be sent to your number.

## How we built it
Using Flask and Twilio we setup a server to relay our sms requests to the mapquest api to retrieve directions to the destination.

## Challenges we ran into
communicating with the mapquest api and the twilio api

## Accomplishments that we're proud of

## What we learned
how to work as a team to complete a software project

## What's next for Textable Directions
adding more functionality in the form of a user database to store common location such as home, work etc...

# Directions
cd into text-directions-app
run this command: `set FLASK_APP=directions` and `set FLASK_ENV=development`
then `flask run` to start development server
open ngrok and run `ngrok http 5000` then you will need to setup the ngrok url within your twilio settings then you can send texts to your twilio number
