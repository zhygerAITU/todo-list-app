# Just Do It - To-Do List WebApp

Just Do It is a simple To-Do List WebApp built with Flask, HTML, CSS, and JavaScript.

## Prerequisites

Before you begin, ensure you have the following requirements installed on your machine:

- Python (version 3.7 or higher)
- pip (Python package installer)
- Git

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/zhygerAITU/todo-list-app.git
   cd just-do-it
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **On Windows (Command Prompt):**
     ```bash
     venv\Scripts\activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application:**
   ```bash
   python run.py
   ```

6. **Open Your Browser:**
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser to use the To-Do List WebApp.

7. **After making these changes, deactivate and reactivate your virtual environment, and reinstall the dependencies:**
    - **On macOS/Linux:**
     ```bash
     deactivate
     ```
     - **On Windows (Command Prompt):**
     ```bash
     deactivate
     ```

    # Then reactivate

## Project Structure

- **`app/`**: Contains the Flask application code.
  - **`templates/`**: HTML templates.
  - **`static/`**: Static files (CSS, JS, images).
  - **`models.py`**: Defines the data models.
  - **`config.py`**: Configuration settings.
  - **`routes.py`**: Defines the application routes.

- **`run.py`**: Script to initialize the Flask app, create the database tables, and run the development server.

