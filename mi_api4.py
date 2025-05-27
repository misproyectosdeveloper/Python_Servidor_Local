from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'db.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # para acceder a las columnas por nombre
    return conn

@app.route('/articulos', methods=['GET'])
def get_articulos():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM articulos')
    articulos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(articulos)

@app.route('/clientes', methods=['GET'])
def get_clientes():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM clientes')
    clientes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(clientes)

@app.route('/Ventas', methods=['GET'])
def get_Ventas():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM Ventas')
    Ventas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(Ventas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
