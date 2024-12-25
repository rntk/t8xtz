# FastAPI Project

This is a base structure for a FastAPI project with separated modules for handlers, middlewares, and so on.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rntk/t8xtz.git
   ```
2. Navigate to the project directory:
   ```bash
   cd t8xtz
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```
2. Open your browser and navigate to `http://127.0.0.1:8000` to see the API documentation.
