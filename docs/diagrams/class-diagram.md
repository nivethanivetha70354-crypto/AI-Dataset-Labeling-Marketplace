# Class / Module Diagram

## AI Dataset Labeling Marketplace

The system follows a modular Python FastAPI architecture.

## Main Modules

```text
                         AI DATASET LABELING MARKETPLACE
                                      |
              +-----------------------+-----------------------+
              |                       |                       |
              v                       v                       v
        AUTH MODULE            DATASET MODULE            TASK MODULE
              |                       |                       |
        User / Auth              Dataset / Label        Task / Assignment
              |                       |                       |
              +-----------------------+-----------------------+
                                      |
                                      v
                              ANNOTATION MODULE
                                      |
                                      v
                               Annotation / Label
                                      |
                                      v
                              DATABASE MODULE
                                      |
                                      v
                              PostgreSQL Database
```

## Core Classes

### User

Attributes:
- user_id
- name
- email
- password
- role

Responsibilities:
- Register user
- Authenticate user
- Manage user profile
- Identify user role

### Dataset

Attributes:
- dataset_id
- owner_id
- name
- description
- file_path
- status

Responsibilities:
- Create dataset
- Upload dataset
- Update dataset
- Manage dataset status

### Task

Attributes:
- task_id
- dataset_id
- assigned_to
- title
- status
- created_at

Responsibilities:
- Create labeling task
- Assign task to annotator
- Update task status
- Track task progress

### Label

Attributes:
- label_id
- name
- description

Responsibilities:
- Define available labels
- Manage label information

### Annotation

Attributes:
- annotation_id
- task_id
- label_id
- annotator_id
- value
- confidence
- status

Responsibilities:
- Create annotation
- Update annotation
- Store annotation confidence
- Submit annotation for review

## Service Modules

### AuthService
- User registration
- User login
- JWT authentication
- Role validation

### DatasetService
- Dataset creation
- Dataset upload
- Dataset retrieval
- Dataset status management

### TaskService
- Task creation
- Task assignment
- Task status management
- Task progress tracking

### AnnotationService
- Annotation creation
- Annotation update
- Annotation validation
- Annotation submission

## Repository Modules

### UserRepository
- User database operations

### DatasetRepository
- Dataset database operations

### TaskRepository
- Task database operations

### LabelRepository
- Label database operations

### AnnotationRepository
- Annotation database operations

## Relationships

- User owns many Datasets.
- Dataset contains many Tasks.
- User can be assigned many Tasks.
- Task contains many Annotations.
- Label is used by many Annotations.
- User can create many Annotations.

## FastAPI Module Structure

```text
app/
├── main.py
├── api/
│   ├── auth.py
│   ├── datasets.py
│   ├── tasks.py
│   └── annotations.py
├── models/
│   ├── user.py
│   ├── dataset.py
│   ├── task.py
│   ├── label.py
│   └── annotation.py
├── schemas/
│   ├── user.py
│   ├── dataset.py
│   ├── task.py
│   └── annotation.py
├── services/
│   ├── auth_service.py
│   ├── dataset_service.py
│   ├── task_service.py
│   └── annotation_service.py
├── repositories/
│   ├── user_repository.py
│   ├── dataset_repository.py
│   ├── task_repository.py
│   ├── label_repository.py
│   └── annotation_repository.py
└── database/
    └── connection.py
```