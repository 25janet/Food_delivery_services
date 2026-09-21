# Phase 1 — System Design

The purpose of Phase 1 is to answer one question:

> **What exactly are we building, and how should all the pieces interact?**

Before Docker, Kubernetes, Terraform, or CI/CD, we need a solid application architecture. We will work through 14 design decisions, starting with **Business Requirements**.

---

## 1. Business Requirements

### 1.1 What are we building?
We are building a simplified food delivery platform where:
* Customers can create accounts.
* Customers can browse restaurants.
* Customers can view menus.
* Customers can place food orders.
* Customers can make a payment.
* Restaurants can manage their menus and orders.
* Drivers can receive delivery assignments.
* Customers can track the status of their orders.
* The system can send notifications about important order events.

> **Note:** The application is intentionally simplified compared to commercial platforms like Uber Eats or Glovo. The goal isn't to recreate every feature, but rather to create enough business functionality to serve as a realistic distributed system for DevOps operation.

---

### 1.2 Actors

We have three main user types interacting with the system:

#### 👤 Customer
* Register and log in.
* Browse restaurants and view menus.
* Add food to an order and place an order.
* Pay for an order.
* View current order status and order history.

#### 🍽️ Restaurant
* Register and manage restaurant profile.
* Add, update, and remove menu items.
* View incoming orders.
* Accept or reject orders.
* Update food preparation status.

#### 🛵 Driver
* Register and manage driver profile.
* View available delivery assignments.
* Accept a delivery.
* Update delivery status.
* Mark a delivery as completed.

---

### 1.3 Core Business Flow

```
Customer
   │
   ▼
Browse Restaurant
   │
   ▼
Select Food
   │
   ▼
Create Order
   │
   ▼
Payment
   │
   ▼
Restaurant Receives Order
   │
   ▼
Restaurant Prepares Order
   │
   ▼
Driver Assigned
   │
   ▼
Driver Picks Up Order
   │
   ▼
Driver Delivers Order
   │
   ▼
Order Completed
```

#### Why split into services?
* **Payment Service:** Payment handling is a distinct business and compliance responsibility.
* **Driver Service:** Delivery management operates independently from kitchen management.
* **Notification Service:** Asynchronous notifications are triggered by decoupled domain events.

---

### 1.4 Functional Requirements

#### User Management
* Register, log in, view profile, and update profile.

#### Restaurant Management
* Create restaurant profile, manage menu (add/update/remove items), view incoming orders.

#### Food Browsing
* View list of restaurants, view restaurant details, view menus, and view individual food items.

#### Order Management
* **Customer:** Create order, view order status, view order history, cancel order.
* **Restaurant:** Accept order, reject order, update preparation status.

#### Payment
* Create payment, process payment, check payment status, associate payment with an order.
* *Implementation Note:* Payments are simulated (`SUCCESS` vs. `FAILED`) to demonstrate distributed transactions without requiring real money processing.

```
Payment Request ──► Payment Service ──┬──► SUCCESS
                                     └──► FAILED
```

#### Delivery
* Assign driver, accept delivery, update delivery status, complete delivery.

```
PENDING ──► ASSIGNED ──► ACCEPTED ──► PICKED_UP ──► OUT_FOR_DELIVERY ──► DELIVERED
```

#### Notifications
* Generate notifications for key events:
  * Order Created $\rightarrow$ *"Your order has been received."*
  * Payment Successful $\rightarrow$ Notification sent
  * Driver Assigned $\rightarrow$ Notification sent
  * Order Delivered $\rightarrow$ Notification sent

---

### 1.5 Non-Functional Requirements

* **Scalable:** Individual microservices can be scaled independently (e.g., scaling `Order Service` to 4 pods while `Notification Service` runs on 1 pod).
* **Resilient:** High fault tolerance. If `Notification Service` fails, `Order Service` must continue to process orders.
* **Observable:** Metrics, logs, trace events, and health checks integrated via Prometheus & Grafana.
* **Secure:** JWT-based authentication, RBAC, password hashing, container security, network policies, and cloud secrets management.
* **Automated:** Fully automated CI/CD pipeline:
  ```
  git push ──► CI ──► Tests ──► Security Scan ──► Docker Build ──► Push Image ──► Deploy
  ```

---

### 1.6 Important Business Rules

1. **Order Rule:** A customer cannot place an order for a restaurant that does not exist.
2. **Payment Rule:** An order must not be confirmed if the payment fails.
3. **Delivery Rule:** A driver cannot be assigned to an order before it reaches the `READY_FOR_PICKUP` stage.
4. **Driver Constraint:** A driver cannot be assigned multiple active deliveries at the same time.

---



---

### 1.7 Minimum Viable Product (MVP) Scope

```
                 FOOD DELIVERY MVP
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
      Users        Restaurants         Drivers
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                      Orders
                        │
                        ▼
                     Payment
                        │
                        ▼
                    Delivery
                        │
                        ▼
                  Notifications
```

#### Target E2E Journey:
```
Register ──► Login ──► Browse Restaurant ──► Select Food ──► Place Order ──► Pay ──► Restaurant Accepts ──► Food Prepared ──► Driver Assigned ──► Driver Picks Up ──► Driver Delivers ──► Order Completed
```

---

## 📋 System Design Decisions Summary

| Area | Decision |
| :--- | :--- |
| **Platform** | Food Delivery Platform |
| **Main Actors** | Customer, Restaurant, Driver |
| **Core Entity** | Order |
| **Payment** | Simulated (`SUCCESS` / `FAILED`) |
| **Delivery** | Driver Assignment + Lifecycle Status Tracking |
| **Communication** | API-based (REST / Event-driven) |
| **Architecture** | Microservices Architecture |
| **Databases** | Database-per-service pattern |
| **Containers** | Docker |
| **Orchestration** | Kubernetes |
| **CI/CD** | GitHub Actions |
| **IaC** | Terraform |
| **Cloud** | AWS |
| **Monitoring** | Prometheus + Grafana |
| **Initial Goal** | Working End-to-End MVP |