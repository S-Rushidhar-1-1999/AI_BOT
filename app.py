from flask import Flask
app = Flask(__name__)

@app.route('/')
def AI_World():
    return '@USE_FULL_BOTZ'


if __name__ == "__main__":
    app.run()
