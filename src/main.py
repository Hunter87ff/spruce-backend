from app import app
import os
from routes.auth import auth
from routes._guild import guild


app.register_blueprint(auth)
app.register_blueprint(guild) # subdomain="guild"

if os.getenv("dev"):
  app.run(port=3001, host="0.0.0.0", debug=True)
