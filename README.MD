# Clustering Evaluation


##1. Installer les dépendances nécessaires

Assurez-vous d'avoir FastAPI, Uvicorn, et pandas installés dans votre environnement. Vous pouvez les installer en utilisant pip :

```
pip install fastapi uvicorn pandas
```

##2. Exécuter le Microservice

Pour exécuter le microservice, utilisez la commande suivante dans votre terminal dans le répertoire /backend:

```
uvicorn api:app --reload
```

##3. Importer le dataset Mall_Customers.csv de https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python
et le stocker dans un répertoire /data

##4. Tester l'API

Vous pouvez tester l'API en utilisant Swagger ou un outil comme Postman ou cURL pour envoyer une requête GET à http://127.0.0.1:8000/evaluate_clustering/

##5 Démarrer le serveur sur le port 8888

```
python -m http.server 8888
```

##6 Aller sur la page http://localhost:8888/frontend/