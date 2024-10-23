from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    return f"<h1> HELLO {name} !</h1>"

@app.route("/blog/<int:blog_id>")
def blog(blog_id):
    return f"<h1> BLOG {blog_id} !</h1>"

@app.route("/admin")
def hello_admin():
    return f"<h1> HELLO ADMIN DZ!</h1>"

if __name__ == '__main__':
    app.run(debug=True)