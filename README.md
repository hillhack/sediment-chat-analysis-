# Sentiment Chat Analysis

The Sentiment Analysis Application is a web-based tool designed to analyze user-provided textual input, offering insights into word frequency and sentiment polarity. This project is a Vue.js application that interacts with a Flask backend for text analysis. It allows users to input text and receive word frequency counts and sentiment analysis results.
![Screenshot from 2025-01-05 17-20-57](https://github.com/user-attachments/assets/b3bc7479-2961-45bd-86b1-2071ba42d58b)
![Screenshot from 2025-01-05 17-20-42](https://github.com/user-attachments/assets/1febabd9-0cf8-4d52-8536-5d3ea3d36afd)
![Screenshot from 2025-01-05 12-57-23](https://github.com/user-attachments/assets/421ba6af-011a-436f-a946-85f5e81bc539)
![Screenshot from 2025-01-05 12-28-53](https://github.com/user-attachments/assets/dbeef9c8-11ed-4dd9-9c64-f4c97ce27399)



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
   git clone https://github.com/hillhack/sentiment-chat-analysis-.git
   cd sentiment-chat-analysis/frontend
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
