import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Set page configuration
st.set_page_config(page_title="Credit Card Clustering", layout="wide")

st.title("💳 Credit Card Customer Segmentation")
st.markdown("This app segments credit card users based on their balance, purchases, and credit limits.")

# Load data - ensure CC GENERAL.csv is in your HF Space repo
@st.cache_data
def load_data():
    df = pd.read_csv('CC GENERAL.csv')
    # Clean data based on your notebook logic
    df.dropna(inplace=True)
    return df

data = load_data()

# Sidebar for Cluster Configuration
st.sidebar.header("Model Parameters")
n_clusters = st.sidebar.slider("Select Number of Clusters (K)", 2, 10, 5)

# Feature Selection (Matching your notebook)
clustering_features = ["BALANCE", "PURCHASES", "CREDIT_LIMIT"]
X = data[clustering_features]

# Clustering Logic
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

# Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Cluster Distribution")
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x='BALANCE', y='PURCHASES', hue='Cluster', palette='viridis', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Data Summary")
    st.write(data.head())

st.subheader("Cluster Centroids (Mean Values)")
st.write(data.groupby('Cluster')[clustering_features].mean())