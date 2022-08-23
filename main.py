import math
import paginate
from ordinaland import *
from flask import Flask, request, render_template
app = Flask(__name__)
from random import choice
from math import ceil
@app.route("/")
def index():
    article1 = choice(articles)
    article2 = choice(articles)
    article3 = choice(articles)
    liste_articles = [article1,article2,article3]

    return render_template("index.html",liste_articles=liste_articles)

@app.route("/blog/<n>")
def blog(n):
    nbr_pages = math.ceil(len(articles) / 3)
    pages = paginate.Page(articles,n,3)
    long = len(pages)

    return render_template("blog.html",pages=pages,long=long,nbr_pages=nbr_pages)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

