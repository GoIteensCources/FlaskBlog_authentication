from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.models import Post
from flask_login import login_required


@app.route("/")
def index():
    stmt = db.select(Post).order_by(Post.title, Post.created)
    posts = db.session.execute(stmt).scalars()

    return render_template("index.html", posts=posts)


@app.route("/<int:post_id>/")
def post_detail(post_id):
    post = db.get_or_404(Post, post_id)
    print(post)
    return render_template("post.html",
                           post=post)


@app.route("/create/", methods=["POST", "GET"])
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        user = request.form["user"]

        if not title:
            flash("Поле title необхідне для заповнювання")
        else:
            post = Post(
                title=title,
                content=content,
                user=user
            )
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("index"))

    return render_template("create.html", )


@app.route("/<int:post_id>/edit/", methods=["POST", "GET"])
def edit(post_id):
    post = db.get_or_404(Post, post_id)
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        user = request.form["user"]
        if not title:
            flash("Поле title необхідне для заповнювання")
        else:
            post.title = title
            post.content = content
            post.user = user
            db.session.commit()
            return redirect(url_for("post_detail", post_id=post_id))

    return render_template("edit.html", post=post)


@app.route("/<int:post_id>/delete/")
def delete(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index"))


