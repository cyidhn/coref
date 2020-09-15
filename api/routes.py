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
from french_crs.fast_text2corefchains import stanza_spacy_lang_model, mentions2chains
model = stanza_spacy_lang_model(
    spacy_stanza_lang_model="sequoia", framework="stanza")


@app.route("/importer-texte-idhn", methods=["POST"])
def importerTexteIdhn():
    if request.method == 'POST':

        # Retourner text
        texte = escape(request.form["texte"])

        # Lancement du model
        model.run_spacy_pipe_lines(texte)
        model.find_mentions_in_doc()

        # Save content
        chains_generator = mentions2chains(model.doc, model.doc_mentions_list)
        chains_generator.generate_mention_pairs(window_size=30)
        chains_generator.generate_json_mention_pairs()
        chains_generator.json_mention_pairs2dataframe(
            save_file=True, file_path="./static/coreference.xlsx")

        # Return
        return jsonify(
            link="/static/coreference.xlsx",
        )
        # return name_return, 201

    # return "Problem"
