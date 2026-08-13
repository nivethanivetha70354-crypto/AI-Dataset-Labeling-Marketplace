# Class / Module Diagram

## AI Dataset Labeling Marketplace

The system follows a modular Python FastAPI architecture with separate API,
model, schema, service, database, core, and utility modules.

## Main Module Architecture

```text
                    AI DATASET LABELING MARKETPLACE
                                  |
                 +----------------+----------------+
                 |                |                |
                 v                v                v
           AUTH MODULE      DATASET MODULE     TASK MODULE
                 |                |                |
           User / JWT        Dataset APIs       Task APIs
                 |                |                |
                 +----------------+----------------+
                                  |
                                  v
                         ANNOTATION MODULE
                                  |
                                  v
                           DATABASE MODULE
                                  |
                                  v
                         PostgreSQL Database
```

## Core Classes

### User

**Attributes**

* `user_id`
* `name`
* `email`
* `password`
* `role`

**Responsibilities**

* Register user
* Authenticate user
* Manage user information
* Identify user role

### Dataset

**Attributes**

* `dataset_id`
* `owner_id`
* `name`
* `description`
* `file_path`
* `status`

**Responsibilities**

* Create dataset
* Upload dataset
* View dataset
* Update dataset
* Manage dataset status

### Task

**Attributes**

* `task_id`
* `dataset_id`
* `assigned_to`
* `title`
* `status`
* `created_at`

**Responsibilities**

* Create labeling task
* Assign task to annotator
* Update task status
* Track task progress

### Label

**Attributes**

* `label_id`
* `name`
* `description`

**Responsibilities**

* Define available labels
* Store label information
* Manage label information

### Annotation

**Attributes**

* `annotation_id`
* `task_id`
* `label_id`
* `annotator_id`
* `value`
* `confidence`
* `status`

**Responsibilities**

* Create annotation
* Update annotation
* Store annotation confidence
* Submit annotation for review

## Service Modules

### Authentication Module

Responsibilities:

* User login
* Password verification
* JWT access-token generation
* Current-user identification
* Role-based authorization

### Dataset Module

Responsibilities:

* Dataset creation
* Dataset retrieval
* Dataset status management
* Dataset-related API operations

### Task Module

Responsibilities:

* Task creation
* Task retrieval
* Task assignment
* Task status management

### Annotation Module

Responsibilities:

* Annotation creation
* Annotation update
* Annotation validation
* Annotation submission

## Database / Model Relationships

```text
User
 |
 +---- owns -------> Dataset
 |
 +---- assigned to -> Task
 |
 +---- creates ----> Annotation

Dataset
 |
 +---- contains ---> Task

Task
 |
 +---- contains ---> Annotation

Label
 |
 +---- used by ----> Annotation
```

## Entity Relationships

* One User can own many Datasets.
* One Dataset can contain many Tasks.
* One User can be assigned many Tasks.
* One Task can contain many Annotations.
* One Label can be used by many Annotations.
* One User can create many Annotations.

## FastAPI Module Structure

```text
app/
├── main.py
│
├── api/
│   ├── auth.py
│   ├── datasets.py
│   ├── tasks.py
│   └── users.py
│
├── core/
│
├── database/
│   └── connection.py
│
├── models/
│   ├── user.py
│   ├── dataset.py
│   ├── task.py
│   └── ...
│
├── schemas/
│   ├── user.py
│   ├── dataset.py
│   ├── task.py
│   └── ...
│
├── services/
│
└── utils/
```

## Module Responsibilities

### `api/`

Contains FastAPI route modules and HTTP endpoints.

```text
auth.py       → Authentication and authorization
users.py      → User-related endpoints
datasets.py   → Dataset endpoints
tasks.py      → Task endpoints
```

### `models/`

Contains SQLAlchemy database models representing application entities.

### `schemas/`

Contains Pydantic request and response schemas used for API validation.

### `services/`

Contains reusable business-logic components.

### `database/`

Contains database connection and session management.

### `core/`

Contains application-level configuration and core functionality.

### `utils/`

Contains reusable utility functions such as password hashing and security
helpers.

## Request Flow

```text
React Frontend
      |
      | HTTP Request
      v
FastAPI API Module
      |
      v
Authentication / Authorization
      |
      v
Business Logic
      |
      v
SQLAlchemy Model
      |
      v
PostgreSQL Database
      |
      v
API Response
      |
      v
React Frontend
```

## Technology Mapping

| Component         | Technology       |
| ----------------- | ---------------- |
| Frontend          | React            |
| Backend           | Python / FastAPI |
| API Validation    | Pydantic         |
| ORM               | SQLAlchemy       |
| Database          | PostgreSQL       |
| Authentication    | OAuth2 / JWT     |
| Password Security | Argon2           |
| Version Control   | Git / GitHub     |
| Containerization  | Docker           |

## Goal of the Module Architecture

The architecture separates API routes, database models, schemas, business
logic, database connectivity, and utility functions.

This separation makes the application easier to develop, test, maintain,
debug, and extend.
