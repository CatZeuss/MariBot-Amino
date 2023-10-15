from dotenv import load_dotenv
from os import getenv
from edamino import Bot


load_dotenv('.env')

EMAIL = getenv('oigresergio14@hotmail.com')
PASSWORD = getenv('30757223')

bot = Bot(email=EMAIL, password=PASSWORD, prefix="/")

