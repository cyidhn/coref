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
from reine import call_reine
import excel2json
import json
import pandas

@app.route("/importer-texte-idhn", methods=["POST"])
def importerTexteIdhn():
    if request.method == 'POST':

        # Retourner text
        texte = escape(request.form["texte"])
        name = escape(request.form["name"])
        link = escape(request.form["link"])

        # Lancement du model
        analyse1(texte, link)
        # excel2json.convert_from_file('./static/' + link + ".xlsx")

        # # Debug
        # with open('./static/Sheet1.json') as f:
        #     d = json.load(f)
        #     myData = d
        excel_data_df = pandas.read_excel('./static/' + link + ".xlsx", sheet_name='Sheet1')
        myData = excel_data_df.to_json(orient='records')
        myData = json.loads(myData)

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
    if request.method == 'POST':

        # Retourner text
        # name = escape(request.form["name"])
        link = escape(request.form["link"])

        # Lancement du model
        excel_data_df = pandas.read_excel('./static/' + link + ".xlsx", sheet_name='Sheet1')
        myData = excel_data_df.to_json(orient='records')
        myData = json.loads(myData)

        # Return
        return jsonify(
            data=myData
        )
        # return name_return, 201

    # return "Problem"


@app.route("/algo-reine", methods=["POST"])
def algoReine():
    if request.method == 'POST':

        # Retourner text
        # name = escape(request.form["name"])
        link = str(escape(request.form["link"]))
        texte = str(escape(request.form["texte"]))
        print(texte)

        # Lancement du model
        call_reine(DOCUMENT_TEXT=texte, DOCUMENT_LINK=link,
                   LEM=True, NB_ARBRES=3, NB_MOTS=10, NB_ITERATIONS=1000, NB_INIT=1)

        # Return
        return jsonify(
            data=link
        )
        # return name_return, 201

    # return "Problem"
