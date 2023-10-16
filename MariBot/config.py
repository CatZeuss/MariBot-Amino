from dotenv import load_dotenv
from os import getenv
from edamino import Bot


load_dotenv('.env')

EMAIL = getenv('')
PASSWORD = getenv('')

bot = Bot(email=EMAIL, password=PASSWORD, prefix="/")

