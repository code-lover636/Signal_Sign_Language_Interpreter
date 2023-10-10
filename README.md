# SIGNAL
### Sign Language Interpreter with Random Forest Regressor
This project was made as a part of Chakravyuha hackathon and we emerged as one of the finalists. <be>
This Sign Language Interpreter project utilizes Machine Learning techniques, specifically the Random Forest Regressor, in conjunction with the Google Mediapipe library to interpret sign language gestures. 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)

## Introduction

This project aims to create a real-time sign language interpreter using the Random Forest Regressor model. The Google Mediapipe library is used for hand tracking and landmark detection. This combination of technologies allows for accurate interpretation of sign language gestures.

## Features

- Real-time sign language interpretation.
- Random Forest Regressor model for gesture recognition.
- Google Mediapipe for hand tracking and landmark detection.

## Requirements

- Python 3.6+
- [Streamlit](https://streamlit.io/)
- [Google Mediapipe](https://mediapipe.dev/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/code-lover636/Signal_Sign_Language_Interpreter.git
   cd Signal_Sign_Language_Interpreter
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run detection.py
   ```

2. Open a web browser and navigate to the provided URL.

3. The web application will display a video stream with the hand landmarks highlighted.

4. Make sign language gestures in front of your camera and observe the predicted gesture.

## Demo

![Demo GIF](https://github.com/code-lover636/Chakravyuh_Hackathon/assets/77882744/d98f004c-30c3-4e96-8100-425b5b310dac)

