from ordinaland import *
from flask import Flask, request, render_template
app = Flask(__name__)
from random import choice

@app.route("/")
def index():
    article1 = (articles[len(articles)-1])
    article2 = (articles[len(articles)-2])
    article3 = (articles[len(articles)-3])
    liste_articles = [article1,article2,article3]

    return render_template("index.html",liste_articles=liste_articles)

@app.route("/construire-ordinateur")
def construire():
    return render_template("construire-ordinateur.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

