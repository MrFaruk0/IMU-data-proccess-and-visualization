def extract(df):

    features = df.groupby(['exercise']).apply(
        lambda x: pd.Series({

            'acc_x_mean': x['acc_x'].mean(),
            'acc_y_mean': x['acc_y'].mean(), 
            'acc_z_mean': x['acc_z'].mean(),
        
            'gyr_x_mean': x['gyr_x'].mean(),
            'gyr_y_mean': x['gyr_y'].mean(), 
            'gyr_z_mean': x['gyr_z'].mean(),
            
        })
    ).reset_index()
    return features