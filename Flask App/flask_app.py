import flask
from flask import Flask, render_template, url_for, request, redirect
import random

app = Flask(__name__)

def roll(n, d, mod):
    a = 0
    for dice in range(int(n)):
        a+=random.randint(1, int(d))
    if(mod == ''):
        mod = 0
    return (a +int(mod))

@app.route("/")
def home():
    return render_template("sitehome_b.html", swordsnsorcerors = url_for("sns"))

@app.route("/appsns", methods=["POST", "GET"])
def sns():
    if request.method == "POST":
        form_number = request.form['n']
        form_dice = request.form['d']
        form_mod = request.form['mod']
        return render_template("sitesns.html", result = roll(form_number, form_dice, form_mod))
    else:
        return render_template("sitesns.html")

@app.route("/result")
def result_sns():
    try:
        return render_template("siteresult_sns.html", number=2, dice=2, app=url_for("sns"))
    except:
        return redirect(url_for("sns"))

@app.route("/<lost>/")
def lost(lost):
    return render_template("sitelost.html", weird=lost)

if __name__ == "__main__":
    app.run(debug = True)