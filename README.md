# CI/CD Pipeline using Jenkins, Docker, GitHub and AWS EC2

## 🚀 Project Overview
This project demonstrates a complete DevOps CI/CD pipeline for deploying a Flask web application using Jenkins, Docker, GitHub, and AWS EC2.

The application is containerized using Docker and deployed on an AWS EC2 instance. Jenkins automates the build and deployment process, enabling continuous integration and continuous deployment.

---
## 🛠️ Tech Stack
- Python (Flask)
- Docker
- Jenkins
- Git & GitHub
- AWS EC2 (Ubuntu)
- Linux (CLI)

---
## 🧱 Architecture Flow

Developer → GitHub → Jenkins → Docker Build → AWS EC2 Deployment → Web Application

---
## 📂 Project Structure
app.py Dockerfile README.md

---
## 🐍 Flask Application (app.py)

A simple Flask web application that runs on port 5000 and displays a message in the browser.

---## 🐳 Docker Setup

### 🔹 Build Docker Image
```bash
docker build -t myapp .
🔹 Run Docker Container
Bash
Copy code
docker run -d -p 5000:5000 myapp
🌐 Access Application
After deployment, open in browser:
Copy code

http://<EC2-PUBLIC-IP>:5000
Example:
Copy code

http://13.xx.xx.xx:5000
🔁 CI/CD Pipeline Workflow
Developer pushes code to GitHub repository
Jenkins pulls latest code from GitHub
Jenkins builds Docker image
Docker container is deployed on AWS EC2
Application becomes accessible via public IP
⚙️ Jenkins Role
Automates build and deployment
Pulls code from GitHub
Builds Docker image
Runs Docker container on EC2
🧪 Testing & Verification
Check running containers:
Bash
Copy code
docker ps
Check logs:
Bash
Copy code
docker logs <container_id>
Check application:
Open browser:
Copy code

http://<EC2-PUBLIC-IP>:5000
🧹 Cleanup (IMPORTANT for AWS cost control)
Stop container:
Bash
Copy code
docker stop <container_id>
Remove container:
Bash
Copy code
docker rm <container_id>
Remove image:
Bash
Copy code
docker rmi myapp
Stop EC2 instance:
Go to AWS Console → EC2 → Instances → Terminate instance
🎯 Key Learning Outcomes
CI/CD pipeline implementation
Docker containerization
Jenkins automation
AWS EC2 deployment
GitHub version control
Linux server management
Real-world DevOps workflow
👨‍💻 Author
DevOps Learning Project by MAHAMMAD SAFAF
