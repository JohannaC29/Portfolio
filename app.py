from flask import Flask, redirect, render_template, url_for, flash, request,logging, Response
import sqlite3 as sql 
from logindb import*
import time 
from flask_login import fresh_login_required,user_loaded_from_request
from flask_apscheduler import APScheduler
from flask_wtf import  FlaskForm,Form
from wtforms.validators import data_required
app = Flask(__name__) 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
def healthMotDB():

    conn = sql.connect('SQL database/login.db')
   
    conn.row_factory = sql.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/register', methods = ['GET','POST'])
def register(): 
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['Lname']
        email = request.form['email']
        password = request.form['password']
        conn =healthMotDB()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO login(fname,Lname,email,password)VALUES(?,?,?,?)',(fname,lname,email,password))
        conn.commit()
        conn.close()
        flash("You have sucessfully registered please return to homepage to login")
        time.sleep(3)
        return redirect(url_for('register'))
    return render_template('register.html', title='register')


@app.route('/login', methods = ['GET','POST'])
def login(): 
    if request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        conn =healthMotDB()
        cursor = conn.cursor()
        query1= "SELECT * FROM login WHERE email ='{email}'AND password='{password}'".format( email=email, password=password)
        row=cursor.execute(query1)
        row1= row.fetchall()
        conn.commit()
        conn.close()
        if len(row1)==1: 
          return redirect(url_for('main'))   
    return render_template('login.html', title='login')


@app.route('/main')
def main(): 
    return render_template('main.html')



@app.route('/mot', methods=['POST', 'GET'])
def mot():
    if request.method == 'POST':
        fullname= request.form['fullname']
        address = request.form['address']
        postcode= request.form['postcode']
        mobile= request.form['mobile']
        email= request.form['email']
        additional= request.form['additional']
        conn =healthMotDB()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO MOTBooking(fullname,address,postcode,mobile,email,additional)VALUES(?,?,?,?,?,?)',(fullname,address,postcode,mobile,email,additional))
        conn.commit()
        conn.close()
    return render_template('mot.html', title='mot')


    


@app.route('/gp', methods=['POST', 'GET'])
def gp():
    if request.method == 'POST':
        fullname= request.form['fullname']
        address = request.form['address']
        postcode= request.form['postcode']
        mobile= request.form['mobile']
        email= request.form['email']
        service= request.form['service']

        additional= request.form['additional']
        conn =healthMotDB()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO GpBooking(fullname,address,postcode,mobile,email,serviceOptions,additional)VALUES(?,?,?,?,?,?,?)',(fullname,address,postcode,mobile,email,service,additional))
        conn.commit()
        conn.close()
    return render_template('gp.html', title='gp')


@app.route('/surgery', methods=['POST', 'GET'])
def surgery():
    if request.method == 'POST':
        fullname= request.form['fullname']
        address = request.form['address']
        postcode= request.form['postcode']
        mobile= request.form['mobile']
        email= request.form['email']
        service= request.form['service']
        additional= request.form['additional']
        conn =healthMotDB()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO surgeryBooking(fullname,address,postcode,mobile,email,serviceOptions,additional)VALUES(?,?,?,?,?,?,?)',(fullname,address,postcode,mobile,email,service,additional))
        conn.commit()
        conn.close()
    return render_template("surgery.html")



if __name__ == '__main__':
    app.run(debug=True)

