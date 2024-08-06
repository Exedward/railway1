from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods = ['GET'])
def insert_data():
    if request.is_json:
        data = request.get_json()
        value = data.get('value')
        return jsonify({"Mensagem": "Dados inseridos com sucesso!"}), 201
    else:
        return jsonify({"Erro": "A requisição deve ser um json"}), 400
    
if __name__ == '__name__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
