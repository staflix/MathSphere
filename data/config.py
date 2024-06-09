import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('key')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_url = os.getenv('redirect_url')
auth_url = os.getenv('auth_url')
token_url = os.getenv('token_url')
userinfo_url = os.getenv('userinfo_url')
mail_password = os.getenv('mail_password')
