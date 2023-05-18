from os import environ

API_ID = int(environ.get('API_ID', '19491592'))
API_HASH = environ.get('API_HASH', '01a4118f7aec3b2caece77a057fdd197')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

OWNER_USERNAME  = environ.get("OWNER_USERNAME","")  # WITHOUT @
UPDATES_CHANNEL = environ.get("UPDATES_CHANNEL","")  # WITHOUT @

OPENAI_API = environ.get("OPENAI_API","")
AI_LOGS = int(environ.get("AI_LOGS",""))
