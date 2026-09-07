# Lemon Pulse

**Smart Lemon Tree Monitoring & Diagnosis System**

Lemon Pulse is an advanced cloud-connected agricultural application built for smart lemon tree monitoring and disease diagnosis. This project leverages multiple microservices and machine learning models to provide real-time grove analytics, weather-based smart irrigation, and AI-driven agronomic advice.

## Key Features

- **Real-Time Sensor Monitoring**: Tracks Soil pH, Humidity, and Temperature, with a visual dashboard for monitoring trends.
- **Smart Irrigation Sync**: Integrates with the Open-Meteo API for real-time weather forecasting, automatically recommending or deferring irrigation based on upcoming rainfall and soil conditions.
- **AI-Powered Leaf Diagnosis**: Uses a Hugging Face Vision Transformer (ViT) model locally for classifying citrus leaf diseases. It also queries a comprehensive Hugging Face dataset (87k images) for reference matching.
- **Expert Agronomist Chatbot**: Integrated with the Cerebras Cloud LLM API for lightning-fast RAG (Retrieval-Augmented Generation) and expert advice on citrus diseases, soil care, and pest control.
- **Big Data Analytics**: Accumulates sensor data into Firebase Realtime Database and visualizes trends using PySpark Map-Reduce paradigms to track minimum and maximum extremes over time.

## Architecture & Microservices

1. **Firebase Realtime Database**: Stores an inverted search index and IoT sensor history. Allows real-time sync with no backend needed.
2. **Cerebras Cloud LLM API**: Provides high-throughput, low-latency conversational AI and RAG search capabilities for agronomic assistance.
3. **Hugging Face Datasets & Models API**: Provides zero-hosting REST search endpoints and local ViT inference for disease classification.
4. **Open-Meteo Weather API**: Retrieves real-time local weather and 12-hour rain forecasts without API key restrictions.

## Usage

The application provides a comprehensive UI (using `ipywidgets` and `matplotlib`) tailored for Jupyter/Colab environments. It includes visual charts, health scoring, daily tasks, and a fully interactive AI chatbot interface.
