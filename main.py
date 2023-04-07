# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import PTN

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': PTN.parse("10.Days.with.Dad.2020.480p.Farsi.Subbed.HivaMovie.mkv")})


# driver function
if __name__ == '__main__':
    app.run(debug=True)
