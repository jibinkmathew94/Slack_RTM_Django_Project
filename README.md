# Project Title

JukeBox app built with Slack Rtm and Django Backend
## Getting Started



### Run in local machine

Clone this repo to your local machine

Create a app bot user in slack and get the bot_access_token from slack

Add the created App bot to any of the channel in your workspace

Create a virtual environment in your system

Install the requirements mentioned in the package using pip or any other package manager

Make migrations using the command 
```
"python manage.py makemigrations"

```
and then run 
```
"python manage.py migrate"

```
run 
```
python manage.py runrtmclient 
```
set the following environment variables with "bot access token" and channel name as shown below
```
export CHANNEL_NAME='channel_name';

export SLACK_BOT_TOKEN='xoxb-52188xxxxxxx-xxxxxxxxxxx-xxxxxxxxxxxxLjTFbS';

```
to start websocket client to receive messages from Slack RTM

run

```
python manage.py runrtmclient 

```

run 

```
python manage.py runserver
```

to start the server