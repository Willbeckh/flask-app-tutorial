from flask import render_template, redirect, flash
from app import app, db
from app.forms import PostForm
from app.models import Post

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Developer'}
    posts =[
        {
        'author': {'username': 'Guido'},
        'body': 'I designed python language'
        },
        {
         'author': {'username': 'Jack'},
        'body': 'Blue is a cool color'
        }
    ]
    return render_template('index.html', title='Homer', user=user, posts=posts)


# route to the post form
@app.route('/post', methods=['POST', 'GET'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        add = Post(username=form.username.data, post=form.post.data)
        db.session.add(add)
        db.session.commit() 
        flash(f"Hey, {form.username.data}! Your post '{form.post.data}'  was successfully submitted! ")
        return redirect('/index') 
    return render_template('new_post.html', title='Add post', form=form)


# viewing posts in db
@app.route('/view', methods=['GET'])
def view():
    posts = Post.query.all()
    return render_template('all_posts.html', title="Posts", posts=posts)