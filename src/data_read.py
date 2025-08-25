import os
import pandas as pd

def load_data(dir="../data/PTED"):
    dir = os.path.abspath(dir)
    data = []

    for subject in os.listdir(dir):
        subject_path = os.path.join(dir, subject)
        if not os.path.isdir(subject_path):
            continue

        for exercise in os.listdir(subject_path):
            exercise_path = os.path.join(subject_path, exercise)
            if not os.path.isdir(exercise_path):
                continue

            for unit in os.listdir(exercise_path):
                unit_path = os.path.join(exercise_path, unit)
                if not os.path.isdir(unit_path):
                    continue

                test_file = os.path.join(unit_path, "test.txt")
                if os.path.exists(test_file):
                    df = pd.read_csv(test_file, sep=";")
                    if "time index" in df.columns:
                        df["time"] = (df["time index"] - 1) * 0.04
                    elif "n" in df.columns:
                        df["time"] = (df["n"] - 1) * 0.04
                    else:
                        raise ValueError(f"Beklenen kolon bulunamadı: {df.columns}")

                    df["subject"] = subject
                    df["exercise"] = exercise
                    df["unit"] = unit
                    data.append(df)
    
    result = pd.concat(data, ignore_index=True)
    return result