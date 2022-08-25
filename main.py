import math
import paginate
from ordinaland import *
from flask import Flask, request, render_template
app = Flask(__name__)
from math import ceil




@app.route("/")
def index():
    article1 = (articles[len(articles) - 1])
    article2 = (articles[len(articles) - 2])
    article3 = (articles[len(articles) - 3])
    liste_articles = [article1,article2,article3]

    return render_template("index.html"
                           ,liste_articles=liste_articles)

@app.route("/blog/<n>")
def blog(n):
    nbr_pages = math.ceil(len(articles) / 3)
    pages = paginate.Page(articles, n, 3)
    long = len(pages)
    page_courante = int(n)

    return render_template("blog.html",
                           pages=pages,
                           long=long,
                           nbr_pages=nbr_pages,page_courante=page_courante)

@app.route("/article/<numero>")
def article(numero):
    numero = int(numero)
    bon_article = articles[numero]
    return render_template("article.html",
                           bon_article=bon_article)


@app.route("/construire-ordinateur")
def construire():
    return render_template("construire-ordinateur.html",
                           choix_composantes=choix_composantes)


@app.route("/afficher-ordinateur", methods=["POST"])
def afficherOrdinateur():
    reponses = []
    composantes = []
    for key in choix_composantes:
        try:
            reponses.append(request.form[key])
        except:
            pass
    for reponse in reponses:
        for key,values in choix_composantes.items():
            for composante in values:
                if reponse == composante.description:
                    composantes.append(Composante(composante.description,composante.prix,composante.lien))
    ordi = Ordinateur(composantes)

    code_postale = request.form["postal"]
    code_postale = code_postale.replace(" ", "")
    if len(code_postale) == 6 and code_postale[:6:2].isalpha() and code_postale[1:6:2].isnumeric():
        code_postale = True
    else:
        code_postale= False
    return render_template("afficher-ordinateur.html",
                           ordi=ordi,
                           code_postale=code_postale)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/glossaire")
def mot_cle():
    mot = []
    for definition in glossaire:
        mot.append(definition.terme)
    return render_template("glossaire.html",
                           mot=mot)

@app.route("/glossaire/<mot>")
def explication(mot):

    for definition in glossaire:
        if mot == definition.terme:
            terme = definition.terme
            texte = definition.texte
            source = definition.source
            mots_relies = definition.termes_relies()

    return render_template("definition.html",
                           terme=terme,
                           texte=texte,
                           source=source,
                           mots_relies=mots_relies,mot=mot)


if __name__ == "__main__":
    app.run(debug=True)

