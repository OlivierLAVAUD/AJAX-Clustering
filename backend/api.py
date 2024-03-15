from fastapi import FastAPI
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import mean_squared_error, silhouette_score, davies_bouldin_score, calinski_harabasz_score
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import sys


sys.path.append("../")
from config import HTML_PORT

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=HTML_PORT,
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

def read_data():
    # Path to the CSV file in the data directory
    csv_file_path = "../data/Mall_Customers.csv"
    
    # Read the CSV file directly
    df = pd.read_csv(csv_file_path)

    # Convert the 'Gender' column to 0 for Female and 1 for Male
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})

    # Prepare the data for clustering
    X = df.drop(columns=['CustomerID', 'Gender']).values

    return X


@app.get("/evaluate_clustering/")
async def evaluate_clustering():
    try:
        X = read_data()

        # KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans_labels = kmeans.fit_predict(X)
        kmeans_mse = mean_squared_error(X, kmeans.cluster_centers_[kmeans_labels])
       
        return {
            "kmeans": kmeans_mse
        }
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/evaluate_clustering_agglomerative/")
async def evaluate_clustering():
    try:
        X = read_data()
    
        # Hierarchical clustering
        agglomerative = AgglomerativeClustering(n_clusters=3)
        agglomerative_labels = agglomerative.fit_predict(X)

        # Metrics
        silhouette = silhouette_score(X, agglomerative_labels)
        davies_bouldin = davies_bouldin_score(X, agglomerative_labels)
        calinski_harabasz = calinski_harabasz_score(X, agglomerative_labels)
       
        return {
            "silhouette_score": silhouette,
            "davies_bouldin_score": davies_bouldin,
            "calinski_harabasz_score": calinski_harabasz
        }
    
    except Exception as e:
        return {"error": str(e)}


@app.get("/evaluate_clustering_dbscan/")
async def evaluate_clustering():
    try:
        X = read_data()

        # DBSCAN clustering
        dbscan = DBSCAN(eps=3, min_samples=2)
        dbscan_labels = dbscan.fit_predict(X)
        # DBSCAN ne retourne pas de cluster centers, donc vous pouvez calculer la métrique de clustering autrement

        # Metrics
        silhouette = silhouette_score(X, dbscan_labels)
        davies_bouldin = davies_bouldin_score(X, dbscan_labels)
        calinski_harabasz = calinski_harabasz_score(X, dbscan_labels)
       
        return {
            "silhouette_score": silhouette,
            "davies_bouldin_score": davies_bouldin,
            "calinski_harabasz_score": calinski_harabasz
        }
    
    except Exception as e:
        return {"error": str(e)}