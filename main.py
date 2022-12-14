import math
import paginate
from ordinaland import *
from flask import Flask, request, render_template,redirect
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
                           nbr_pages=nbr_pages,page_courante=page_courante,)

@app.route("/article/<numero>")
def article(numero):
    numero = int(numero)
    bon_article = articles[numero]
    nb_max = len(articles)-1
    return render_template("article.html",
                           bon_article=bon_article,
                           nb_max=nb_max,
                           articles=articles)


@app.route("/construire-ordinateur")
def construire():
    return render_template("construire-ordinateur.html",
                           choix_composantes=choix_composantes)


@app.route("/afficher-ordinateur", methods=["POST"])
def afficherOrdinateur():
    reponses = []
    composantes = []
    livraison = round(12.99, 2)
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
    nb_composante = len(composantes)

    code_postal = request.form["postal"]
    code_postal = code_postal.replace(" ", "")
    if len(code_postal) == 6 and code_postal[:6:2].isalpha() and code_postal[1:6:2].isnumeric():
        code_postal = True
        prix_total = round(ordi.total()+livraison, 2)
    else:
        code_postal= False
        prix_total = ordi.total()
    return render_template("afficher-ordinateur.html",
                           ordi=ordi,
                           code_postale=code_postal,
                           prix_total=prix_total,
                           livraison=livraison,
                           nb_composante=nb_composante)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/glossaire")
def mot_cle():
    mot = []
    for definition in glossaire:
        mot.append(definition.terme)
    return render_template("glossaire.html",
                           mot=mot,)

@app.route("/glossaire/<mot>")
def explication(mot):
    for definition in glossaire:
        if mot == definition.terme:
            terme = definition.terme
            texte = definition.texte
            source = definition.source
            mots_relies = definition.termes_relies()
    if mot in mots_relies :
        mots_relies.remove(mot)
    nb_mot= len(mots_relies)

    return render_template("definition.html",
                           terme=terme,
                           texte=texte,
                           source=source,
                           mots_relies=mots_relies,
                           mot=mot,
                           nb_mot=nb_mot)
"""  a effacer


@app.route("/<mot>")
def redirect_view(mot):
    response = redirect('/')
    return response

@app.route("/contact/<mot>")
def redirect_view2(mot):
    response = redirect('/contact')
    return response

@app.route("/blog/<mot>")
def redirect_view3(mot):
    response = redirect("/blog")
    return response """


if __name__ == "__main__":
    app.run(debug=True)

