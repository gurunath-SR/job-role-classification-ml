import pandas as pd
from langdetect import detect

# Load normalized dataset
df = pd.read_csv(
    "datasets/cleaned/normalized_roles_dataset.csv"
)

print("Original Shape:")
print(df.shape)

# ---------------------------------------------------
# REMOVE DUPLICATES
# ---------------------------------------------------

df = df.drop_duplicates()

# ---------------------------------------------------
# REMOVE EMPTY DESCRIPTIONS
# ---------------------------------------------------

df = df.dropna(subset=['description'])

# ---------------------------------------------------
# REMOVE INTERNSHIPS
# ---------------------------------------------------

df = df[
    ~df['title'].str.contains(
        'intern',
        case=False,
        na=False
    )
]

# ---------------------------------------------------
# REMOVE VERY SHORT DESCRIPTIONS
# ---------------------------------------------------

df = df[
    df['description'].str.len() > 100
]

# ---------------------------------------------------
# KEEP ONLY ENGLISH DESCRIPTIONS
# ---------------------------------------------------

def is_english(text):
    try:
        return detect(str(text)) == 'en'
    except:
        return False

df = df[
    df['description'].apply(is_english)
]

# ---------------------------------------------------
# SAVE CLEANED DATASET
# ---------------------------------------------------

df.to_csv(
    "datasets/cleaned/cleaned_dataset.csv",
    index=False
)

# ---------------------------------------------------
# OUTPUT
# ---------------------------------------------------

print("\nCleaning Completed!\n")

print("Final Shape:")
print(df.shape)

print("\nRole Distribution:\n")
print(df['role'].value_counts())