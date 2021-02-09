from flask import render_template
from . import main

#Routes
@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/blog')
def blog():
    #Fetch posts then pass them to render_template
    return render_template('blog.html')