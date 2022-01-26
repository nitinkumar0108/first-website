from xml.dom.domreg import registered
from flask import Flask,render_template,request,url_for
import sqlite3 as sql
import os

database='protoset.db'
db='subtable.db'

def get_db(database):
    if not os.path.isfile(database):
        conn=sql.connect(database)
        query='''CREATE TABLE stuff (fname TEXT,lname TEXT,email TEXT,
                password REAL)'''
        conn.execute(query)
    conn=sql.connect(database)
    return conn





app=Flask(__name__)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['GET','POST'])
def registration():
        if request.method=='POST':
            first=request.form.get('fname')
            last=request.form.get('lname')
            email=request.form.get('email')
            password=request.form.get('password')
            conn=get_db(database)
        # Create cursor
            cursor=conn.cursor()
            query='''INSERT INTO stuff (fname,lname,email,
                    password) VALUES (?,?,?,?)'''
            data=[first,last,email,password]
            cursor.execute(query,data)
            conn.commit()
            conn.close()
            
            return render_template('login.html',data=data , info='Registered')
        return render_template('registration.html')

    

    

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':
        search_term=request.form['search']
        return render_template('search.html',search=search_term)
    return render_template('index.html')
    





@app.route('/subscribe', methods=['GET','POST'])
def subscribe():
        if request.method=='POST':
            
            email=request.form.get('email')
            
            conn=get_db(database)
        # Create cursor
            cursor=conn.cursor()
            query='''INSERT INTO stuff (email)'''
                   
            data=[email]
            cursor.execute(query,data)
            conn.commit()
            conn.close()
            
            return render_template('subscriber.html',data=data)
        return render_template('index.html')
  
@app.route('/about')
def about():
    return render_template('about.html')
    

if __name__=='__main__':
    app.run(debug=True,port=5800)


