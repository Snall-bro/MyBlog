import os

class Config:
    SECRET_KEY = os.environ.get('SECRET KEY') or 'you-will-never-guess'