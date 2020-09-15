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


@app.route("/importer-texte-idhn", methods=["POST"])
def importerTexteIdhn():
    print("Here")
    if request.method == 'POST':

        # Retourner text
        texte = escape(request.form["texte"])

        # Lancement du model
        analyse1(texte)

        # Return
        return jsonify(
            link="/static/coreference.xlsx",
        )
        # return name_return, 201

    # return "Problem"
