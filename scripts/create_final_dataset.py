import pandas as pd
import re

# Load balanced dataset
df = pd.read_csv(
    "datasets/final/balanced_dataset.csv"
)

print("Original Shape:")
print(df.shape)

# ---------------------------------------------------
# CLEAN TEXT FUNCTION
# ---------------------------------------------------

def clean_text(text):

    # Convert to lowercase
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r'http\\S+', ' ', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z ]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\\s+', ' ', text)

    return text.strip()

# ---------------------------------------------------
# CREATE FINAL TEXT COLUMN
# ---------------------------------------------------

# Combine title + description + skills
df['combined_text'] = (
    df['title'].fillna('') + ' ' +
    df['description'].fillna('') + ' ' +
    df['skills_desc'].fillna('')
)

# Clean text
df['text'] = df['combined_text'].apply(clean_text)

# ---------------------------------------------------
# KEEP ONLY REQUIRED COLUMNS
# ---------------------------------------------------

final_df = df[['text', 'role']]

# Remove empty rows
final_df = final_df[
    final_df['text'].str.len() > 20
]

# ---------------------------------------------------
# SAVE FINAL ML DATASET
# ---------------------------------------------------

final_df.to_csv(
    "datasets/final/clean_it_roles_dataset.csv",
    index=False
)

# ---------------------------------------------------
# OUTPUT
# ---------------------------------------------------

print("\nFinal Dataset Created Successfully!\n")

print("Final Shape:")
print(final_df.shape)

print("\nSample Data:\n")
print(final_df.head())