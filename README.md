# Flask_telegram

Pjocets has been created for demonstrate how i can working with Flask and Postgresql

## How to install

1. Python3 should be already installed. Then use ```pip``` (or ```pip3```, if there is a conflict with Python2) to install dependencies:

```$ pip install -r requirements.txt```

2. Environments keys should be in ```.env``` file, he should contains one variable

```telegram_bot_token=your_bot_token_from_telegram```

3. Now we need to install Postgresql :

```sudo apt-get install postgresql postgresql-contrib```

4. Logging into PSQL mode

```sudo -i -u postgres```

5. Create your user in postgresql 

```sudo -u postgres createuser --interactive```

```Enter name of role to add: your_name```

```Shall the new role be a superuser? (y/n) y```

6. Create your database

```createdb your_database_name```

7. Setting your database user password

```sudo -u user_name psql db_name```

```ALTER USER 'your_database_username' WITH PASSWORD 'your_database_password';```


8. Edit ```config.py``` 

```
POSTGRES = {
    'user' : 'your_database_username',
    'pw' : 'your_database_password',
    'db' : 'your_database',
    'host' : 'localhost',
    'port' : '5432'
}
```

9. Activate a virtual environment

```cd flask_telegram```

```source venv/bin/activate```

10. Now we should make a migration

```python manage.py db init```

```python manage.py db migrate```

```python manage.py db upgrade```

11. Install the npm

```sudo apt install npm```

12. Change directory to 

```cd \web```

13. Start the angular server

```npm start```

14. Thats all, in the next steps you'll send a message to telegram bot [Telegram_flask_bot](http://t.me/flask_telegram_bot) and after see him text in the main page of project (index.html), you can reply on a user message from web interface, use button 'reply'

