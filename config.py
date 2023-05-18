from os import environ

API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

OWNER_USERNAME  = environ.get("OWNER_USERNAME","")  # WITHOUT @
UPDATES_CHANNEL = environ.get("UPDATES_CHANNEL","")  # WITHOUT @

OPENAI_API = environ.get("OPENAI_API","")
AI_LOGS = int(environ.get("AI_LOGS",""))
