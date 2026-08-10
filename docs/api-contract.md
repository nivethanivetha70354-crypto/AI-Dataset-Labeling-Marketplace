# API Contract

## AI Dataset Labeling Marketplace

The API connects the React frontend with the FastAPI backend.

## Base URL

```text
/api
```

## 1. User APIs

### Register User

```http
POST /api/users/register
```

Purpose:

New user account create panna.

Request:

```json
{
  "name": "User Name",
  "email": "user@example.com",
  "password": "password"
}
```

Response:

```json
{
  "user_id": 1,
  "name": "User Name",
  "email": "user@example.com",
  "role": "annotator"
}
```

### Login User

```http
POST /api/users/login
```

Purpose:

User login panna.

Request:

```json
{
  "email": "user@example.com",
  "password": "password"
}
```

Response:

```json
{
  "access_token": "token",
  "user_id": 1
}
```

---

## 2. Dataset APIs

### Upload Dataset

```http
POST /api/datasets
```

Purpose:

New dataset upload panna.

Request:

```text
multipart/form-data
file
name
description
```

Response:

```json
{
  "dataset_id": 1,
  "name": "Sample Dataset",
  "status": "uploaded"
}
```

### Get Datasets

```http
GET /api/datasets
```

Purpose:

Available datasets list panna.

Response:

```json
[
  {
    "dataset_id": 1,
    "name": "Sample Dataset",
    "status": "uploaded"
  }
]
```

### Get Dataset

```http
GET /api/datasets/{dataset_id}
```

Purpose:

Specific dataset details get panna.

---

## 3. Task APIs

### Create Task

```http
POST /api/tasks
```

Purpose:

Dataset-ku annotation task create panna.

Request:

```json
{
  "dataset_id": 1,
  "title": "Image Annotation Task",
  "assigned_to": 2
}
```

Response:

```json
{
  "task_id": 1,
  "dataset_id": 1,
  "title": "Image Annotation Task",
  "status": "assigned"
}
```

### Get Tasks

```http
GET /api/tasks
```

Purpose:

Annotation tasks list panna.

### Update Task

```http
PUT /api/tasks/{task_id}
```

Purpose:

Task status or task information update panna.

---

## 4. Annotation APIs

### Create Annotation

```http
POST /api/annotations
```

Purpose:

Dataset item-ku annotation create panna.

Request:

```json
{
  "task_id": 1,
  "label_id": 2,
  "value": "car"
}
```

Response:

```json
{
  "annotation_id": 1,
  "task_id": 1,
  "label_id": 2,
  "value": "car",
  "status": "pending"
}
```

### Update Annotation

```http
PUT /api/annotations/{annotation_id}
```

Purpose:

Human annotator annotation-a correct panna.

Request:

```json
{
  "value": "truck",
  "status": "verified"
}
```

---

## 5. AI Label Suggestion API

### Generate Label Suggestions

```http
POST /api/ai/suggestions
```

Purpose:

Uploaded dataset item-ai AI model process panni possible labels suggest panna.

Request:

```json
{
  "dataset_id": 1,
  "item_id": 10
}
```

Response:

```json
{
  "suggestions": [
    {
      "label": "car",
      "confidence": 0.92
    },
    {
      "label": "person",
      "confidence": 0.81
    }
  ]
}
```

---

## 6. Annotation Statistics API

### Get Annotation Statistics

```http
GET /api/statistics/annotations
```

Purpose:

Annotation progress and statistics display panna.

Response:

```json
{
  "total_annotations": 100,
  "verified_annotations": 80,
  "pending_annotations": 20,
  "accuracy_score": 92.5
}
```

---

## API Summary

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/users/register` | Register user |
| POST | `/api/users/login` | Login |
| POST | `/api/datasets` | Upload dataset |
| GET | `/api/datasets` | List datasets |
| GET | `/api/datasets/{dataset_id}` | Get dataset |
| POST | `/api/tasks` | Create task |
| GET | `/api/tasks` | List tasks |
| PUT | `/api/tasks/{task_id}` | Update task |
| POST | `/api/annotations` | Create annotation |
| PUT | `/api/annotations/{annotation_id}` | Update annotation |
| POST | `/api/ai/suggestions` | Get AI suggestions |
| GET | `/api/statistics/annotations` | Get statistics |

## API Flow

```text
React Frontend
      ↓
FastAPI Backend
      ↓
API Endpoint
      ↓
Database / AI Module
      ↓
Response
      ↓
React Frontend
```

## Human-in-the-Loop API Flow

```text
Dataset
   ↓
AI Suggestion API
   ↓
AI Label Suggestions
   ↓
Human Review
   ↓
Annotation API
   ↓
Verified / Corrected Annotation
   ↓
Database
```