from flask import Flask


app = Flask(__name__)

# Set to false in production
DEBUG = True


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Welcome !</h1>"




if __name__ == "__main__":

    app.run(debug=DEBUG)