from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Flask server is online'

app.run()
