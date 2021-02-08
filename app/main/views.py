from flask import render_template
from . import main

#Routes
@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/blog')
def blog():
    #Fetch posts
    return render_template('blog.html', posts=posts)