# 🛒 Product Recommendation System using Sentiment-Based Analysis

This project analyzes customer reviews to determine sentiment and identify best and worst-performing products based on a combined scoring metric. The goal is to help retailers like Target improve product recommendations and customer experience.

---

## 📌 Objective

- Analyze product reviews and ratings to estimate guest sentiment.
- Predict whether a guest recommends a product based on review/title sentiment.
- Score each product using a combined metric:
  - `doRecommend` (binary)
  - `Rating` (numerical)
  - Sentiment probability from review text
  - Sentiment probability from title
- Identify the **best** and **least** performing products.
- Display best/worst reviews and titles for insight into product reception.

---
### 📂 Project Structure
```
Product-Recommendation-System-using-Sentiment-Analysis/
├── data.xlsx              #Dataset
├── train.ipynb            #Jupyter notebook with full data analysis, modeling, and evaluation
├── app.py                 #Flask application to serve model results
├── rf_model_review.pkl    #Trained model
├── requirements.txt       #Python dependencies for running the notebook and app
├── LICENSE
└── README.md
```
---
## 🛠️ Installation

1. Clone this repository. 
```
   git clone https://github.com/tarakeshwari-sn/Product-Recommendation-System-using-Sentiment-Analysis
```
2. Install dependencies.
```
   pip install -r requirements.txt
```
3. Run the `train.ipynb` file to train the model.
```
   python train.ipynb
```
4. Then run the `app.py` to deploy the application on your local server.
```
  streamlit run app.py
```
---

   
