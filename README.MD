# Clustering Evaluation


##1. Installer les dépendances nécessaires

Assurez-vous d'avoir FastAPI, Uvicorn, et pandas installés dans votre environnement. Vous pouvez les installer en utilisant pip :

```pip install fastapi uvicorn pandas```

##3. Exécuter le Microservice

Pour exécuter le microservice, utilisez la commande suivante dans votre terminal :

``` uvicorn api:app --reload ```
##4. Tester l'API

Vous pouvez tester l'API en utilisant un outil comme Postman ou cURL pour envoyer une requête POST à http://127.0.0.1:8000/evaluate_clustering/ avec le fichier CSV Mall_Customers.csv comme pièce jointe.

https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python


##5 Lancer index.html de puis le répertoire front
```
python -m http.server 8888
```