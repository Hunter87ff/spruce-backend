from flask import Blueprint, request
import src._http as client
from app import app
from flask_caching import Cache
from module._client import Client


guild = Blueprint("guild", __name__)
cache = Cache(config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 60})  # Config specific to blueprint
cache.init_app(app)




@guild.route("/api/guilds", methods=["GET"])
@cache.cached(timeout=60)
async def get_guilds():
    access_token = request.cookies.get("access_token") or request.args.get("key")
    _guilds = await Client().guilds(access_token)
    return _guilds or {"error": "No guilds found. with given access token."}
    # return await client.fetch_api("/users/@me/guilds", access_token)


@guild.route("/api/guilds/<guild_id>", methods=["GET"])
@cache.cached(timeout=60)
async def get_guild(guild_id:int):
    access_token = request.cookies.get("access_token") or request.args.get("key")
    return await client.bot_request(f"/guilds/{guild_id}")
