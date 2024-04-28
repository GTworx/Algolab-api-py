import os
from dotenv import load_dotenv

load_dotenv()

MY_API_KEY = os.getenv('MY_API_KEY')
MY_USERNAME = os.getenv('MY_USERNAME')
MY_PASSWORD = os.getenv('MY_PASSWORD')

print(MY_API_KEY)
print(MY_USERNAME)
print(MY_PASSWORD)

print(os.environ.get('MY_API_KEY'))
print(os.environ.get('MY_USERNAME'))
print(os.environ.get('MY_PASSWORD'))
