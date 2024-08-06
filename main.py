from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

#Configuração do banco de dados
DATABASE_URL = os.getenv('DATABASE_URL')

#Conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
    return conn

@app.route('/data', methods = ['POST'])
def insert_data():
    if request.is_json:
        data = request.get_json()
        value = data.get('value')
        if not value:
            return jsonify({"Erro": "Nenhum valor passado."}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO (Tensão, corrente)  VALUES (%f)', value)
        conn.commit()
        cur.close()

        return jsonify({"Mensagem": "Dados inseridos com sucesso!"}), 200
    else:
        return jsonify({"Erro": "A requisição deve ser um json"}), 400
    
if __name__ == '__name__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
