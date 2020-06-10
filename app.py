from flask import Flask, render_template, request,redirect,url_for

from Common import defination
from Model import database

app = Flask(__name__)

@app.route("/Homepage")
def homepage():
    return render_template("Homepage.html")

#FormHandling
@app.route("/Search",methods = ["GET","POST"])
def homepage_handling():

    ob = defination.define()
    database.Database.initialize()

    if request.method == "POST":
        search_text = request.form["searchtext"]
        meaning = ob.get_word_defination(search_text)
        database.Database.insert('mycollection',{'word':search_text,'meaning':meaning})
        #print(search_text,meaning)
    return render_template("Homepage.html",st = search_text,data = meaning)

@app.route("/MyWord")
def mywords():
    if request.method == "GET":
        database.Database.initialize()
        doc = database.Database.find("mycollection")
    return render_template("MyWord.html",document = doc)


if __name__ == "__main__":
    app.run(debug = True,port  = 5026)