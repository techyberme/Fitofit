class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER= 'root'
    MYSQL_PASSWORD= 'root'
    MYSQL_DB='db_fitofito'


config = { 
    'development': DevelopmentConfig
}