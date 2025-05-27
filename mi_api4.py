from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'db.db'
DATABASE2 = 'db3.db3'
DATABASE2 = 'db1.db1'

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
    
@app.route('/articulos2', methods=['GET'])
def get_articulos2():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM articulos')
    articulos2 = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(articulos2)
    
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

@app.route('/Categorias', methods=['GET'])
def get_Categorias():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM Categorias')
    Categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(Categorias)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
