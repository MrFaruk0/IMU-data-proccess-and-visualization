import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

def plot_acc_exercise(df, exercise_label, subject=None, unit=None):
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
    plt.title(f'{exercise_label} {unit} ivme değerleri')
    plt.xlabel('Zaman (s)')
    plt.ylabel('ivme (m/s²)')
    plt.show()

def plot_gyro_exercise(df, exercise_label, subject=None, unit=None):
    subset = df[df['exercise'] == exercise_label]
    if subject:
        subset = subset[subset['subject'] == subject]
    if unit:
        subset = subset[subset['unit'] == unit]

    b, a = signal.butter(4, 0.1, btype='low')
    filtered_gyro_x = signal.filtfilt(b, a, subset['gyr_x'])
    filtered_gyro_y = signal.filtfilt(b, a, subset['gyr_y'])
    filtered_gyro_z = signal.filtfilt(b, a, subset['gyr_z'])

    plt.figure(figsize=(10,5))
    plt.plot(subset['time'], filtered_gyro_x, label='Gyr X')
    plt.plot(subset['time'], filtered_gyro_y, label='Gyr Y')
    plt.plot(subset['time'], filtered_gyro_z, label='Gyr Z')
    plt.legend()
    plt.title(f'{exercise_label} {unit} jiroskop değerleri (filtrelenmiş)')
    plt.xlabel('Zaman (s)')
    plt.ylabel('Açı Hızı (°/s)')
    plt.show()

def plot_mag_exercise(df, exercise_label, subject=None, unit=None):
    subset = df[df['exercise'] == exercise_label]
    if subject:
        subset = subset[subset['subject'] == subject]
    if unit:
        subset = subset[subset['unit'] == unit]

    plt.figure(figsize=(10,5))
    plt.plot(subset['time'], subset['mag_x'], label='Mag X')
    plt.plot(subset['time'], subset['mag_y'], label='Mag Y')
    plt.plot(subset['time'], subset['mag_z'], label='Mag Z')
    plt.legend()
    plt.title(f'{exercise_label} {unit} manyetometre değerleri')
    plt.xlabel('Zaman (s)')
    plt.ylabel('Manyetik Alan (µT)')
    plt.show()