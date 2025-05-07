# Django To-Do App

A simple yet powerful To-Do list application built with **Django**, designed to manage tasks with various features like **task creation**, **editing**, **deleting**, **marking tasks as completed**, and more.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)


---

## About

This To-Do application allows users to register, log in, and manage their tasks. Users can add new tasks, mark tasks as completed or pending, and delete tasks as needed. The app is built with Django, which offers a robust and secure backend.

---

## Features
- **User Authentication:** Register, login, and logout functionalities.
- **Task Management:** Add, edit, and delete tasks.
- **Task Completion:** Mark tasks as "Completed" or "Pending".
- **Task Sorting:** Tasks are displayed by creation date.
- **User-Specific Data:** Tasks are tied to the authenticated user, so each user only sees their own tasks.
- **Responsive Design:** Optimized UI for both desktop and mobile.

---

## Screenshots

#### Login Page
![Login Page](https://via.placeholder.com/800x400.png?text=Login+Page)

#### Task List
![Task List](https://via.placeholder.com/800x400.png?text=Task+List)

#### Add Task Page
![Add Task](https://via.placeholder.com/800x400.png?text=Add+Task+Page)

*Note: Replace the placeholder links with your actual project screenshots.*

---

## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Usage

- **Register**: Create a new account.
- **Login**: Access your tasks after logging in.
- **Add a Task**: Click on "Add Task" to create a new task.
- **Complete or Pending**: Mark tasks as completed or pending.
- **Delete Task**: Remove tasks when no longer needed.

## Technologies Used

- **Django** - A Python web framework used for backend development.
- **SQLite** - A lightweight database engine used for storage (can be switched to PostgreSQL/MySQL).
- **HTML/CSS** - For front-end development and styling.
- **Bootstrap** - (Optional) For responsive layout.
- **Git** - For version control



