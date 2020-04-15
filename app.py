from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("unfound.html")

if __name__ == '__main__':
    app.run(debug = True)
