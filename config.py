import os

API_ID = API_ID = 25218674

API_HASH = os.environ.get("API_HASH", "87c231f0e8704795b8239d06965b4351")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6953702071:AAHg25sMiG6Fm6_19VU5pVw0uz4-es-ptp0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6837703584))

LOG = -1002015336181

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6837703584").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


