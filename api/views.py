from flask import render_template,jsonify,request,redirect, url_for, Response
from app import app
from models import Message
from models import User
from models import db
import json
import requests
import os

@app.route('/api/messages', methods=['GET'])
def get_messages():
    messages = getJsonMsgs(Message.query.all())
    return Response(messages, mimetype='json', status=200)

@app.route('/api/message/<int:message_id>', methods=['GET'])
def get_message(message_id): 
    message = getJsonMsg(Message.query.filter_by(id=message_id).first())
    return Response(message, mimetype='json', status=200)



@app.route('/msg_from_bot', methods=['POST'])
def msg_from_bot():

  if request.method == 'POST':

    # user
    name = request.form.get('name', type=str)
    telegram_id = request.form.get('telegram_id', type=str)
    # msg
    text = request.form.get('text', type=str)

    data = [
      name,
      telegram_id,
      text
    ]
    
    
    if any(value is None for value in data):
      return  Response("List of required parameters : name,telegram_id,text", mimetype='json', status=400) 

    # Creating user

    NewUser = User(name, telegram_id)
    db.session.add(NewUser)
    db.session.commit()

    # Creating message

    MewMessage = Message(text, NewUser, NewUser.id)
    db.session.add(MewMessage)
    db.session.commit()

    return Response(status=200)

@app.route('/api/send_to_user', methods=['POST'])  
def send_to_user():
    text = request.form.get('text', type=str)
    telegram_id = request.form.get('telegram_id', type=str)

    token = os.getenv("telegram_bot_token")
    url_tmp = 'https://api.telegram.org/bot{}/{}?'
    url = url_tmp.format(token,'sendMessage')
    params = {"chat_id":telegram_id,"text":text}

    #any proxy
    https_proxy = "https://45.250.178.36:8080" 
    proxyDict = {  
              "https" : https_proxy
            }
            
    response = requests.post(url,params=params, proxies=proxyDict) 
    return Response(text, mimetype='json', status=200)   

def getJsonMsgs(messages):
  msgs_list = []
  for message in messages:
    msg = {
      'id': message.id,
      'text': message.text,
      'telegram_id': message.user.telegram_id,
      'username': message.user.name
    }
    msgs_list.append(msg)
  return json.dumps(msgs_list)

def getJsonMsg(message):
  msg = {
    'id': message.id,
    'text': message.text,
    'telegram_id': message.user.telegram_id,
    'username': message.user.name
    }
  return json.dumps(msg)

