from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_data():
    return jsonify({"sucesso": "A requisição foi ok!"})
    
if __name__ == '__name__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
