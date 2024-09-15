# Task Manager Backend

## Overview

This is the backend for a task manager application built with Django and Django REST Framework. It supports user authentication and task management features with JWT for secure access.

## Features

- User registration and login
- Task creation, retrieval, updating, and deletion
- Filter tasks by status and search by title
- JWT authentication for secure access

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jasirck/Task-Manager-Technaureus-M-T-Backend.git
   cd Task-Manager-Technaureus-M-T-Backend

2.
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3.
   pip install -r requirements.txt

4.
   python manage.py makemigrations
   python manage.py migrate

5.
   python manage.py runserver


