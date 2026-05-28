import pandas as pd
from sklearn.utils import resample

# Load cleaned dataset
df = pd.read_csv(
    "datasets/cleaned/cleaned_dataset.csv"
)

print("Original Distribution:\n")
print(df['role'].value_counts())

# ---------------------------------------------------
# BALANCING SETTINGS
# ---------------------------------------------------

TARGET_MIN = 200
TARGET_MAX = 300

balanced_data = []

# ---------------------------------------------------
# BALANCE EACH ROLE
# ---------------------------------------------------

for role in df['role'].unique():

    role_df = df[df['role'] == role]

    current_count = len(role_df)

    # ------------------------------------------------
    # UNDERSAMPLE LARGE CLASSES
    # ------------------------------------------------

    if current_count > TARGET_MAX:

        role_df = role_df.sample(
            TARGET_MAX,
            random_state=42
        )

    # ------------------------------------------------
    # OVERSAMPLE SMALL CLASSES
    # ------------------------------------------------

    elif current_count < TARGET_MIN:

        role_df = resample(
            role_df,
            replace=True,
            n_samples=TARGET_MIN,
            random_state=42
        )

    balanced_data.append(role_df)

# ---------------------------------------------------
# COMBINE ALL
# ---------------------------------------------------

balanced_df = pd.concat(balanced_data)

# Shuffle dataset
balanced_df = balanced_df.sample(
    frac=1,
    random_state=42
)

# ---------------------------------------------------
# SAVE FINAL BALANCED DATASET
# ---------------------------------------------------

balanced_df.to_csv(
    "datasets/final/balanced_dataset.csv",
    index=False
)

# ---------------------------------------------------
# OUTPUT
# ---------------------------------------------------

print("\nBalanced Distribution:\n")
print(balanced_df['role'].value_counts())

print("\nFinal Shape:")
print(balanced_df.shape)