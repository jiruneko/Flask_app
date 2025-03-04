from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    print("Rendering index.html")  # ここでログを確認
    return render_template(
        "index.html", title="ホームページ", content="これはサンプルページです"
    )


@app.route("/profile")
def profile():
    user = {"name": "Taro", "age": 30, "localhost": "Tokyo"}
    return render_template("profile.html", user=user)


@app.route("/post")
def posts():
    post = [
        {"title": "Flaskの使い方", "author": "Alice"},
        {"title": "jinja2の紹介", "author": "Bob"},
        {"title": "Flaskのルーティング", "author": "Charlie"},
    ]

    return render_template("posts.html", posts=posts)


@app.route("/dashboard")
def dashbord():
    user_logged_in = True
    return render_template("dashboard.html", logged_in=user_logged_in)


def format_datatime(value, format="%Y/%m/%d"):
    return value.strtime(format)


app.jinja_env_.filters["datetime"] = format_datatime


@app.route("/time")
def show_time():
    now = datetime.now()
    return render_template("time.html", current_time=now)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return ["Hello {name}!"]
    return render_template("submit.html")


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    return f"You searched for: {query}"


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
