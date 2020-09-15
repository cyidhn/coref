def analyse1(texte):
    # Imports
    from french_crs.fast_text2corefchains import stanza_spacy_lang_model, mentions2chains

    # Choix de l'algo
    model = stanza_spacy_lang_model(
        spacy_stanza_lang_model="sequoia", framework="stanza")

    # Lancement du model
    model.run_spacy_pipe_lines("""à mettre en oeuvre de le protectionnisme intelligent à mettre en avant de le patriotisme économique pour donner un avantage à les entreprises françaises dans la commande publique voilà tout cela. Le patriotisme économique qui n’a jamais été mis en oeuvre le protectionnisme intelligent la défiscalisation de les heures supplémentaires la suppression de le travail détaché la baisse de les charges mais exclusivement pour les TPE PME. Il met en place un patriotisme économique un protectionnisme intelligent il dit à les constructeurs américains si vous voulez aller faire vos voitures à l ’ étranger construire une voiture à l’ étranger alors vous paierez une taxe en les réimportant à les Etats-Unis . D ’ autant que évidemment ce que fait Trump m ’ intéresse et pour cause puisqu ’ il met en place la politique que j’ appelle de mes voeux depuis très longtemps et notamment la politique de patriotisme économique de protectionnisme intelligent""")
    model.find_mentions_in_doc()

    # Lancement de l'algo
    chains_generator = mentions2chains(model.doc, model.doc_mentions_list)
    chains_generator.generate_mention_pairs(window_size=30)
    chains_generator.generate_json_mention_pairs()
    chains_generator.json_mention_pairs2dataframe(
        save_file=True, file_path="./coreference.xlsx")
