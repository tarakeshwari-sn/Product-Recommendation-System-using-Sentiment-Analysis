import streamlit as st
import pickle
import pandas as pd

# Load trained model and tfidf vectorizer
with open("rf_model_review.pkl", "rb") as f:
    model, tfidf = pickle.load(f)

# Get correct feature names
feature_names = tfidf.get_feature_names_out()
expected_columns = ['rating'] + list(feature_names)

st.title("🛍️ Product Review Sentiment Analyzer")

review = st.text_area("✍️ Enter a product review:")
rating = st.slider("⭐ Select product rating: (1 - would not buy again, 5 - loved it)", min_value=1, max_value=5, value=5)

if st.button("🔍 Analyze Review") and review.strip():
    # Use the loaded tfidf (DON'T FIT AGAIN)
    vec = tfidf.transform([review])
    vec_df = pd.DataFrame(vec.toarray(), columns=feature_names)
    vec_df.insert(0, 'rating', rating)

    # Fill any missing expected columns with 0
    for col in expected_columns:
        if col not in vec_df.columns:
            vec_df[col] = 0

    # Reorder
    vec_df = vec_df[expected_columns]

    try:
        prediction = model.predict(vec_df)[0]
        if prediction == 1:
            st.success("✅ Positive Sentiment: This product is recommended.")
        else:
            st.error("❌ Negative Sentiment: This product is not recommended.")
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")