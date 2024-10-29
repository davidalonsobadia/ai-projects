# OpenAI Text Generator App

This project is a simple web application that connects to the OpenAI API to generate text responses based on user-provided prompts. The app is divided into two main parts:
- **Frontend**: A React-based user interface where users can input prompts and see generated text.
- **Backend**: A Flask API that interacts with the OpenAI API to process prompts and return generated text.

## Project Structure

- **Frontend**: React application (`ai-app`) where users can enter prompts and submit them.
- **Backend**: Flask server (`ai-backend`) that handles incoming requests from the frontend, sends prompts to OpenAI's API, and returns the generated text.

## Requirements

### Prerequisites
- Node.js (for the frontend)
- Python 3.6+ (for the backend)
- An OpenAI API key (add it to an `.env` file)

### Environment Variables
Create an `.env` file in the root of the backend folder with the following variable:
```
OPENAI_API_KEY=your_openai_api_key
```

### Note
The project currently does not work without a valid OpenAI API key and may incur charges based on usage.

## Installation

### 1. Backend
1. **Navigate to the backend folder** and install dependencies:
```bash
pip install -r requirements.txt
```
Ensure you have your .env file set up with your OpenAI API key.

### 2. Frontend
Navigate to the frontend folder and install dependencies:
```bash
npm install
```

## Running the Project
### 1. Starting the Backend
To start the Flask server, run:

```bash
python app.py
```
The backend will be available at http://localhost:5000.

### 2. Starting the Frontend
To start the React frontend, run:

```bash
npm start
```
The frontend will be available at http://localhost:3000.

### Usage
Open the frontend in your browser at http://localhost:3000.
Enter a prompt in the text area and click "Generar" to send the prompt to the backend.
The backend will process the prompt using the OpenAI API and return the generated text to the frontend for display.
### Troubleshooting
- OpenAI API Key: Ensure you have a valid API key set in the .env file.
- Cross-Origin Issues: The backend uses flask-cors to enable CORS; ensure both backend and frontend are running on the same machine or update configurations as needed.
### License
This project is for educational and personal use. Ensure compliance with OpenAI's usage policies.

