
# Microservices-Based POS System - Group Assignment 1

## Project Overview

This project is a Proof of Concept (PoC) for a microservices-based Point of Sale (POS) system. It demonstrates how microservices can manage data independently and compares this approach to monolithic and SOA architectures. By breaking the system into smaller services, it gains flexibility, scalability, and reliability, with each service handling a specific function, such as customer management, orders, inventory, or billing.

## Objectives

The main goals of this project are:

- Design a microservice-based architecture to manage separate data areas.
- Split a central database into smaller, specific databases for each area.
- Use Function-as-a-Service (FaaS) for tasks that need to work with different services.
- Evaluate the benefits and challenges of this architecture.

## Installation Guide

### Step 1: Check Prerequisites

#### Install Python 3.11:

1. Download Python 3.11 from Python’s website.
2. During installation, check the box to add Python to your PATH.

### Step 2: Download the Project

#### Clone the Repository (if using Git):
```bash
git clone <repository_url>
```

Or, download the project ZIP file and extract it to your preferred directory.

#### Navigate to the Project Folder:
```bash
cd path/to/your/project/SDA2
```

### Step 3: Set Up Docker and Database

#### Start Docker Compose:

In the project folder, ensure Docker is started, then locate the `docker-compose.yml` file. Run the following command to set up the database and services:

```bash
docker compose up -d
```

#### Load the Database Schema:

Once the Docker container is running, load the initial database structure using the command provided in `databasestart.txt`.

### Step 4: Set Up and Run Microservices

Before starting each service, it’s essential to prepare your environment and ensure each service runs independently. Follow these steps to set up and execute each microservice in the system.

#### 1. Activate Virtual Environment

Each microservice may rely on specific Python dependencies. To maintain consistency, it’s recommended to use a virtual environment (`venv`) to isolate these dependencies:

1. Navigate to the project’s main folder:
   ```bash
   cd path/to/your/project/SDA2-main
   ```

2. start the venv function

python -m venv venv

3. Activate the virtual environment (assuming it’s named `venv`):
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

#### 2. Install Python Dependencies for All Services

With the virtual environment active, install the dependencies listed in the main `requirements.txt` file. This file includes all required libraries for each microservice, eliminating the need to install dependencies separately within each service folder:

```bash
pip install -r requirements.txt
```

#### 3. Open Separate Terminals for Each Service

Each microservice needs to run on its own, often in separate terminals with an venv. This separation allows you to monitor logs for each service and manage them individually.

1. Open a new terminal for each microservice.
2. Ensure the virtual environment is activated in each terminal.

#### 4. Navigate to Each Service Folder and Start Services

In each terminal, navigate to the specific directory for the microservice you want to start:

```bash
cd path/to/your/project/SDA2/services/<service_name>
```

For example:
- `cd services/customer` for the customer service.
- `cd services/order` for the order service.

Each service folder contains the necessary files to run that particular microservice.

#### 5. Run Each Service

After navigating to each service folder, start the service by running its main script, typically `app.py` or another main entry point file. For example:

```bash
python app.py
```

This command launches the microservice in the current terminal. If everything is set up correctly, you should see log outputs indicating that the service is running.

**Note:** Each microservice is typically configured to run on a specific port. You may need to confirm these port numbers and ensure they don’t conflict with other services.

#### 6. Start the Gateway Service

The gateway acts as the API entry point for your microservices. It typically routes requests to the appropriate microservice. befor doing it dont forget the venv

1. Open a new terminal.
2. Navigate to the `gateway` folder:
   ```bash
   cd path/to/your/project/SDA2/gateway
   ```
3. Start the gateway service by running its main file:
   ```bash
   python gateway.py
   ```

Ensure the gateway service is running without errors. This service will handle external requests and communicate with the individual microservices.

#### 7. Verify All Services are Running

Each service should log its status to the terminal when it starts. Check each terminal for any errors. If there are no issues, each service should be accessible at its specified port. The gateway will direct requests to the appropriate microservices, enabling them to function as a cohesive system.

By following these detailed instructions, you should have each microservice and the gateway up and running, ready to handle requests and interact with the database.

### Step 5: Access and Test the Database

#### Open Database Interface:

In your browser, go to `localhost:8080` to access the database interface.

#### Login Credentials:

- **Server**: `customer`
- **Username**: `root`
- **Password**: `example`
- **Database**: `customer`

#### Check Data:

Verify that the Databases (like `customer`, `order`, `product`) have been created and populated with sample data.

### Step 6: Testing and API Endpoints

#### API Testing:

Use tools like Postman or cURL to send test requests to each service’s API endpoints.

Verify that you can perform basic CRUD (Create, Read, Update, Delete) operations for each service.

Test with the path `http://localhost:5000/<service>/<id>`.

For example:
```bash
http://localhost:5000/customer/1
```

You should receive the relevant data.
