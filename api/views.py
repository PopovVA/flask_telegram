from flask import render_template,jsonify,request,redirect, url_for, Response
from app import app
from models import Message
from models import User
from models import db
import requests
import os

@app.route('/')
def index(): 
    Messages = Message.query.all()
    return render_template('index.html', Messages=Messages)

@app.route('/reply/<int:message_id>', methods=['GET','POST'])
def reply(message_id): 
    if request.method == 'POST':
        text = request.form['name']
        message = Message.query.filter_by(id=message_id).first()
        telegram_id = message.user.telegram_id
        send_to_user(text,telegram_id)
        return redirect(url_for('index'))
    message = Message.query.filter_by(id=message_id).first()
    return render_template('reply.html', message=message)



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
      return  Response("List of required parameters : name,telegram_id,text", mimetype='text/html', status=400) 

    # Creating user

    NewUser = User(name, telegram_id)
    db.session.add(NewUser)
    db.session.commit()

    # Creating message

    MewMessage = Message(text, NewUser, NewUser.id)
    db.session.add(MewMessage)
    db.session.commit()

    return Response(status=200)

  return redirect(url_for('index'))
    
def send_to_user(text,telegram_id):
    token = os.getenv("telegram_bot_token")
    url_tmp = 'https://api.telegram.org/bot{}/{}?'
    url = url_tmp.format(token,'sendMessage')
    params = {"chat_id":telegram_id,"text":text}

    #any proxy
    https_proxy = "https://217.69.14.55:3128" 
    proxyDict = {  
              "https" : https_proxy
            }
            
    response = requests.post(url,params=params, proxies=proxyDict)    

