<h1 align="center">Interface pour le résolution de coréférence en français</h1>
  
 
Interface Web pour l'algorithme de résolution de coréférence (https://github.com/mehdi-mirzapour/French-CRS) développé par Medhi Mirzapour (https://hal.archives-ouvertes.fr/hal-02906925). L'interface est développée et maintenue par l'équipe du laboratoire de l'IDHN.

### Download project 

```
git clone --recurse-submodules https://github.com/demangejeremy/coref.git
```

### Project setup

```
npm install
```

```
virtualenv -p python3 env
```

```
source env/bin/activate
```

```
cd ./api && pip install -r requirements.txt && cd ./French-CRS && pip install -e . && python -m spacy download fr_core_news_md && cd ../../
```


```
python ./api/app.py & npm run serve &

```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Lints and fixes files

```
npm run lint
```

## Citations

```bibtex
@inproceedings{desoyer2016coreference,
  title={Coreference Resolution for French Oral Data: Machine Learning Experiments with ANCOR},
  author={D{\'e}soyer, Ad{\`e}le and Landragin, Fr{\'e}d{\'e}ric and Tellier, Isabelle and Lefeuvre, Ana{\"\i}s and Antoine, Jean-Yves and Dinarelli, Marco},
  booktitle={International Conference on Intelligent Text Processing and Computational Linguistics},
  pages={507--519},
  year={2016},
  organization={Springer}
}
```

```bibtex
@inproceedings{muzerelle:hal-01075679,
  TITLE = {{ANCOR\_Centre, a Large Free Spoken French Coreference Corpus:  description of the Resource and Reliability Measures}},
  AUTHOR = {Muzerelle, Judith and Lefeuvre, Ana{\"i}s and Schang, Emmanuel and Antoine, Jean-Yves and Pelletier, Aurore and Maurel, Denis and Eshkol, Iris and Villaneau, Jeanne},
  BOOKTITLE = {{LREC'2014, 9th Language Resources and Evaluation Conference.}},
  PAGES = {843-847},
  YEAR = {2014}
}
```
