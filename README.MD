# Clustering Evaluation

## Démarrage du backend

### via Docker :

Executer les commandes ci-dessous dans le répertoire backend/  
1. Construction de l'image  
```
docker build -t back-ajax .
```
2. Execution du container  
```
docker run -d -p 8000:8000 back-ajax
```

### méthode classique :

1. Installer les dépendances nécessaires : Assurez-vous d'avoir FastAPI, Uvicorn, et pandas installés dans votre environnement. Vous pouvez les installer en utilisant pip :  
```
pip install fastapi uvicorn pandas
```

2. Exécuter le Microservice  
Executez la commande suivante dans votre terminal dans le répertoire /backend:  
```
uvicorn api:app --reload
```

3. Importer le dataset Mall_Customers.csv de https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python  
et le stocker dans un répertoire /backend/data/  

4. Tester l'API  
Vous pouvez tester l'API en utilisant Swagger ou un outil comme Postman ou cURL pour envoyer une requête GET à http://127.0.0.1:8000/evaluate_clustering_kmeans/ 

## Démarrer d'un serveur front-end sur le port 8888

Exécutez la commande suivante dans le répertoire /frontend  
```
python -m http.server 8888
```

Rendez-vous sur la page http://localhost:8888/frontend/