# Recipe Chatbot and Recommender

This project is a chatbot and recommender system for recipes, developed using Streamlit, pandas, and scikit-learn. It helps users search for recipes by name, get personalized recommendations based on available ingredients, and explore various recipe details.

---

## Features

### 1. **Search by Name**

Users can input the name of a recipe, and the bot will return a list of matching recipes along with their ingredients and steps.

### 2. **Recommendations by Ingredients**

Users can enter the ingredients they have, and the bot will recommend recipes based on similarity using TF-IDF and cosine similarity.

### 3. **Recipe Information**

Retrieve detailed information about a recipe, including:

- Name
- Ingredients
- Steps
- Estimated Cooking Time
- Difficulty Level
- Cuisine Type

---

## How to Run the Application

### 1. Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)

### 2. Install Dependencies

Run the following command to install all required libraries:

```bash
pip install -r requirements.txt
```

### 3. Download Dataset

Manually download the dataset from Kaggle:
[Kaggle Dataset](https://www.kaggle.com/datasets/canggih/indonesian-food-recipes?select=dataset-ayam.csv)

Place the dataset in the appropriate directory before running the application.

### 4. Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

### 5. Interact with the Chatbot

Once the app is running, open the provided local URL in your web browser (e.g., `http://localhost:8501`) to start interacting with the chatbot.

---

## Dataset

The chatbot uses a dataset with the following columns:

| Column Name    | Description                            |
| -------------- | -------------------------------------- |
| `title`        | Name of the recipe                     |
| `ingredients`  | List of ingredients used               |
| `steps`        | Step-by-step cooking instructions      |
| `cook_time`    | Estimated cooking time in minutes      |
| `difficulty`   | Difficulty level (Easy, Medium, Hard)  |
| `cuisine`      | Type of cuisine (e.g., Italian, Asian) |

---

## Application Interface

Below is a Canva design showing the application in action:

[View Application Interface on Canva](https://www.canva.com/design/DAGe5owjiVQ/xQLN8PO1wUdoMROBSGFgcg/view?utm_content=DAGe5owjiVQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h3b1bddaeba)

This interface allows users to:

- Search for recipes by name, ingredients, or cuisine type.
- View top-rated recipes with recommendations.

---

## Contact Information

For questions, issues, or contributions, please contact:

**Email:** ariq.syas30@gmail.com

