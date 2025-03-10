# -*- coding: utf-8 -*-
"""finaloutput.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15mFuxhnN7vIREJV6zhdAE94X-bZD8T9H

TO find how many gesture are there in data
"""

import scipy.io
import numpy as np

# Load the .mat file
mat_data = scipy.io.loadmat('/content/S1_E1_A1.mat')

# Extract relevant data
emg_data = mat_data['emg']  # EMG data
stimulus_data = mat_data['restimulus'].squeeze()  # Gesture labels

# Find unique gestures
unique_gestures = np.unique(stimulus_data)

# Create a dictionary to store segregated gestures
gesture_data = {}

# Segregate EMG data by gesture
for gesture in unique_gestures:
    if gesture != 0:  # Ignoring gesture '0', which usually indicates no gesture
        gesture_emg = emg_data[stimulus_data == gesture]
        gesture_data[gesture] = gesture_emg
        print(f"Gesture {gesture}: {gesture_emg.shape}")

# Now gesture_data contains EMG data separated by gesture

"""To find all gesture using 16 cannela"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the .mat file
mat_data = scipy.io.loadmat('/content/S1_E1_A1.mat')

# Extract relevant data
emg_data = mat_data['emg']  # EMG data
stimulus_data = mat_data['restimulus'].squeeze()  # Gesture labels

# Find unique gestures
unique_gestures = np.unique(stimulus_data)

# Loop through each gesture and plot all 16 channels
for gesture in unique_gestures:
    if gesture != 0:  # Skip gesture '0', which usually indicates no gesture
        gesture_emg = emg_data[stimulus_data == gesture]

        # Plot EMG data for all 16 channels
        time = np.arange(gesture_emg.shape[0])

        plt.figure(figsize=(16, 12))
        for channel in range(16):
            plt.subplot(4, 4, channel + 1)
            plt.plot(time, gesture_emg[:, channel])
            plt.title(f'Gesture {gesture} - Channel {channel + 1}')
            plt.xlabel('Time Samples')
            plt.ylabel('EMG Signal')

        plt.tight_layout()
        plt.show()

"""To find only one gesture using all channels"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the .mat file
mat_data = scipy.io.loadmat('/content/S1_E1_A1.mat')

# Extract relevant data
emg_data = mat_data['emg']  # EMG data
stimulus_data = mat_data['restimulus'].squeeze()  # Gesture labels

# Define the specific gesture to plot
specific_gesture = 12 # Change this to the gesture you want to visualize

# Extract EMG data for the specific gesture
gesture_emg = emg_data[stimulus_data == specific_gesture]

# Plot EMG data for all 16 channels of the specific gesture
time = np.arange(gesture_emg.shape[0])

plt.figure(figsize=(16, 12))
for channel in range(16):
    plt.subplot(4, 4, channel + 1)
    plt.plot(time, gesture_emg[:, channel])
    plt.title(f'Gesture {specific_gesture} - Channel {channel + 1}')
    plt.xlabel('Time Samples')
    plt.ylabel('EMG Signal')

plt.tight_layout()
plt.show()

"""to find one gestue using all channels"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the .mat file
mat_data = scipy.io.loadmat('/content/S1_E1_A1.mat')

# Extract relevant data
emg_data = mat_data['emg']  # EMG data
stimulus_data = mat_data['restimulus'].squeeze()  # Gesture labels

# Define the specific gesture to plot
specific_gesture = 8 # Change this to the gesture you want to visualize

# Extract EMG data for the specific gesture
gesture_emg = emg_data[stimulus_data == specific_gesture]

# Average across all channels for the specific gesture
average_emg = np.mean(gesture_emg, axis=1)

# Plot the averaged EMG data for the specific gesture
time = np.arange(average_emg.shape[0])

plt.figure(figsize=(12, 6))
plt.plot(time, average_emg, color='b')
plt.title(f'EMG Signal for Gesture {specific_gesture}')
plt.xlabel('Time Samples')
plt.ylabel('Average EMG Signal')
plt.grid()
plt.show()

import scipy.io
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the .mat file
data = scipy.io.loadmat('/content/S1_E1_A1.mat')
print(data.keys())  # Check the keys to understand the structure

sEMG_recording = data['emg']

# Plot the EMG recording
plt.figure(figsize=(14, 7), dpi=120, facecolor='w', edgecolor='k')
plt.plot(sEMG_recording)
plt.xlabel('time (msec)', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(['electrode_1', 'electrode_2', 'electrode_3', 'electrode_4',
            'electrode_5', 'electrode_6', 'electrode_7', 'electrode_8',
            'electrode_9', 'electrode_10', 'electrode_11', 'electrode_12',
            'electrode_13', 'electrode_14', 'electrode_15', 'electrode_16'])
plt.show()

# Ensure the shape is what we expect
print(sEMG_recording.shape)  # Check if it has shape (time_samples, n_electrodes)
print(data['emg'].shape)  # Check if it matches sEMG_recording in shape

# Process the signal for each electrode (if the shape matches)
n_electrodes = 16
for electrode in range(n_electrodes):
    # Multiply each electrode's signal by its corresponding value in 'data['emg']' and scale
    sEMG_recording[:, electrode] = (data['emg'][:, electrode] * sEMG_recording[:, electrode]) / 100

# Now, sEMG_recording should be updated with the scaled values

plt.figure(figsize=(14, 7), dpi=120, facecolor='w', edgecolor='k')
plt.plot(sEMG_recording)
plt.xlabel('time (msec)', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(['electrode_1', 'electrode_2', 'electrode_3', 'electrode_4',
            'electrode_5', 'electrode_6', 'electrode_7', 'electrode_8',
            'electrode_9', 'electrode_10', 'electrode_11', 'electrode_12',
            'electrode_13', 'electrode_14', 'electrode_15', 'electrode_16'])
plt.show()
t, duration = 10000, 15
img = sEMG_recording[t : t + duration, :]

plt.figure(figsize=(8, 15), dpi=80)
plt.imshow(np.swapaxes(img,0,1))
plt.show()

"""Specify the gesture ID to extract and visualize"""

import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Load the .mat file
data = scipy.io.loadmat('/content/S1_E1_A1.mat')
print(data.keys())  # Check the keys to understand the structure

sEMG_recording = data['emg']  # Extract EMG signals
stimulus_labels = data['stimulus']  # Extract gesture labels

def plot_emg_signals_for_gesture(sEMG_recording, stimulus_labels, gesture_id):
    # Identify indices for the specified gesture
    gesture_indices = np.where(stimulus_labels.flatten() == gesture_id)[0]

    if len(gesture_indices) > 0:
        # Extract sEMG signals for the gesture
        gesture_emg = sEMG_recording[gesture_indices, :]
        print(f"Extracted sEMG signals for Gesture {gesture_id} with shape: {gesture_emg.shape}")

        # Plot the sEMG signals for the gesture
        plt.figure(figsize=(14, 7), dpi=120, facecolor='w', edgecolor='k')
        plt.plot(gesture_emg)
        plt.xlabel('Time (samples)', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        plt.legend(['Electrode 1', 'Electrode 2', 'Electrode 3', 'Electrode 4',
                    'Electrode 5', 'Electrode 6', 'Electrode 7', 'Electrode 8',
                    'electrode_9', 'electrode_10', 'electrode_11', 'electrode_12',
            'electrode_13', 'electrode_14', 'electrode_15', 'electrode_16'])
        plt.title(f"sEMG Signals for Gesture {gesture_id}")
        plt.show()
    else:
        print(f"No data found for Gesture {gesture_id}.")

# Specify the gesture ID to extract and visualize
gesture_id =1
plot_emg_signals_for_gesture(sEMG_recording, stimulus_labels, gesture_id)























"""specefic gesture id

"""

import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Load the .mat file
data = scipy.io.loadmat('/content/S1_E1_A1.mat')
print(data.keys())  # Check the keys to understand the structure

# Extract relevant data
sEMG_recording = data['emg']  # Extract EMG signals
stimulus_labels = data['stimulus']  # Extract gesture labels
repetitions = data['repetition']  # Extract repetition information
restimulus_labels = data['restimulus']  # Extract detailed gesture labels

# Function to plot EMG signals for a specific gesture, repetition, and level
def plot_emg_signals_for_gesture(sEMG_recording, stimulus_labels, repetitions, restimulus_labels, gesture_id):
    # Identify indices for the specified gesture
    gesture_indices = np.where(stimulus_labels.flatten() == gesture_id)[0]

    if len(gesture_indices) > 0:
        # Extract sEMG signals, repetitions, and levels for the gesture
        gesture_emg = sEMG_recording[gesture_indices, :]
        gesture_repetitions = repetitions[gesture_indices]
        gesture_levels = restimulus_labels[gesture_indices]

        print(f"Extracted sEMG signals for Gesture {gesture_id} with shape: {gesture_emg.shape}")

        # Plot the sEMG signals for the gesture
        plt.figure(figsize=(14, 7), dpi=120, facecolor='w', edgecolor='k')
        plt.plot(gesture_emg)
        plt.xlabel('Time (samples)', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        plt.legend(['Electrode 1', 'Electrode 2', 'Electrode 3', 'Electrode 4',
                    'Electrode 5', 'Electrode 6', 'Electrode 7', 'Electrode 8',
                    'Electrode 9', 'Electrode 10', 'Electrode 11', 'Electrode 12',
                    'Electrode 13', 'Electrode 14', 'Electrode 15', 'Electrode 16'],
                   loc='upper right', fontsize=8)
        plt.title(f"sEMG Signals for Gesture {gesture_id}\nRepetitions: {np.unique(gesture_repetitions).tolist()}, Levels: {np.unique(gesture_levels).tolist()}", fontsize=15)
        plt.show()
    else:
        print(f"No data found for Gesture {gesture_id}.")

# Specify the gesture ID to extract and visualize
gesture_id = 10
plot_emg_signals_for_gesture(sEMG_recording, stimulus_labels, repetitions, restimulus_labels, gesture_id)

"""specefic gesture for in differnt repetation"""

import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Load the .mat file
data = scipy.io.loadmat('/content/S1_E1_A1.mat')
print(data.keys())  # Check the keys to understand the structure

# Extract relevant data
sEMG_recording = data['emg']  # Extract EMG signals
stimulus_labels = data['stimulus']  # Extract gesture labels
repetitions = data['repetition']  # Extract repetition information
restimulus_labels = data['restimulus']  # Extract detailed gesture labels

# Function to plot EMG signals for each repetition of a specific gesture
def plot_emg_signals_per_repetition(sEMG_recording, stimulus_labels, repetitions, restimulus_labels, gesture_id):
    # Identify indices for the specified gesture
    gesture_indices = np.where(stimulus_labels.flatten() == gesture_id)[0]

    if len(gesture_indices) > 0:
        # Extract sEMG signals, repetitions, and levels for the gesture
        gesture_emg = sEMG_recording[gesture_indices, :]
        gesture_repetitions = repetitions[gesture_indices]
        unique_repetitions = np.unique(gesture_repetitions)

        print(f"Extracted sEMG signals for Gesture {gesture_id} with shape: {gesture_emg.shape}")

        # Plot each repetition in a separate figure
        for rep in unique_repetitions:
            rep_indices = np.where(gesture_repetitions.flatten() == rep)[0]
            rep_emg = gesture_emg[rep_indices, :]

            plt.figure(figsize=(14, 7), dpi=120, facecolor='w', edgecolor='k')
            plt.plot(rep_emg)
            plt.xlabel('Time (samples)', fontsize=15)
            plt.ylabel('Amplitude', fontsize=15)
            plt.legend([f'Electrode {i+1}' for i in range(rep_emg.shape[1])], loc='upper right', fontsize=8)
            plt.title(f"sEMG Signals for Gesture {gesture_id} - Repetition {int(rep)}", fontsize=15)
            plt.show()

    else:
        print(f"No data found for Gesture {gesture_id}.")

# Specify the gesture ID to extract and visualize
gesture_id = 10
plot_emg_signals_per_repetition(sEMG_recording, stimulus_labels, repetitions, restimulus_labels, gesture_id)

import scipy.io
import numpy as np
import os

# Load the .mat file
data = scipy.io.loadmat('/content/S1_E2_A1.mat')

# Extract sEMG signals and labels
sEMG_recording = data['emg']  # Shape: (samples, electrodes)
stimulus_labels = data['stimulus'].flatten()  # Gesture labels
repetition_labels = data['repetition'].flatten()  # Repetition labels

# Get unique gestures and repetitions
unique_gestures = np.unique(stimulus_labels)
unique_repetitions = np.unique(repetition_labels)

# Dictionary to store separated data
separated_data = {}

# Loop through each gesture and repetition
for gesture in unique_gestures:
    if gesture == 0:
        continue  # Skip rest class

    for repetition in unique_repetitions:
        indices = np.where((stimulus_labels == gesture) & (repetition_labels == repetition))[0]
        if len(indices) > 0:
            separated_data[f'gesture_{gesture}_repetition_{repetition}'] = sEMG_recording[indices, :]

# Save the separated data to a single .mat file
output_file = '/content/separated_sEMG_data s1.mat'
scipy.io.savemat(output_file, separated_data)

print(f"Separated sEMG data saved successfully in {output_file}.")

"""saving the data to form gesture and train in CNN"""

import scipy.io
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the .mat file
data = scipy.io.loadmat('/content/S2_E1_A1.mat')

# Extract relevant data
sEMG_recording = data['emg']  # Extract EMG signals
stimulus_labels = data['stimulus']  # Extract gesture labels

# Get unique gestures from stimulus labels
unique_gestures = np.unique(stimulus_labels)

# Normalize EMG data (Min-Max Scaling)
sEMG_recording = (sEMG_recording - np.min(sEMG_recording)) / (np.max(sEMG_recording) - np.min(sEMG_recording))

# Convert stimulus labels to one-hot encoding for multi-class classification
labels = to_categorical(stimulus_labels.flatten() - 1, num_classes=len(unique_gestures))  # Subtract 1 if label starts from 1

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    sEMG_recording, labels, test_size=0.2, random_state=42, shuffle=True
)

# Reshape for CNN (samples, time_steps, channels)
X_train = np.expand_dims(X_train, axis=-1)  # (samples, time_steps, 1)
X_test = np.expand_dims(X_test, axis=-1)

# Define a multi-class CNN model
model = Sequential([
    Conv1D(filters=16, kernel_size=5, activation='relu', input_shape=(X_train.shape[1], 1)),
    MaxPooling1D(pool_size=2),
    Dropout(0.3),
    Conv1D(filters=32, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
    Dropout(0.3),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(len(unique_gestures), activation='softmax')  # Softmax for multi-class classification
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Get model predictions
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)  # Get class labels for predictions

# Convert y_test to class labels (from one-hot encoding)
y_test_classes = np.argmax(y_test, axis=1)

# Dictionary to store accuracy per gesture
gesture_accuracy = {}

# Calculate accuracy for each gesture class
for gesture in unique_gestures:
    # Get indices where the gesture appears in the test set
    indices = np.where(y_test_classes == (gesture - 1))[0]  # Adjust if labels start from 1

    # Calculate accuracy for this gesture
    correct_predictions = np.sum(y_pred_classes[indices] == y_test_classes[indices])
    total_predictions = len(indices)

    accuracy = (correct_predictions / total_predictions) * 100 if total_predictions > 0 else 0
    gesture_accuracy[gesture] = accuracy

# Display accuracy for each gesture
for gesture, acc in gesture_accuracy.items():
    print(f"Gesture {gesture} Accuracy: {acc:.2f}%")

import scipy.io
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import AdamW
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Load the .mat file
data = scipy.io.loadmat('/content/S1_E1_A1.mat')

# Extract EMG signals and labels
sEMG_recording = data['emg']
stimulus_labels = data['stimulus']
unique_gestures = np.unique(stimulus_labels)

# Function: Bandpass Filter (20-450Hz)
def bandpass_filter(data, lowcut=20, highcut=450, fs=1000, order=4):
    nyquist = 0.5 * fs
    low, high = lowcut / nyquist, highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data, axis=0)

sEMG_recording = bandpass_filter(sEMG_recording)

# Function: Z-score Normalization
mean, std = np.mean(sEMG_recording, axis=0), np.std(sEMG_recording, axis=0)
sEMG_recording = (sEMG_recording - mean) / std

# Convert labels to one-hot encoding
labels = to_categorical(stimulus_labels.flatten() - 1, num_classes=len(unique_gestures))

# Split into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(
    sEMG_recording, labels, test_size=0.2, random_state=42, shuffle=True
)

#  Function: Data Augmentation (Adding Gaussian Noise)
def augment_data(emg_signal):
    noise = np.random.normal(0, 0.05, emg_signal.shape)  # 5% Gaussian Noise
    return emg_signal + noise

X_train = np.array([augment_data(sample) for sample in X_train])

# Reshape for CNN (samples, time_steps, 1)
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# Final CNN Model (Adjusted for Input Shape)
model = Sequential([
    Conv1D(filters=32, kernel_size=5, activation='relu', padding='same', input_shape=(X_train.shape[1], 1)),
    BatchNormalization(),
    MaxPooling1D(pool_size=2, strides=1),  # Prevent excessive reduction
    Dropout(0.3),

    Conv1D(filters=64, kernel_size=3, activation='relu', padding='same'),
    BatchNormalization(),
    MaxPooling1D(pool_size=2, strides=1),
    Dropout(0.3),

    Conv1D(filters=128, kernel_size=3, activation='relu', padding='same'),
    BatchNormalization(),
    MaxPooling1D(pool_size=2, strides=1),
    Dropout(0.3),

    Flatten(),
    Dense(128, activation='relu'),
    BatchNormalization(),
    Dropout(0.3),

    Dense(len(unique_gestures), activation='softmax')
])

# Optimizer with Learning Rate Decay
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.001, decay_steps=1000, decay_rate=0.9
)
optimizer = AdamW(learning_rate=lr_schedule, weight_decay=1e-4)

# Compile model
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
history = model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))

# Evaluate model
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)  # Predicted class labels
y_test_classes = np.argmax(y_test, axis=1)  # True class labels

# Gesture-wise Accuracy Calculation
gesture_accuracy = {}
for gesture in unique_gestures:
    indices = np.where(y_test_classes == (gesture - 1))[0]
    correct = np.sum(y_pred_classes[indices] == y_test_classes[indices])
    accuracy = (correct / len(indices)) * 100 if len(indices) > 0 else 0
    gesture_accuracy[gesture] = accuracy

# Print Accuracy Per Gesture
for gesture, acc in gesture_accuracy.items():
    print(f"Gesture {gesture} Accuracy: {acc:.2f}%")

# Plot Training History
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Model Accuracy Over Epochs')
plt.show()