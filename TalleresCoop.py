from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'TalleresCooperativos.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'TalleresCooperat'
app.config['MYSQL_PASSWORD'] = 'ndsfsn22299'
app.config['MYSQL_DB'] = 'TalleresCooperat$talleresCooperat'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM inventario')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', items = data)

@app.route('/add_item', methods=['POST'])
def add_item():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        valor = request.form['valor']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO inventario (codigo, nombre, cantidad, valor) VALUES (%s,%s,%s,%s)", (codigo, nombre, cantidad, valor))
        mysql.connection.commit()
        flash('item Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_item(id):
    codigo = id
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM inventario WHERE CODIGO = %s', (codigo))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-item.html', item = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_item(id):
    if request.method == 'POST':
        codigo = id
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        valor = request.form['valor']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE inventario
            SET nombre = %s,
                cantidad = %s,
                valor = %s
            WHERE codigo = %s
        """, (nombre, cantidad, valor, codigo))
        flash('item Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_item(id):
    codigo = id
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM inventario WHERE CODIGO = {0}'.format(codigo))
    mysql.connection.commit()
    flash('item Removed Successfully')
    return redirect(url_for('Index'))

#nueva modificacion

'''
# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)


js/jquery.min.js
js/bootstrap.min.js
js/scripts.js
'''
