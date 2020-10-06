#
# TextPrint
# Laboratoire IDHN
#

#
# Importations
#
from flask import render_template
from flask import request, make_response, redirect, session, escape
from app import app
from flask import jsonify
import json
import os.path
import calendar
import time
import chardet
import io
import sys
from beta import analyse1
import excel2json
import json


@app.route("/importer-texte-idhn", methods=["POST"])
def importerTexteIdhn():
    print("Here")
    if request.method == 'POST':

        # Retourner text
        texte = escape(request.form["texte"])
        name = escape(request.form["name"])
        link = escape(request.form["link"])

        # Lancement du model
        analyse1(texte, link)
        excel2json.convert_from_file('./static/' + link + ".xlsx")

        # Debug
        with open('./static/Sheet1.json') as f:
            d = json.load(f)
            myData = d

        # Return
        return jsonify(
            link=link,
            name=name,
            data=myData
        )
        # return name_return, 201

    # return "Problem"


@app.route("/visu-texte-idhn", methods=["POST"])
def visuTexteIdhn():
    print("Here")
    if request.method == 'POST':

        # Retourner text
        # name = escape(request.form["name"])
        link = escape(request.form["link"])

        # Lancement du model
        excel2json.convert_from_file('./static/' + link + ".xlsx")

        # Debug
        with open('./static/Sheet1.json') as f:
            d = json.load(f)
            myData = d

        # Return
        return jsonify(
            data=myData
        )
        # return name_return, 201

    # return "Problem"
