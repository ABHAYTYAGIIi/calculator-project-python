# Python Calculator – CI/CD Deployment with Azure DevOps

A simple Python calculator application deployed to an Azure Virtual Machine using an automated CI/CD pipeline with Azure DevOps.

## Project Overview

This project demonstrates a basic DevOps workflow where application source code is stored in Git and automatically built, tested, and deployed to an Azure VM through an Azure DevOps pipeline.

The project was created to practice:

- Python application development
- Git and version control
- Azure DevOps Repos
- Azure DevOps Pipelines
- CI/CD automation
- Automated testing with pytest
- Deployment to an Azure Virtual Machine
- Linux server administration

## Architecture

```text
Developer
   |
   v
Git Repository
   |
   v
Azure DevOps Pipeline
   |
   +------------------+
   |                  |
   v                  v
Build & Test      Deployment
   |                  |
   |                  v
   |            Azure VM
   |                  |
   |                  v
   +----------> Python Application

Technologies Used
Python
Pytest
Git
Azure DevOps
Azure Repos
Azure Pipelines
Azure Virtual Machine
Linux
SSH
Project Structure
calculator-project-python/
│
├── app.py
├── calculator.py
├── test_calculator.py
├── requirements.txt
├── azure-pipelines.yml
├── README.md
└── .gitignore
Application

The calculator supports basic arithmetic operations such as:

Addition
Subtraction
Multiplication
Division

The application logic is implemented in calculator.py, while app.py is used to run the application.

Testing

The project uses pytest for automated testing.

Tests are located in:

test_calculator.py

Tests can be executed using:

pytest
CI/CD Pipeline

The Azure DevOps pipeline automates the application workflow.

Pipeline Flow
Code Push
   ↓
Build
   ↓
Install Dependencies
   ↓
Run Tests
   ↓
Deployment
   ↓
Azure VM

The pipeline is triggered whenever changes are pushed to the main branch.

Deployment

The application is deployed to an Azure Linux Virtual Machine.

The pipeline connects to the VM using SSH and transfers the application files before starting/restarting the application.

This eliminates the need to manually copy and deploy the application after every code change.

Key DevOps Concepts Demonstrated
Continuous Integration

Every change pushed to the main branch triggers the pipeline, which builds the application and executes automated tests.

Continuous Deployment

After successful validation, the pipeline deploys the updated application to the Azure VM.

Infrastructure
Azure
└── Virtual Machine
    └── Linux
        └── Python Calculator
How to Run Locally

Clone the repository:

git clone <repository-url>
cd calculator-project-python

Create a virtual environment:

python3 -m venv venv

Activate it:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Run tests:

pytest
Learning Outcomes

Through this project, I gained hands-on experience with:

Creating and testing a Python application
Managing source code using Git
Working with Azure DevOps Repos
Creating YAML-based CI/CD pipelines
Automating application testing
Deploying applications to Azure VMs
Using SSH for remote deployment
Understanding the flow from source code to production


Author

Abhay Tyagi
