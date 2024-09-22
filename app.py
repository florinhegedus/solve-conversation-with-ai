import os
from flask import Flask


app = Flask(__name__)

# Let the app know if it is inside a docker container
in_container = os.getenv('IN_CONTAINER', False)


@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(host="localhost", port=9999)