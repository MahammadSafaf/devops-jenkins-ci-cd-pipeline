# CI/CD Pipeline using Jenkins, Docker, GitHub and AWS EC2

## 🚀 Project Overview
This project demonstrates a complete DevOps CI/CD pipeline to deploy a Flask web application using Jenkins, Docker, GitHub, and AWS EC2.

The application is containerized using Docker and deployed on an AWS EC2 instance. Jenkins automates the build and deployment process.

---

## 🛠️ Tech Stack
- Python (Flask)
- Docker
- Jenkins
- Git & GitHub
- AWS EC2 (Ubuntu)
- Linux

---

## 🧱 Architecture Flow
Developer → GitHub → Jenkins → Docker Build → AWS EC2 → Web Application

---

## 📂 Project Structure
- app.py  
- Dockerfile  
- README.md  

---

## 🐍 Flask Application
A simple Flask application running on port 5000 and accessible via browser.

---

## 🐳 Docker Setup

### Build Docker Image
docker build -t myapp .

### Run Docker Container
docker run -d -p 5000:5000 myapp

---

## 🌐 Access Application
Open in browser:
http://<EC2-PUBLIC-IP>:5000

Example:
http://13.xx.xx.xx:5000

---

## 🔁 CI/CD Pipeline Workflow
- Push code to GitHub  
- Jenkins pulls code  
- Docker image is built  
- Container is deployed on AWS EC2  
- Application runs on port 5000  

---

## ⚙️ Jenkins Role
- Automates build and deployment  
- Integrates with GitHub  
- Builds Docker image  
- Runs container  

---

## 🧪 Testing & Verification
Check running containers:
docker ps

Check logs:
docker logs <container_id>

Test in browser:
http://<EC2-PUBLIC-IP>:5000

---

## 🧹 Cleanup (IMPORTANT)
docker stop <container_id>  
docker rm <container_id>  
docker rmi myapp  

Terminate EC2 instance from AWS Console to avoid billing.

---

## 🎯 Key Learning Outcomes
- CI/CD pipeline implementation  
- Docker containerization  
- Jenkins automation  
- AWS EC2 deployment  
- GitHub version control  
- Linux basics  

---

## 👨‍💻 Author
DevOps Learning Project by MAHAMMAD SAFAF
