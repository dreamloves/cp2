import os

API_ID = API_ID = 28590119

API_HASH = os.environ.get("API_HASH", "2494557bf21e6c5152f26070aa1a97c7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6338695339:AAGOrn_9WovtN0NWV1vZVIMwKiFYgFx_XV4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6462391456))

LOG = -1002140062103

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6462391456").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


