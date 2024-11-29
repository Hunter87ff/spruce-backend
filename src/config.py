import os
from dotenv import load_dotenv
import requests
import aiohttp
import asyncio
from flask import Request, Response
load_dotenv()
env=os.environ



DOMAIN = "sprucbot.tech"
OWNER_ID = 885193210455011369
SECRET_KEY = env.get("SECRET_KEY") #app secret
MEDIAH = env.get("MEDIAH")
WEBH = env.get("WEBH") #backend webhook
CLIENT_ID = 931202912888164474 #client id
CSECRET = env.get("CSECRET") #client secret
TOKEN = env.get("TOKEN") #client token
CALLBACK = env.get("CALLBACK") #authentication callback endpoint
MSGH = env.get("MSGH")
PAYWBH = env.get("PAYWBH")
DONATE_LINK = f"https://{DOMAIN}/donate"
BASE_API = "https://discord.com/api/v10"
BASE_URL = CALLBACK.replace("/callback", "")
INVITE_URL = f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&permissions=8&scope=bot&guild_id="
CACHE_TIMEOUT = 360
ALLOWED_ORIGIN = env.get("ALLOWED_ORIGIN").split(",")
XCLIENT_ID = env.get("XCLIENT_ID")
XCLIENT_SECRET = env.get("XCLIENT_SECRET")
PAY_MAINTANANCE = "paymaintanance"
CLIENT_BASE = env.get("CLIENT_BASE", "http://localhost:3000")
SITE_AUTH = f"https://discord.com/oauth2/authorize?client_id=931202912888164474&response_type=code&redirect_uri={CLIENT_BASE}%2Fauth&scope=identify+guilds+email+connections"

# Discord API Endpoints
DISCORD_API_BASE_URL = "https://discord.com/api/v10"

DISCORD_AUTHORIZATION_BASE_URL = DISCORD_API_BASE_URL + "/oauth2/authorize"
DISCORD_TOKEN_URL = DISCORD_API_BASE_URL + "/oauth2/token"


DISCORD_OAUTH_ALL_SCOPES = [
    "bot", "connections", "email", "identify", "guilds", "guilds.join",
    "gdm.join", "messages.read", "rpc", "rpc.api", "rpc.notifications.read", "webhook.incoming",
]

DISCORD_OAUTH_DEFAULT_SCOPES = [
    "identify", "email", "guilds"
]


DISCORD_PASSTHROUGH_SCOPES = [
    "bot", "webhook.incoming",
]


DISCORD_IMAGE_BASE_URL = "https://cdn.discordapp.com/"
DISCORD_EMBED_BASE_BASE_URL = "https://cdn.discordapp.com/"
DISCORD_EMOJI_URL = "https://cdn.discordapp.com/emojis/"
DISCORD_IMAGE_FORMAT = "png"
DISCORD_ANIMATED_IMAGE_FORMAT = "gif"
DISCORD_USER_AVATAR_BASE_URL = DISCORD_IMAGE_BASE_URL + "avatars/{user_id}/{avatar_hash}.{format}"
DISCORD_DEFAULT_USER_AVATAR_BASE_URL = DISCORD_EMBED_BASE_BASE_URL + "embed/avatars/{modulo5}.png"
DISCORD_GUILD_ICON_BASE_URL = DISCORD_IMAGE_BASE_URL + "icons/{guild_id}/{icon_hash}.png"

DISCORD_USERS_CACHE_DEFAULT_MAX_LIMIT = 100







# def access(request:Request):
# 	print(str(request.headers.get("X-Forwarded-For")))
# 	if str(request.headers.get("X-Forwarded-For")) in ALLOWED_ORIGIN:
# 		return True
