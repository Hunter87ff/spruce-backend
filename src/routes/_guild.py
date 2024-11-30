import json
from flask import Blueprint, request, make_response, jsonify
import _http as client
from app import app
from flask_caching import Cache
from module._client import Client


guild = Blueprint("guild", __name__)
cache = Cache(config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 60})  # Config specific to blueprint
cache.init_app(app)




@guild.route("/api/guilds", methods=["GET"])
async def get_guilds():
    access_token = request.cookies.get("access_token") or request.args.get("key") or request.headers.get("Authorization")
    if request.cookies.get("guilds"):
        return request.cookies.get("guilds")
    _guilds = await Client(access_token).guilds(json=True)
    _resp = make_response(jsonify(_guilds))
    return (_resp, 200)  or ({"error": "No guilds found. with given access token."}, 404)
    # return await client.fetch_api("/users/@me/guilds", access_token)


@guild.route("/api/guilds/<guild_id>", methods=["GET"])
async def get_guild(guild_id:int):
    access_token = request.cookies.get("access_token") or request.args.get("key")
    return await client.bot_request(f"/guilds/{guild_id}")
