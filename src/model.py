import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def sensor_fusion(features_df):

    fused = []

    grouped = features_df.groupby(['subject', 'exercise'])

    for (subject, exercise), group in grouped:
        features = {"subject":subject, "exercise":exercise}

        for _, row in group.iterrows():
            unit = row["unit"]

            for col in group.columns:
                if col in ["subject", "exercise", "unit"]:
                    continue
                features[f"{unit}_{col}"] = row[col]

        fused.append(features)

    return pd.DataFrame(fused)

def train_model(fused):
    
    X = fused.drop(["subject", "exercise"] , axis=1)
    y = fused["exercise"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Değerlendirme")
    print(classification_report(y_test, y_pred))

    return model