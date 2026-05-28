import pandas as pd

# Load filtered dataset
df = pd.read_csv(
    "datasets/cleaned/it_filtered_dataset.csv"
)

# Convert title to lowercase
df['title'] = df['title'].astype(str).str.lower()

# Normalize roles
def normalize_role(title):

    # Frontend Developer
    if any(x in title for x in [
        'frontend',
        'front end',
        'react',
        'angular',
        'vue',
        'ui engineer'
    ]):
        return 'Frontend Developer'

    # Backend Developer
    elif any(x in title for x in [
        'backend',
        'back end',
        'java developer',
        'python developer',
        'node developer',
        'api developer'
    ]):
        return 'Backend Developer'

    # Full Stack Developer
    elif 'full stack' in title:
        return 'Full Stack Developer'

    # Data Analyst
    elif any(x in title for x in [
        'data analyst',
        'business analyst'
    ]):
        return 'Data Analyst'

    # Software Tester
    elif any(x in title for x in [
        'qa',
        'quality assurance',
        'software tester',
        'test engineer'
    ]):
        return 'Software Tester'

    # DevOps Engineer
    elif 'devops' in title:
        return 'DevOps Engineer'

    # Cloud Engineer
    elif 'cloud' in title:
        return 'Cloud Engineer'

    # Cybersecurity Analyst
    elif any(x in title for x in [
        'cybersecurity',
        'security analyst',
        'soc analyst'
    ]):
        return 'Cybersecurity Analyst'

    # Mobile Developer
    elif any(x in title for x in [
        'android',
        'ios',
        'mobile developer',
        'flutter',
        'react native'
    ]):
        return 'Mobile Developer'

    # UI/UX Designer
    elif any(x in title for x in [
        'ui designer',
        'ux designer',
        'ui/ux'
    ]):
        return 'UI/UX Designer'

    else:
        return None

# Apply normalization
df['role'] = df['title'].apply(normalize_role)

# Remove unmatched rows
df = df[df['role'].notnull()]

# Save normalized dataset
df.to_csv(
    "datasets/cleaned/normalized_roles_dataset.csv",
    index=False
)

# Show results
print("\nNormalization Completed!\n")

print(df['role'].value_counts())