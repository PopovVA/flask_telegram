DEBUG = True
POSTGRES = {
    'user' : 'your_database_username',
    'pw' : 'your_database_password',
    'db' : 'your_database_name',
    'host' : 'localhost',
    'port' : '5432'
}
SQLALCHEMY_DATABASE_URI =  'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
SQLALCHEMY_TRACK_MODIFICATIONS = False
