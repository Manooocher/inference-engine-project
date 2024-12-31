# inference engine project   /////////////////////////////////   developed by Manooooooch

## Introduction
inference engine project is a comprehensive logic inference system designed to process and infer logical expressions. The project is divided into three main components:

1. **Backend**: An Express.js server written in TypeScript that handles API requests and serves the frontend.
2. **Frontend**: A Next.js application written in TypeScript that provides a user interface for interacting with the logic inference system.
3. **Inference Engine**: A Python-based engine that parses logical expressions and performs inference using various libraries.

## Project Structure
The project is organized into the following directories:

- `backend/`: Contains the Express.js server code.
- `frontend/`: Contains the Next.js application code.
- `inference-engine/`: Contains the Python-based inference engine code.

## Setup
To set up the project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Manooocher/inference-engine-project.git
    cd inference-engine-project
    ```

2. **Backend**:
    - Navigate to the [backend](http://_vscodecontentref_/0) directory:
        ```bash
        cd backend
        ```
    - Install dependencies:
        ```bash
        npm install
        ```
    - Create a [.env](http://_vscodecontentref_/1) file and add your environment variables.

3. **Frontend**:
    - Navigate to the `frontend` directory:
        ```bash
        cd ../frontend
        ```
    - Install dependencies:
        ```bash
        npm install
        ```
    - Create a [.env](http://_vscodecontentref_/2) file and add your environment variables.

4. **Inference Engine**:
    - Navigate to the [inference-engine](http://_vscodecontentref_/3) directory:
        ```bash
        cd ../inference-engine
        ```
    - Create a virtual environment and activate it:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```
    - Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    - Create a [.env](http://_vscodecontentref_/4) file and add your environment variables.

## Running the Project
To run the entire project using Docker Compose, use the following command:
```bash
docker-compose up --build