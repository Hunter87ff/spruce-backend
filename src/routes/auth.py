from flask import Blueprint, request, jsonify, make_response, redirect
import config, aiohttp, _http
auth = Blueprint("auth", __name__)
data = {}

@auth.route("/api/authorise", methods=["GET"])
async def token():
    """
    Asynchronous handler for Discord OAuth2 authorization.
    Exchanges the authorization code for tokens.
    """
    # Get configuration values
    client_id = config.CLIENT_ID
    client_secret = config.CSECRET
    redirect_uri = config.CALLBACK

    # Build token request payload
    token_request = {
        "grant_type": "authorization_code",
        "code": request.args.get("code", ""),
        "redirect_uri": request.args.get("url", redirect_uri),
        "client_id": client_id,
        "client_secret": client_secret,
    }

    try:
        # Make an asynchronous POST request to Discord's OAuth2 token endpoint
        async with aiohttp.ClientSession() as session:
            async with session.post(
                config.DISCORD_TOKEN_URL,
                data=token_request,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            ) as response:
                if response.status == 200:
                    _data:dict = await response.json()
                    result = {
                        "access_token": _data.get("access_token"),
                        "refresh_token": _data.get("refresh_token"),
                    }
                    return jsonify(result), 200

                # For non-OK responses, forward Discord's error message
                error_data = await response.json()
                return jsonify({"error": error_data}), response.status

    except aiohttp.ClientError as e:
        # Handle network-related errors
        return jsonify({"error": "Failed to connect to Discord API", "details": str(e)}), 500



@auth.route("/login", methods=["GET"])
async def login():
    return redirect(config.SITE_AUTH)


@auth.route("/api/oauth2", methods=["GET"])
async def oauth2():
    access_token = request.cookies.get("access_token") or request.args.get("code") or request.headers.get("Authorization")
    if data.get(access_token):
        return jsonify(data.get(access_token)), 288

    _authorised, code = await _http.fetch_api("/users/@me", access_token)
    _resp = make_response(jsonify(_authorised))
    if code==200:
        _resp.set_cookie("access_token", access_token)
        if len(data)>1000:data.clear()
        data[access_token] = _authorised

    return _resp, code if code>400 else 288



# @auth.route("/api/callback", methods=["GET"])
# async def callback():
#     return render("index.html")  # here we can add a fancy authenticating page???
#     #return data
