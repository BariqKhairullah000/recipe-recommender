import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import glob
import streamlit as st

# Load all datasets
files = glob.glob("dataset-*.csv")  # Mengambil semua file CSV dengan pola nama tertentu
df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

# Preprocessing: Pastikan kolom Ingredients dalam format string
df["Ingredients"] = df["Ingredients"].astype(str).str.lower()

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
ingredients_matrix = vectorizer.fit_transform(df["Ingredients"])

def recommend_recipes(user_input, top_n=5):
    """
    Rekomendasi resep berdasarkan input bahan dari user.
    """
    user_input = " ".join(user_input).lower()  # Gabungkan daftar bahan menjadi string
    user_vec = vectorizer.transform([user_input])
    
    # Hitung cosine similarity
    similarities = cosine_similarity(user_vec, ingredients_matrix).flatten()
    
    # Ambil top-N resep dengan skor tertinggi
    top_indices = similarities.argsort()[-top_n:][::-1]
    recommendations = df.iloc[top_indices][["Title", "Ingredients", "Steps"]]
    
    return recommendations

def add_to_favorites(recipe):
    """Menambahkan resep ke daftar favorit."""
    if "favorite_recipes" not in st.session_state:
        st.session_state["favorite_recipes"] = []
    if recipe not in st.session_state["favorite_recipes"]:
        st.session_state["favorite_recipes"].append(recipe)

# Streamlit UI
st.title("Rekomendasi Resep Berdasarkan Bahan")
user_input = st.text_input("Masukkan bahan yang Anda miliki (pisahkan dengan koma)", "ayam, bawang, cabai")

if st.button("Cari Resep"):
    ingredients_list = [x.strip() for x in user_input.split(",")]
    recommended_recipes = recommend_recipes(ingredients_list)
    
    if recommended_recipes.empty:
        st.write("Tidak ada resep yang cocok dengan bahan tersebut.")
    else:
        for idx, row in recommended_recipes.iterrows():
            st.subheader(row["Title"])
            st.write(f"**Bahan:** {row['Ingredients']}")
            st.write(f"**Langkah:** {row['Steps']}")
            if st.button(f"❤️ Simpan {row['Title']}", key=f"save_{row['Title']}"):
                add_to_favorites(row.to_dict())
                st.success(f"{row['Title']} ditambahkan ke favorit!")

# Tampilkan Resep Favorit
st.sidebar.title("Resep Favorit")
if "favorite_recipes" in st.session_state and st.session_state["favorite_recipes"]:
    for fav in st.session_state["favorite_recipes"]:
        st.sidebar.subheader(fav["Title"])
        st.sidebar.write(f"**Bahan:** {fav['Ingredients']}")
        st.sidebar.write(f"**Langkah:** {fav['Steps']}")
else:
    st.sidebar.write("Belum ada resep favorit.")
