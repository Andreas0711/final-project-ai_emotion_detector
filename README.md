# Repository for final project

## Emotion Detection System - Flask & Watson AI
This repository contains a **Python-based web application** developed as a final project. The core functionality is to analyze the emotional tone of a given text using IBM Watson's Natural Language Processing (NLP) capabilities.

### 🚀 Key Features
* **AI-Powered Analysis:** Integrates with the Watson NLP Runtime API to detect specific emotions.
* **Multi-Emotion Scoring:** The system extracts and displays scores for five distinct categories: Anger, Disgust, Fear, Joy, and Sadness.
* **Dominant Emotion Logic:** Custom Python logic to calculate the highest-scoring emotion from the API's JSON response.
* **Robust Backend:** Built with the Flask micro-framework for high performance and easy routing.
* **Unit Testing:** Includes a testing suite to validate emotion accuracy and handle edge cases like blank inputs.

### 🛠️ Tech Stack
* **Language:** Python 3.11
* **Framework:** Flask (Web Server & Routing)
* **API:** IBM Watson NLP (Emotion Prediction Service)
* **Libraries:** `requests`, `json`, `unittest`

### 📂 Project Structure
* **server.py**: The entry point of the Flask application.
* **EmotionDetection/**: A dedicated package containing the logic for API calls.
* **tests/**: Unit tests to ensure the application behaves as expected.
* **templates/**: HTML interface for user interaction.