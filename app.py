import re

import random

from cs50 import SQL
from flask_session import Session
from flask import Flask, redirect, render_template, request

from helper import Trie, calculateboggle, populate, fill, definition, finddefinition

app = Flask(__name__)

db = SQL("sqlite:///database.db")





t = Trie()

populate(t)





@app.route("/", methods=["GET", "POST"])

def index():

    if request.method == "GET":

        return render_template("index.html")

    else:

        letterInput = ''

        for i in range(16):

            c = chr(random.randint(65, 90))

            letterInput = letterInput + c

        return redirect("/boggle/" + letterInput)





@app.route("/boggle/<letterInput>", methods=["GET"])

def boggle(letterInput):

    letterInput = str(letterInput).upper()

    if len(letterInput) != 16 or letterInput.isalpha() == False:

        return redirect("/")

    else:

        db.execute("INSERT INTO history (chain, dtime) VALUES (?, datetime('now'))", letterInput)

        dict = {}

        length = []

        boxbool = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

        boggleb = [['', '', '', ''],
                   ['', '', '', ''],
                   ['', '', '', ''],
                   ['', '', '', '']]

        for i in range(len(letterInput)):

            boggleb[i // 4][i % 4] = list(letterInput)[i]

        for i in range(4):

            for j in range(4):

                boxbool[i][j] = 1
                buffer = boggleb[i][j]

                calculateboggle(i, j, boggleb, boxbool, buffer, dict, t, length)

                fill(boxbool)

        return render_template("boggle.html", dict=dict, length=length)





@app.route("/dictionary", methods=["GET", "POST"])

def dictionary():

    if request.method == "GET":

        return render_template("dictionary.html")

    else:

        entry = request.form.get("entry")

        index = definition(t, entry)

        if index:

            text = finddefinition(index)

            text = re.search('(?<=[A-Z]{2}\s)(.+)', text)[0]

            text = text[0].upper() + text[1:]

            return render_template("dictionary.html", entry=entry, text=text)

        else:

            return apology("Not in dictionary", 404)





@app.route("/history", methods=["GET"])

def history():

    history = db.execute("SELECT oid AS oid, chain, dtime FROM history GROUP BY chain ORDER BY dtime DESC LIMIT 20")

    return render_template("history.html", history=history)





@app.route("/engine", methods=["GET"])

def engine():

    return render_template("engine.html")





@app.route("/bibliography", methods=["GET"])

def bibliography():

    return render_template("bibliography.html")





# Returning error message
def apology(message, code):

    return render_template("apology.html", top=code, bottom=message)