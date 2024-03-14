from fastapi import FastAPI
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import sys


sys.path.append("../")
from config import api_port

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=api_port,
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

@app.get("/evaluate_clustering/")
async def evaluate_clustering():
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
            "KMeans MSE": kmeans_mse
        }
    except Exception as e:
        return {"error": str(e)}
