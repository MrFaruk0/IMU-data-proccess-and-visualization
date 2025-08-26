import pandas as pd

def extract(df):

    features = []

    grouped = df.groupby(['subject', 'exercise', 'unit'])

    for (subject, exercise, unit), group in grouped:
        f = {
            "subject": subject,
            "exercise": exercise,
            "unit": unit,
        }

        f["acc_x_mean"] = group["acc_x"].mean()
        f["acc_y_mean"] = group["acc_y"].mean()
        f["acc_z_mean"] = group["acc_z"].mean()
        f["gyr_x_mean"] = group["gyr_x"].mean()
        f["gyr_y_mean"] = group["gyr_y"].mean()
        f["gyr_z_mean"] = group["gyr_z"].mean()

        f["acc_x_std"] = group["acc_x"].std()
        f["acc_y_std"] = group["acc_y"].std()
        f["acc_z_std"] = group["acc_z"].std()
        f["gyr_x_std"] = group["gyr_x"].std()
        f["gyr_y_std"] = group["gyr_y"].std()
        f["gyr_z_std"] = group["gyr_z"].std()

        features.append(f)

    return pd.DataFrame(features)