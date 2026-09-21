# 🍔 Food Delivery Services — Microservices & DevOps Project

A production-style **food delivery platform** designed and deployed as a **microservices-based application**, with a strong focus on **DevOps, automation, containerization, cloud infrastructure, CI/CD, Kubernetes, and observability**.

This project is being built as a hands-on learning and portfolio project to demonstrate how a modern distributed application can be developed, containerized, deployed, automated, monitored, and managed.

---

## 🎯 Project Goal

The goal is to build a food delivery platform composed of independently deployable services and progressively implement a complete DevOps workflow around it.

The project will evolve from:

**Local development → Docker → CI/CD → Kubernetes → Infrastructure as Code → AWS**

The focus is not only on building the application, but on understanding **how to deploy, automate, secure, monitor, and operate it**.

---

## 🏗️ Planned Architecture

The platform will initially consist of several independent microservices:

```text
                         ┌──────────────────┐
                         │      Client      │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   API Gateway    │
                         │      NGINX       │
                         └────────┬─────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
        ┌───────────┐       ┌───────────┐       ┌───────────┐
        │   User    │       │ Restaurant│       │   Order   │
        │  Service  │       │  Service  │       │  Service  │
        └─────┬─────┘       └─────┬─────┘       └─────┬─────┘
              │                   │                   │
              ▼                   ▼                   ▼
        ┌───────────┐       ┌───────────┐       ┌───────────┐
        │ PostgreSQL│       │ PostgreSQL│       │ PostgreSQL│
        └───────────┘       └───────────┘       └───────────┘

                         ┌──────────────────┐
                         │ Payment Service  │
                         └────────┬─────────┘
                                  │
                         ┌────────▼─────────┐
                         │  Driver Service  │
                         └────────┬─────────┘
                                  │
                         ┌────────▼─────────┐
                         │Notification      │
                         │Service           │
                         └──────────────────┘
```

> The architecture is currently a starting point and will be refined during the system-design phase.

---

## 🧩 Planned Microservices

| Service              | Responsibility                                 |
| -------------------- | ---------------------------------------------- |
| User Service         | User registration, authentication and profiles |
| Restaurant Service   | Restaurants, menus and food items              |
| Order Service        | Order creation and order management            |
| Payment Service      | Payment processing and payment status          |
| Driver Service       | Drivers and delivery assignment                |
| Notification Service | Order and delivery notifications               |
| API Gateway          | Routing client requests to services            |

Additional services may be introduced if they provide a clear architectural or DevOps learning benefit.

---

## 🛠️ Technology Stack

### Application

* Python
* Flask / REST APIs
* PostgreSQL
* Redis

### Networking & Gateway

* NGINX
* HTTP/REST
* Service-to-service communication

### Version Control

* Git
* GitHub

### Containers

* Docker
* Docker Compose

### CI/CD

* GitHub Actions
* Automated testing
* Docker image builds
* Container image security scanning
* Container registry

### Container Orchestration

* Kubernetes
* Kubernetes Deployments
* Services
* ConfigMaps
* Secrets
* Ingress
* Persistent Volumes
* Health checks
* Resource management

### Infrastructure as Code

* Terraform
* AWS infrastructure provisioning

### Cloud

* Amazon Web Services (AWS)
* Amazon EKS
* Amazon ECR
* Amazon RDS
* AWS VPC
* AWS IAM
* AWS Load Balancer

### Observability

* Prometheus
* Grafana
* Application logging
* Kubernetes logging
* Health checks and metrics

### Security

* JWT authentication
* Kubernetes Secrets
* RBAC
* Network Policies
* Container image scanning
* Dependency/security scanning

---

## 🚀 DevOps Workflow

The intended workflow is:

```text
Developer
    │
    ▼
   Git
    │
    ▼
 GitHub
    │
    ▼
GitHub Actions
    │
    ├── Tests
    ├── Linting
    ├── Security Scan
    ├── Docker Build
    └── Push Image
             │
             ▼
      Container Registry
             │
             ▼
        Kubernetes
             │
             ▼
          AWS EKS
             │
       ┌─────┴─────┐
       ▼           ▼
   Monitoring    Logging
       │           │
       ▼           ▼
   Prometheus    Grafana
```

Infrastructure will eventually be provisioned using:

```text
Terraform
    │
    ▼
   AWS
    │
    ├── VPC
    ├── Networking
    ├── IAM
    ├── ECR
    ├── EKS
    └── RDS
```

---

## 📚 Project Learning Objectives

Through this project, the following areas will be explored:

* Microservices architecture
* REST API design
* Service-to-service communication
* Database-per-service architecture
* Docker containerization
* Docker networking
* Docker Compose
* Git and GitHub workflows
* CI/CD pipelines
* Automated testing
* Container image security
* Kubernetes orchestration
* Kubernetes networking
* Kubernetes configuration and secrets
* Infrastructure as Code
* Terraform
* AWS infrastructure
* EKS
* Container registries
* Application monitoring
* Centralized logging
* Security practices
* Troubleshooting distributed applications

---

## 🗺️ Development Roadmap

The project will be developed incrementally.

### Phase 1 — System Design

* [ ] Define business requirements
* [ ] Define microservices
* [ ] Define service responsibilities
* [ ] Design database-per-service architecture
* [ ] Define service communication
* [ ] Design API endpoints
* [ ] Design authentication flow
* [ ] Design order lifecycle
* [ ] Design payment flow
* [ ] Design delivery workflow
* [ ] Identify failure scenarios
* [ ] Create architecture diagrams
* [ ] Finalize technology choices

### Phase 2 — Application Development

* [ ] Create repository structure
* [ ] Build User Service
* [ ] Build Restaurant Service
* [ ] Build Order Service
* [ ] Build Payment Service
* [ ] Build Driver Service
* [ ] Build Notification Service
* [ ] Configure API Gateway
* [ ] Implement service communication
* [ ] Add testing

### Phase 3 — Docker

* [ ] Create Dockerfiles
* [ ] Build service images
* [ ] Configure Docker networks
* [ ] Configure environment variables
* [ ] Add container health checks
* [ ] Create Docker Compose environment
* [ ] Test the complete platform locally

### Phase 4 — CI/CD

* [ ] Create GitHub Actions workflows
* [ ] Automate testing
* [ ] Automate linting
* [ ] Build Docker images automatically
* [ ] Scan images for vulnerabilities
* [ ] Push images to a container registry
* [ ] Automate deployment

### Phase 5 — Kubernetes

* [ ] Create local Kubernetes cluster
* [ ] Create namespaces
* [ ] Create Deployments
* [ ] Create Services
* [ ] Configure ConfigMaps
* [ ] Configure Secrets
* [ ] Configure Ingress
* [ ] Configure persistent storage
* [ ] Add readiness probes
* [ ] Add liveness probes
* [ ] Configure resource requests/limits
* [ ] Test scaling and failure recovery

### Phase 6 — Observability

* [ ] Application logging
* [ ] Kubernetes logging
* [ ] Prometheus
* [ ] Grafana
* [ ] Application metrics
* [ ] Service health monitoring
* [ ] Dashboard creation
* [ ] Alerting

### Phase 7 — Infrastructure as Code

* [ ] Learn Terraform project structure
* [ ] Create Terraform configuration
* [ ] Provision AWS networking
* [ ] Configure IAM
* [ ] Create ECR repositories
* [ ] Provision EKS
* [ ] Provision database infrastructure
* [ ] Manage infrastructure through Terraform
* [ ] Document Terraform workflow

### Phase 8 — AWS Deployment

* [ ] Deploy container images to ECR
* [ ] Deploy Kubernetes workloads to EKS
* [ ] Configure AWS networking
* [ ] Configure load balancing
* [ ] Connect application to managed databases
* [ ] Configure monitoring
* [ ] Test production-style deployment

### Phase 9 — Security & Hardening

* [ ] Secure application configuration
* [ ] Remove hardcoded secrets
* [ ] Configure Kubernetes Secrets
* [ ] Configure RBAC
* [ ] Add Network Policies
* [ ] Run container security scans
* [ ] Review IAM permissions
* [ ] Harden containers
* [ ] Review exposed services

### Phase 10 — Documentation & Final Demo

* [ ] Architecture documentation
* [ ] API documentation
* [ ] Deployment documentation
* [ ] CI/CD documentation
* [ ] Terraform documentation
* [ ] Troubleshooting guide
* [ ] Monitoring dashboard
* [ ] Final architecture diagram
* [ ] Project demonstration

---

## 📂 Planned Repository Structure

```text
food-delivery-services/
│
├── services/
│   ├── user-service/
│   ├── restaurant-service/
│   ├── order-service/
│   ├── payment-service/
│   ├── driver-service/
│   └── notification-service/
│
├── gateway/
│
├── docker/
│
├── kubernetes/
│
├── terraform/
│
├── monitoring/
│
├── tests/
│
├── docs/
│
├── .github/
│   └── workflows/
│
├── .gitignore
└── README.md
```

The structure will be refined as the architecture develops.

---

## 🧠 Engineering Approach

This project will follow a **build → test → automate → deploy → monitor → improve** approach.

Rather than introducing every technology at once, each technology will be introduced when there is a clear reason for using it.

For example:

```text
Microservices
      ↓
Docker
      ↓
Docker Compose
      ↓
CI/CD
      ↓
Kubernetes
      ↓
Observability
      ↓
Terraform
      ↓
AWS / EKS
      ↓
Security & Hardening
```

---

## 📖 Documentation

Detailed documentation will be maintained in the `docs/` directory.

Planned documentation includes:

* System Architecture
* API Documentation
* Database Design
* Docker Guide
* Kubernetes Guide
* CI/CD Pipeline
* Terraform Infrastructure
* AWS Deployment
* Monitoring & Logging
* Security
* Troubleshooting

---

## ⭐ Project Status

**Status:** 🟡 Planning / System Design

The project is currently at the planning stage.

The next step is to finalize the system architecture before implementation begins.

---

## 👩‍💻 Author

**Janet Wanjiru**

Computer Science Student | Aspiring DevOps Engineer

---

## 📌 Disclaimer

This is a learning and portfolio project designed to explore modern software delivery and DevOps practices through a realistic microservices application.
