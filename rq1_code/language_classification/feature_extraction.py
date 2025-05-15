import os
import pandas as pd

native_dir = "../rectangle_data/native_fixations"
nonnative_dir = "../rectangle_data/nonnative_fixations"

def extract_fixation_features(file_path, label):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

    required_columns = {"duration", "x_cord", "y_cord"}
    if not required_columns.issubset(df.columns):
        print(f"Skipping {file_path}, missing required columns")
        return None

    df = df[df["duration"] > 0]

    if df.empty:
        print(f"Skipping {file_path}, no valid fixations")
        return None, None

    features = {
        "mean_duration": df["duration"].mean(),
        "std_duration": df["duration"].std(),
        "mean_x_cord": df["x_cord"].mean(),
        "std_x_cord": df["x_cord"].std(),
        "mean_y_cord": df["y_cord"].mean(),
        "std_y_cord": df["y_cord"].std(),
        "fixation_count": len(df),
        "label": label
    }

    return features, df["participant"][0]

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT_DIR, 'rectangle_data')

if not os.path.isdir(DATA_DIR):
    print("'rectangle_data/' folder is missing. Please download or place it in the project root.")
    exit(1)

participant_features = []

for folder, label in [(native_dir, "native"), (nonnative_dir, "nonnative")]:
    for file_name in os.listdir(folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder, file_name)
            feats, participant_id = extract_fixation_features(file_path, label)
            if feats:
                feats["participant_id"] = participant_id
                participant_features.append(feats)

features_df = pd.DataFrame(participant_features)

features_df.to_csv("fixation_features.csv", index=False)
print("Feature extraction complete. Saved to fixation_features.csv")

