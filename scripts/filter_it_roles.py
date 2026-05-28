import pandas as pd

# Load raw dataset
df = pd.read_csv("datasets/raw/linked-in/postings.csv")

# Convert title column to lowercase
df['title'] = df['title'].astype(str).str.lower()

# Allowed IT role keywords
it_keywords = [

    # Frontend
    'frontend',
    'front end',
    'react developer',
    'angular developer',
    'vue developer',
    'ui engineer',

    # Backend
    'backend',
    'back end',
    'node developer',
    'java developer',
    'python developer',
    'api developer',

    # Full stack
    'full stack',

    # Data
    'data analyst',

    # Testing
    'software tester',
    'qa engineer',
    'quality assurance',

    # DevOps
    'devops',

    # Cloud
    'cloud engineer',

    # Cybersecurity
    'cybersecurity',
    'security analyst',
    'soc analyst',

    # Mobile
    'android developer',
    'ios developer',
    'mobile developer',
    'flutter developer',
    'react native',

    # UI/UX
    'ui designer',
    'ux designer',
    'ui/ux'
]

# Filter only IT roles
filtered_df = df[
    df['title'].apply(
        lambda x: any(keyword in x for keyword in it_keywords)
    )
]

# Save filtered dataset
filtered_df.to_csv(
    "datasets/cleaned/it_filtered_dataset.csv",
    index=False
)

# Display info
print("\nFiltering Completed Successfully!\n")

print("Original Dataset Shape:")
print(df.shape)

print("\nFiltered Dataset Shape:")
print(filtered_df.shape)

print("\nSample Roles:")
print(filtered_df['title'].head(20))