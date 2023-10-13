# FastAPI Dockerized Project

This is a template project for building a FastAPI application and containerizing it with Docker. It also includes a requirements.txt file to manage project dependencies.

## Getting Started

Follow these steps to clone the project, build a Docker container, and manage requirements.

### Prerequisites

- Docker: You must have Docker installed on your system.

### Cloning the Project

Clone the repository to your local machine:

```bash
git clone https://github.com/Sanjeev-Gautam/FastAPI.git
cd FastAPI

Building the Docker Container

docker build -t fastapi-app .

Running the Docker Container

docker run -d -p 8000:8000 fastapi-app

#Your FastAPI application should now be accessible at http://localhost:8000

Managing Requirements

pip install -r requirements.txt
