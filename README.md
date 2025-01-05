# Sediment Chat Analysis

The Sentiment Analysis Application is a web-based tool designed to analyze user-provided textual input, offering insights into word frequency and sentiment polarity. This project is a Vue.js application that interacts with a Flask backend for text analysis. It allows users to input text and receive word frequency counts and sentiment analysis results.

<img src="./frontend/public/sedimentchat.svg" width="600" height="400" alt="Sediment Chat Preview">

## Project Structure

```
sediment-chat-analysis/
├── backend/
│   ├── app.py
│   ├── requirements.txt
├── frontend/
│   ├── .gitignore
│   ├── .vscode/
│   │   ├── extensions.json
│   │   ├── settings.json
│   ├── index.html
│   ├── jsconfig.json
│   ├── package.json
│   ├── public/
│   ├── src/
│   │   ├── App.vue
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── SentimentMeter.vue
│   │   │   ├── TextAnalyzer.vue
│   │   ├── index.css
│   │   ├── main.js
│   │   ├── views/
│   │   │   ├── Home.vue
│   ├── vite.config.js
├── README.md
```

### Frontend
- **[public/](frontend/public/)**: Directory for static assets such as images, fonts, and stylesheets.
- **[src/App.vue](frontend/src/App.vue)**: Root Vue component that serves as the main layout for the application.
- **[src/assets/](frontend/src/assets/)**: Directory for static assets such as images, fonts, and stylesheets.
- **[src/components/SentimentMeter.vue](frontend/src/components/SentimentMeter.vue)**: Vue component for visualizing sentiment analysis results.
- **[src/components/TextAnalyzer.vue](frontend/src/components/TextAnalyzer.vue)**: Vue component for handling user input and displaying analysis results.
- **[src/index.css](frontend/src/index.css)**: Global CSS file for styling the application.
- **[src/main.js](frontend/src/main.js)**: Entry point for the Vue application, initializing the Vue instance and mounting the app.
- **[src/views/Home.vue](frontend/src/views/Home.vue)**: Main view component that includes the TextAnalyzer component.


### Backend
- **[app.py](backend/app.py)**: Flask backend application that handles text analysis requests.
- **[requirements.txt](backend/requirements.txt)**: List of Python dependencies for the Flask backend.

## Setup Instructions

### Frontend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/hillhack/sediment-chat-analysis-.git
   cd sediment-chat-analysis/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the application:
   ```bash
   npm run dev
   ```

4. Open your browser and navigate to [http://localhost:5173](http://localhost:5173) to view the application.

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd ../backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask backend:
   ```bash
   python app.py
   ```

4. The backend will be available at [http://localhost:5000](http://localhost:5000).

## Usage
1. Enter text in the input field and submit to analyze.
2. View the word frequency count and sentiment score displayed on the page.
3. The sentiment score is visualized using a sentiment meter, which ranges from -1 (negative) to 1 (positive).

## Dependencies

### Frontend
- **Vue.js**: JavaScript framework for building the user interface.
- **Vite**: Build tool for fast development and production builds.
- **Vue DevTools**: Browser extension for debugging Vue.js applications.

### Backend
- **Flask**: Python web framework for handling backend requests.
- **Flask-CORS**: Middleware for enabling Cross-Origin Resource Sharing (CORS).
- **TextBlob**: Library for processing textual data, including sentiment analysis.
