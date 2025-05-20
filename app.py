from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

def home():
    return render_template('index.html')

def query_db(sql,args=(), one=False):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(sql, args)
    rv = cur.fetchall()
    con.commit()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    # Connect to the database
    results = query_db("SELECT * FROM bikes")
    return render_template('index.html', results=results)

@app.route('/form')
def add_form():
    return render_template('form.html')

@app.route('/delete')
def delete_form():
    return render_template('delete.html')

@app.post('/add_stuff')
def add_bike():
    model = request.form['model']
    if not model:
        return "Model cannot be empty", 400  # Return an error if the field is empty
    sql = "INSERT INTO bikes (model) VALUES (?)"
    query_db(sql, [model])
    BikeID = request.form['BikeID']
    if not BikeID:
        return "BikeID cannot be empty", 400  # Return an error if the field is empty
    sql = "INSERT INTO bikes (BikeID) VALUES (?)"
    query_db(sql, [BikeID])
    MakerID = request.form['MakerID']
    if not MakerID:
        return "MakerID cannot be empty", 400  # Return an error if the field is empty
    sql = "INSERT INTO bikes (MakerID) VALUES (?)"
    query_db(sql, [MakerID])
    Topspeed = request.form['Topspeed']
    if not Topspeed:
        return "Topspeed cannot be empty", 400  # Return an error if the field is empty
    sql = "INSERT INTO bikes (Topspeed) VALUES (?)"
    query_db(sql, [Topspeed])
    Cost = request.form['Cost']
    if not Cost:
        return "Cost cannot be empty", 400  # Return an error if the field is empty
    sql = "INSERT INTO bikes (Cost) VALUES (?)"
    query_db(sql, [Cost])
    Description = request.form['Description']
    if not Description:
        return "Description cannot be empty", 400  # Return an error if the field is empty
    sql = "INSERT INTO bikes (Description) VALUES (?)"
    query_db(sql, [Description])
    return redirect('/')

@app.post('/delete')
def delete_bike():
    model = request.form['model']
    if not model:
        return "Model cannot be empty", 400  # Return an error if the field is empty
    sql = "DELETE FROM bikes WHERE model = ?"
    query_db(sql, [model])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)