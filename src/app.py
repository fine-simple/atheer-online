import os
from flask import Flask, send_from_directory, request

app = Flask(__name__, static_url_path='', static_folder='./static', template_folder='./templates')
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/', methods=['GET'])
def home():
    return send_from_directory('templates', 'index.html')

from deps.Atheer.ATHEER_Arabic_Stemmer import AtheerStemmer
@app.route('/api', methods=['GET'])
def getStem():
    string = request.args.get('s')
    type = request.args.get('type')
    if type == 'stem' :
        return " ".join(AtheerStemmer.text2stem(string, False))
    elif type == 'plus':
        return " ".join(AtheerStemmer.text2stem(string, True))
    else:
        return " ".join(AtheerStemmer.text2root(string))

@app.route('/<path:path>', methods=['GET'])
def allOther(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True)