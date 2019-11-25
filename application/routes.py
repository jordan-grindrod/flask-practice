from flask import render_template
from application import app, db
from application.models import Posts

@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.all() 
    return render_template('home.html', title='Home', posts=postData)
    
@app.route('/about')
def about():
    return render_template('about.html', title='About')
