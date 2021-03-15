from flask import render_template
from . import main
import pymongo as pm
import os

client = pm.MongoClient(os.environ.get('MONGO_URI'))
db = client[os.environ.get('ENVIRONMENT')]['post']

#Home page
@main.route('/')
def index():
    #Get latest post
    post = db.find_one()
    return render_template('main/index.html', post=post)

#Book blog
@main.route('/blog')
def blog():
    #Get all posts
    posts = db.find()
    return render_template('main/blog.html', posts=posts)