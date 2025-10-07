# Online Voting System

## Overview
This project is a **Dockerized Online Voting System** built with **Python Flask**. It demonstrates a complete DevOps workflow including **CI/CD**, automated testing, and infrastructure management. The application is designed to be scalable, automated, and production-ready.

---

## Features
- **User Functionality**
  - Users can cast votes on available polls.
  - View poll results in real-time.
- **Admin Functionality**
  - Admins can create polls and view aggregated results.
- **Automated Testing**
  - Unit tests for core functionalities.
  - Integration tests for routes and APIs.
  - Selenium UI tests for end-to-end validation.
- **Infrastructure as Code**
  - **Terraform** provisions AWS EC2 instances.
  - Jenkins pipeline dynamically creates **Ansible inventory** for EC2.
  - **Ansible** configures and deploys the Dockerized application on EC2.
- **CI/CD Pipeline**
  - Jenkins pipeline automates:
    - Docker image build
    - Container deployment
    - Running all tests
    - Publishing test reports
    - Tearing down containers after execution

---

## Tech Stack
- **Backend:** Python 3.11, Flask
- **Frontend:** Jinja2 templating
- **Database:** Redis (can be extended to RDS)
- **Containerization:** Docker
- **CI/CD:** Jenkins
- **Infrastructure:** Terraform (AWS EC2)
- **Configuration Management:** Ansible (via dynamic inventory)
- **Testing:** pytest, Selenium

---

## Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Jenkins configured for CI/CD
- AWS account (for Terraform infrastructure)

### Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/karuna299/online-voting.git
   cd online-voting

2. Build and start containers:

docker-compose up -d --build


3. Run tests inside the web container:

docker-compose exec web pytest -v


4. Tear down containers:

docker-compose down -v




---

## CI/CD Pipeline (Jenkins)

### Infrastructure Stage:

- Terraform provisions EC2 instances dynamically.

- Jenkins generates a dynamic inventory file for Ansible.


### Configuration Stage:

- Ansible uses the dynamic inventory to SSH into EC2 and deploy the Dockerized app.

### Build Stage:

- Builds Docker image of the application.

### Test Stage:

- Runs unit, integration, and Selenium tests.


### Report Stage:

- Publishes test results as JUnit reports.


### Tear Down Stage:

- Stops and removes all containers after pipeline execution.




---

## Infrastructure

- Terraform: Automates provisioning of AWS EC2 instances.

- Ansible: Deploys and configures Docker containers using dynamic inventory.

- Jenkins: Orchestrates both infrastructure provisioning and app deployment.

- Scalability: Can be extended with ALB and RDS for production-ready deployment.



---

## Future Enhancements

- Integrate RDS for persistent database storage.

- Implement AWS Application Load Balancer (ALB) for high availability and scaling.

- Enable multi-AZ deployment for production resilience.



---

## Conclusion

- This project demonstrates hands-on DevOps skills along with application development. Highlights include:

- Automation with CI/CD

- Containerization with Docker

- Infrastructure as Code with Terraform

- Configuration management with Ansible (dynamic inventory via Jenkins)

- End-to-end testing including Selenium
---