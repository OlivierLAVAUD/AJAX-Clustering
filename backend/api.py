from fastapi import FastAPI
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
import uvicorn

sys.path.append("../")
from config import API_BACK_DOMAIN, API_BACK_PORT, API_FRONT_DOMAIN, API_FRONT_PORT

print(" Starting Server Model on :", API_BACK_DOMAIN, ":", API_BACK_PORT)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=API_FRONT_PORT,
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

@app.get("/evaluate_clustering/kmeans/")
async def evaluate_kmeans_clustering():
    try:
        # Path to the CSV file in the data directory
        csv_file_path = "../data/Mall_Customers.csv"
        
        # Read the CSV file directly
        df = pd.read_csv(csv_file_path)
       
        # Convert the 'Gender' column to 0 for Female and 1 for Male
        df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    
        # Prepare the data for clustering
        X = df.drop(columns=['CustomerID', 'Gender']).values
    
        # KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans_labels = kmeans.fit_predict(X)
        kmeans_mse = mean_squared_error(X, kmeans.cluster_centers_[kmeans_labels])
       
        return {
            "kmeans": kmeans_mse
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/evaluate_clustering/agglomerative/")
async def evaluate_agglomerative_clustering():
    try:
        # Path to the CSV file in the data directory
        csv_file_path = "../data/Mall_Customers.csv"
        
        # Read the CSV file directly
        df = pd.read_csv(csv_file_path)
       
        # Convert the 'Gender' column to 0 for Female and 1 for Male
        df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    
        # Prepare the data for clustering
        X = df.drop(columns=['CustomerID', 'Gender']).values
    
        # Agglomerative clustering
        agglomerative = AgglomerativeClustering(n_clusters=3)
        agglomerative_labels = agglomerative.fit_predict(X)
        agglomerative_mse = mean_squared_error(X, agglomerative_labels)
       
        return {
            "agglomerative": agglomerative_mse
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host=API_BACK_DOMAIN, port=API_BACK_PORT)
