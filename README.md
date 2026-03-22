# 🚀 CI/CD Pipeline using Jenkins, Docker & GitHub

## 📌 Project Overview
This project demonstrates a complete CI/CD pipeline using Jenkins, Docker, and GitHub. The goal is to automate the process of building, testing, and deploying a containerized web application whenever code is pushed to the GitHub repository.

The application is a simple Python Flask web app that runs inside a Docker container and is automatically deployed using Jenkins.

---
## 🎯 Objectives
- Automate build and deployment process using CI/CD
- Integrate GitHub with Jenkins for automatic triggers
- Containerize application using Docker
- Deploy and run application in a consistent environment

---
## 🛠️ Tech Stack Used
- Linux (Ubuntu)
- Jenkins (CI/CD Automation)
- Docker (Containerization)
- Git & GitHub (Version Control)
- Python Flask (Web Application)
- Bash (Basic scripting)

---
## 📁 Project Structure
devops-jenkins-ci-cd-pipeline/ │ ├── app.py ├── Dockerfile ├── requirements.txt ├── Jenkinsfile (optional) └── README.md

---
## 🚀 How It Works
1. Developer pushes code to GitHub repository
2. Jenkins detects the change using GitHub webhook
3. Jenkins pulls latest code from repository
4. Docker image is built using Dockerfile
5. Existing container is stopped and removed (if running)
6. New container is created and deployed
7. Application is accessible via browser

---
## 🐍 Flask Application Code

The application contains a simple Flask server with multiple routes:

- / → Home page
- /health → Health check endpoint
- /version → Version information

---
## 📦 Docker Setup

### Dockerfile
- Uses Python base image
- Installs dependencies
- Runs Flask application on port 5000

---
## ⚙️ CI/CD Pipeline (Jenkins)

Jenkins is configured to:
- Pull code from GitHub repository
- Build Docker image
- Stop old container (if exists)
- Run new Docker container
- Expose application on port 5000

---
## 🌐 Application Access

Once deployed, the application can be accessed using:
http://localhost:5000⁠�

or server IP:
http://:5000
Copy code

---
## 🧪 Endpoints

| Endpoint | Description |
|----------|------------|
| / | Home route |
| /health | Health check |
| /version | App version |

---
## 📌 Key Features
- Fully automated CI/CD pipeline
- Docker containerized deployment
- GitHub integration with Jenkins
- Easy rollback by rebuilding containers
- Lightweight Flask application

---
## 🧠 What I Learned
- Setting up Jenkins CI/CD pipeline
- Docker image creation and container management
- GitHub webhook integration
- Linux server management
- Debugging deployment issues using logs

---
## 🐛 Troubleshooting
- If container is not running: check docker ps -a
- If app not accessible: verify port 5000 is open
- If build fails: check Jenkins console logs
- If Flask error occurs: check docker logs <container_id>

---
## 📌 Author
*MAHAMMAD SAFAF*  

---
## 🚀 Future Improvements
- Add Kubernetes deployment
- Add automated testing stage
- Add AWS deployment integration
- Improve logging and monitoring
