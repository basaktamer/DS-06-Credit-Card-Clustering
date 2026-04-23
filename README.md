---
title: Credit Card Clustering
emoji: 💳
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: 1.31.0
app_file: app.py
pinned: false
---

# Credit Card Customer Segmentation

This application identifies latent structures within a population of credit card users using **K-Means Clustering**. 

## Project Overview
- **Aim:** Perform unsupervised behavioral stratification of ~8,600 users.
- **Features Used:** Balance, Purchases, and Credit Limit.
- **Methodology:** Data cleaning (removing 314 null records), feature selection, and WCSS-based clustering.

## How to use
Adjust the slider in the sidebar to change the number of clusters (K) and observe how the user segments evolve in the scatter plot.