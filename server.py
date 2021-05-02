from flask import Flask, jsonify
from flask_cors import CORS
from common import convert_stories


app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



@app.route('/stories')
def hello():
    return jsonify(convert_stories.stories())


if __name__ == "__main__":
    app.run(debug=True, port=8000)
