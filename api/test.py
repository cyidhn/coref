# Imports
from french_crs.fast_text2corefchains import stanza_spacy_lang_model, mentions2chains

# Choix de l'algo
model = stanza_spacy_lang_model(
    spacy_stanza_lang_model="sequoia", framework="stanza")

# Lancement du model
model.run_spacy_pipe_lines("""Ceci est un petit test. Voilà le test.""")
model.find_mentions_in_doc()


# Lancement de l'algo
model.find_mentions_in_doc()

chains_generator = mentions2chains(model.doc, model.doc_mentions_list)

chains_generator.generate_mention_pairs(window_size=30)

chains_generator.generate_json_mention_pairs()

chains_generator.json_mention_pairs2dataframe(
    save_file=True, file_path="./test.xlsx")

chains_generator.columns_drop_list = ["Left_ID", "Right_ID"]

chains_generator.apply_model_to_dataset()
