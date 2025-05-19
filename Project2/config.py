import os
from urllib.parse import quote_plus

class Config:
    SECRET_KEY = 'dev-key-for-techtreasures'
    
    # For PostgreSQL - Update with your password
    password = quote_plus('Haider@57')
    SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:{password}@localhost:5432/techtreasures'
    
   
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False