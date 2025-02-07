# -*- coding: utf-8 -*-
"""KMeansClustering_01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QvMkF8g5m9FgAyEzlI8_Vnsm4pEN0giy
"""

'''

import library

evaluate_model

evaluate_kmeans

getData

'''

import time
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.datasets import make_blobs

def evaluate_model(Y_actual, Y_pred):
    # Calculate metrics
    accuracy            = accuracy_score( Y_actual, Y_pred)
    precision           = precision_score(Y_actual, Y_pred, average='weighted')
    #recall_sensitivity  = recall_score(   Y_actual, Y_pred, average='weighted')
    f1_Score            = f1_score(       Y_actual, Y_pred, average='weighted')

    '''
    conf_matrix = confusion_matrix(Y_actual, Y_pred)
    tn, fp, fn, tp = conf_matrix.ravel()
    specificity = tn / (tn + fp)
    sensitivity = recall_sensitivity
    serendipity = (tp / (tp + fp)) * (tp / (tp + fn))
    '''
    return(accuracy)

# Function to evaluate K-Means clustering
def evaluate_kmeans(X, y_true, n_clusters):
    start_time = time.time()

    # Initialize KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)

    # Fit the model
    kmeans.fit(X)

    # Predict the clusters
    y_pred = kmeans.predict(X)

    # Calculate the time taken
    time_taken = time.time() - start_time

    # Calculate the sum of squared errors (SSE)
    sse = kmeans.inertia_

    return sse, time_taken, y_pred

# Function to calculate clustering accuracy
def getData(n_clusters, random_state):
  # Generate synthetic dataset
  n_samples = 1500
  n_features = 2

  return(make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=random_state))

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
def getDiseaseData():

  # Load the Breast Cancer dataset
  data = load_breast_cancer()
  X = data.data  # Features
  y_true = data.target  # True labels (0 = malignant, 1 = benign)

  # Standardize the features (important for K-Means)
  scaler = StandardScaler()
  X = scaler.fit_transform(X)
  return(X, y_true)

a, b = getDiseaseData()

n_clusters = 3
random_state = 42

# X, y_true = getData(n_clusters, random_state)

X, y_true = getDiseaseData()

# Evaluate K-Means for different dataset sizes
dataset_sizes = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
results = {}

for size in dataset_sizes:
    # Split the dataset
    X_subset, _, y_subset, _ = train_test_split(X, y_true, train_size=(0.7 * size), random_state=random_state)

    # Evaluate K-Means
    sse, time_taken, y_pred = evaluate_kmeans(X_subset, y_subset, n_clusters)

    accuracy = evaluate_model(y_subset, y_pred)

    results[size] = {
        'SSE': sse,
        'Time Taken': time_taken,
        'Accuracy': accuracy,
        'Predictions': y_pred
    }

# Print the results
for size, metrics in results.items():
    print(f"Dataset Size: {int(size * 100)}%")
    print(f"  Sum of Squared Errors (SSE): {metrics['SSE']}")
    print(f"  Time Taken: {metrics['Time Taken']:.4f} seconds")
    print(f"  Clustering Accuracy: {metrics['Accuracy']:.4f}")