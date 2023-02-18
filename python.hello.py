from flask import Flask  # running hello world using flask documentation

app = Flask(__name__)

@app.route("/")
def hello_world():
     return('Hello World')


if __name__ == "__main__":
    app.run()

