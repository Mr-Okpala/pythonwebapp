# Python Flask Dockerized Application

This project is a simple Python Flask application that is containerized using Docker. The setup uses a lightweight Python runtime image and follows best practices for building efficient Docker containers.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Python](https://www.python.org/) (if testing locally without Docker)

## Project Structure

```
.
├── app.py               # The Flask application entry point
├── requirements.txt     # Python dependencies for the application
├── Dockerfile           # Instructions for building the Docker image
└── README.md            # Documentation for the project
```

## Dockerfile Explanation

The `Dockerfile` defines the steps to build a Docker image for this project:

1. **Base Image**
   ```dockerfile
   FROM python:3.10-slim
   ```
   This specifies the official lightweight Python 3.10 image as the base.

2. **Set Working Directory**
   ```dockerfile
   WORKDIR /app
   ```
   All subsequent commands will be executed in the `/app` directory within the container.

3. **Copy Application Files**
   ```dockerfile
   COPY . /app
   ```
   Copies the project files from the local machine to the container's `/app` directory.

4. **Install Dependencies**
   ```dockerfile
   RUN pip install --no-cache-dir -r requirements.txt
   ```
   Installs Python packages specified in `requirements.txt`.

5. **Expose Port**
   ```dockerfile
   EXPOSE 5000
   ```
   Opens port 5000 for accessing the Flask application.

6. **Run Application**
   ```dockerfile
   CMD ["python", "app.py"]
   ```
   Sets the default command to execute the Flask application.

## How to Build and Run the Application

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Build the Docker image:
   ```bash
   docker build -t flask-app .
   ```

3. Run the container:
   ```bash
   docker run -p 5000:5000 flask-app
   ```

4. Access the application in your browser at `http://localhost:5000`.


## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.


