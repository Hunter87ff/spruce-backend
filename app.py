import os
import sys
import config
import logging
import asyncio
import _http as client
from flask_cors import CORS
from flask_caching import Cache
from flask_compress import Compress
from flask import Flask, request, jsonify


if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask("main", static_folder="templates/static", template_folder="templates")
app.config["SERVER_NAME"] = "localhost:3001" 


app.secret_key = config.SECRET_KEY
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.config['CACHE_TYPE'] = 'simple'  # Choose the cache type (e.g., 'simple', 'redis', etc.)
Compress(app)
cache = Cache(app)
CORS(app, origins=config.ALLOWED_ORIGIN, supports_credentials=True, resources={"/*": {"origins": "*"}})


@app.route('/api/status', methods=['GET'])
async def health():
    return jsonify({"status": "alive"}), 200


@app.route("/api/channels/<id>", methods=["GET"])
@cache.cached(timeout=60)
async def get_channel(id:int):
    access_token = request.cookies.get("access_token")
    return await client.bot_request(f"/channels/{id}", access_token)

#app.run(host="0.0.0.0", port=3001)