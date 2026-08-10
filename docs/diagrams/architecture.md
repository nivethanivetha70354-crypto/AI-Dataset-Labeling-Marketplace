# System Architecture

## AI Dataset Labeling Marketplace

The system is divided into different components so that each part has a clear responsibility.

## Architecture Flow

```text
                    ┌──────────────────────┐
                    │        User          │
                    │ Dataset Owner /      │
                    │ Annotator            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    React Frontend    │
                    │                      │
                    │ Dataset Upload       │
                    │ Annotation Interface │
                    │ Task Management      │
                    │ Statistics           │
                    └──────────┬───────────┘
                               │
                            REST API
                               │
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │                      │
                    │ Authentication       │
                    │ Dataset Management   │
                    │ Task Management      │
                    │ Annotation Management│
                    │ API Services         │
                    └───────┬───────┬──────┘
                            │       │
                            ▼       ▼
                  ┌─────────────┐  ┌──────────────┐
                  │ PostgreSQL  │  │   AI / ML    │
                  │  Database   │  │    Module    │
                  │             │  │              │
                  │ Users       │  │ Auto-label   │
                  │ Datasets    │  │ Suggestions  │
                  │ Tasks       │  │ Prediction   │
                  │ Labels      │  │ Processing   │
                  │ Annotations │  │              │
                  └─────────────┘  └──────┬───────┘
                                          │
                                          ▼
                                  ┌────────────────┐
                                  │ Human Review   │
                                  │                │
                                  │ Verify Labels  │
                                  │ Correct Labels │
                                  └───────┬────────┘
                                          │
                                          ▼
                                  ┌────────────────┐
                                  │ Final Labels   │
                                  │ / Annotations  │
                                  └────────────────┘
```

## Main Components

### 1. Frontend

The frontend is the part that users interact with.

It will provide:

- User registration and login
- Dataset upload
- Dataset viewing
- Annotation interface
- AI label suggestions
- Human label correction
- Task management
- Annotation statistics

### 2. Backend

The backend manages the main application logic and connects the frontend with the database and AI/ML module.

It will handle:

- User authentication
- Dataset management
- Task management
- Annotation management
- Label management
- API requests
- Communication with the AI/ML module
- Database operations

### 3. PostgreSQL Database

The database stores the application's structured information.

It will store:

- Users
- Datasets
- Tasks
- Labels
- Annotations
- Annotation statistics

### 4. AI / ML Module

The AI/ML module provides automatic labeling suggestions.

Its main responsibilities are:

- Process uploaded data
- Analyze images or text
- Generate possible labels
- Provide label suggestions
- Send predictions to the backend

### 5. Human Verification

Human annotators check the AI-generated suggestions.

They can:

- Accept a correct label
- Correct an incorrect label
- Add a missing label
- Confirm the final annotation

This creates a human-in-the-loop workflow.

## Main Data Flow

```text
Dataset Upload
      ↓
Frontend
      ↓
Backend
      ↓
Dataset Storage
      ↓
AI / ML Processing
      ↓
AI Label Suggestions
      ↓
Human Verification
      ↓
Correction if Required
      ↓
Final Annotation
      ↓
Database
```

## Human-in-the-Loop Workflow

```text
Dataset
   ↓
AI Prediction
   ↓
Label Suggestion
   ↓
Human Review
   ↓
 ┌───────────────┐
 │ Correct?      │
 └───────┬───────┘
         │
    ┌────┴────┐
    │         │
   Yes        No
    │         │
    │    Human Correction
    │         │
    └────┬────┘
         ↓
   Final Annotation
         ↓
      Database
```

## Technology Mapping

| Component | Technology |
|---|---|
| Frontend | React |
| Backend | Python / FastAPI |
| Database | PostgreSQL |
| AI / ML | Python, OpenCV, YOLO, NLP models |
| Version Control | Git / GitHub |
| Containerization | Docker |

## Goal of the Architecture

The architecture is designed to keep the frontend, backend, database, and AI/ML components separate.

This makes the system easier to develop, test, maintain, and improve.