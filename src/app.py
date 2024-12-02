import os
import sys
import config
import logging
import asyncio
import _http as client
from flask_cors import CORS
from flask_caching import Cache
from flask_compress import Compress
from flask import Flask, request, jsonify, send_from_directory


if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__, static_folder="../dist/assets", static_url_path="/assets")
#app.config["SERVER_NAME"] = "localhost:3001" 

# limiter = Limiter(
#     get_remote_address, # Use the client's IP address to identify them
#     app=app,
#     default_limits=["2000 per day", "500 per hour"] # Set default limits
# )
app.secret_key = config.SECRET_KEY
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.config['CACHE_TYPE'] = 'simple'  # Choose the cache type (e.g., 'simple', 'redis', etc.)
Compress(app)
cache = Cache(app)
CORS(app, 
     origins=config.ALLOWED_ORIGIN, 
     supports_credentials=True, 
     resources={"/*": {"origins": "*"}}
)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404


@app.route('/api/status', methods=['GET'])
@cache.cached(timeout=60)
async def health():
    return jsonify({"status": "alive"}), 200


@app.route("/api/channels/<id>", methods=["GET"])
@cache.cached(timeout=60)
async def get_channel(id:int):
    access_token = request.cookies.get("access_token")
    return await client.bot_request(f"/channels/{id}", access_token)


# # Serve static files from the dist folder
# @app.route('/dist/<path:path>')
# def send_dist(path):
#     return send_from_directory('../dist', path)

# Catch-all route for React Router
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('../dist', 'index.html')


#app.run(host="0.0.0.0", port=3001)
