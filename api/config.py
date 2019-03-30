POSTGRES = {
    'user' : 'vadim',
    'pw' : '12325846',
    'db' : 'telegram_flask',
    'host' : 'localhost',
    'port' : '5432'
}
SQLALCHEMY_DATABASE_URI =  'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
SQLALCHEMY_TRACK_MODIFICATIONS = False