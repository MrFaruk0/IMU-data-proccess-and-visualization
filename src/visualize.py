import matplotlib.pyplot as plt

def plot_exercise(df, exercise_label, subject=None, unit=None):
    subset = df[df['exercise'] == exercise_label]
    if subject:
        subset = subset[subset['subject'] == subject]
    if unit:
        subset = subset[subset['unit'] == unit]

    
    plt.figure(figsize=(10,5))
    plt.plot(subset['time'], subset['acc_x'], label='Acc X')
    plt.plot(subset['time'], subset['acc_y'], label='Acc Y')
    plt.plot(subset['time'], subset['acc_z'], label='Acc Z')
    plt.legend()
    plt.title(f'{exercise_label} ivme değerleri')
    if subject: title += f" - {subject}"
    if unit: title += f" - {unit}"
    plt.title(title)
    plt.xlabel('Zaman (s)')
    plt.ylabel('ivme (m/s²)')
    plt.show()