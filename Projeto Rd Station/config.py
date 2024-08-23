import os

class Config:
    RD_STATION_API_KEY = os.getenv('RD_STATION_API_KEY', 'Chave rdstation')
    DB_SERVER = 'server'
    DB_DATABASE = 'database'
    DB_USERNAME = 'user'
    DB_PASSWORD = 'password'
