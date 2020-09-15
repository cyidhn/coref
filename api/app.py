from routes import *
from flask import Flask
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.secret_key = 'changethisdata___'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app, support_credentials=True, resources={r"/*": {"origins": "*"}})


if __name__ == "__main__":
    app.run()
