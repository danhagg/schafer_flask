from flask import (render_template, url_for, flash, redirect, request, abort,
                   Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    post = Post(title=form.title.data, author=current_user)
    db.session.add(post)
    db.session.commit
    if form.validate_on_submit():
        flash('Your post has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form)
