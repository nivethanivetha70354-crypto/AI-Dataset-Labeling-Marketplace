# ER Diagram

## AI Dataset Labeling Marketplace

The main database entities are Users, Datasets, Tasks, Labels, and Annotations.

## Entities and Relationships

```text
USERS
-----
PK user_id
name
email
password
role
   |
   | uploads
   v
DATASETS
--------
PK dataset_id
FK owner_id
name
description
file_path
status
   |
   | contains
   v
TASKS
-----
PK task_id
FK dataset_id
FK assigned_to
title
status
created_at
   |
   | has
   v
ANNOTATIONS
-----------
PK annotation_id
FK task_id
FK label_id
FK annotator_id
value
confidence
status
   |
   | uses
   v
LABELS
------
PK label_id
name
description
```

## Relationships

- One User can upload many Datasets.
- One Dataset can contain many Tasks.
- One User can be assigned to many Tasks.
- One Task can have many Annotations.
- One Label can be used in many Annotations.
- One User can create many Annotations.

## Primary Keys

- `user_id` -> Users
- `dataset_id` -> Datasets
- `task_id` -> Tasks
- `annotation_id` -> Annotations
- `label_id` -> Labels

## Foreign Keys

- `owner_id` -> Users
- `dataset_id` -> Datasets
- `assigned_to` -> Users
- `task_id` -> Tasks
- `label_id` -> Labels
- `annotator_id` -> Users