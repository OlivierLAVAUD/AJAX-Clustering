from fastapi import FastAPI, UploadFile, File
from sklearn.cluster import  KMeans
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

app = FastAPI()

@app.post("/evaluate_clustering/")
async def evaluate_clustering(file: UploadFile = File(...)):
    # Lire le fichier CSV téléchargé
    df = pd.read_csv(file.file)
    
    # Convertir la colonne Gender en 0 pour Female et 1 pour Male
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    
    # Préparer les données pour le clustering
    X = df.drop(columns=['CustomerID', 'Gender']).values
    
    # KMeans
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans_labels = kmeans.fit_predict(X)
    kmeans_mse = mean_squared_error(X, kmeans.cluster_centers_[kmeans_labels])
   
 
    return {
        "KMeans MSE": kmeans_mse
    }
