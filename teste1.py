from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

#Configuração do banco de dados
url = os.getenv('DATABASE_URL')

#Conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(url, sslmode = 'require')
    return conn

@app.route('/data', methods = ['POST'])
def insert_data():
    if request.is_json:
        data = request.get_json()
        value1 = data.get('value1')
        value2 = data.get('value2')
        #if not value1:
        #    return jsonify({"Erro": "Nenhum valor passado."}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO (Tensão, corrente)  VALUES (%f, %f)', (value1, value2,))
        conn.commit()
        cur.close()

        return jsonify(data), 201
    else:
        return jsonify({"Erro": "A requisição deve ser um json"}), 400
    
if __name__ == '__name__':
    app.run(host = '0.0.0.0', port = 8080)
