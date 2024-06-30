# FastAPI Project

This project is a FastAPI application that processes image data and exposes an API for various operations, including resizing images, storing them in a database, and applying custom color maps.

## Requirements

refer requirements.txt

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/athul911/AIQ-python.git
    cd AIQ-python
    ```

2. **Install dependencies(use a virtual env):**

    ```bash
    pip install -r requirements.txt
    ```

3. ```bash
    fastapi src/main.py --reload or fastapi dev src/main.py --reload (for dev)
    ```

## Running the Application with Docker

### Build the Docker Image

To build the Docker image for the FastAPI application:

```bash
docker build -t fastapi-app .

### Run the container
docker run -d -p 8000:8000 --name fastapi-container fastapi-app

###Access app
http://localhost:8000/docs

##Testing
note: insert the image data to the test db before running the test. once inserted, use the file to update the csv_file_id constant inside /tests/constants.py::Constants
Also the current test coverage report is available in the repo

pytest --cov=src