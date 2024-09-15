# Task Manager Backend

## Overview

This is the backend for a task manager application built with Django and Django REST Framework. It supports user authentication and task management features with JWT for secure access.

## Features

- User registration and login
- User-task association: Each user can access their own tasks.
- Task management: Creation, retrieval, updating, and deletion of tasks.
- Task filtering and search: Filter tasks by status and search by title.
- JWT authentication: Secure access using JSON Web Tokens.


## Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jasirck/Task-Manager-Technaureus-M-T-Backend.git
   cd Task-Manager-Technaureus-M-T-Backend


2. Activate virtual environments:
    ```bash 
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   
4. Install requirements :

   ```bash
   pip install -r requirements.txt

5. Creating makemigration files and apply makemigration files
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate

6. Activate Server
   ```bash
   python3 manage.py runserver
