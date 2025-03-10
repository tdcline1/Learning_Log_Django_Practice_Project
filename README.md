# Learning Log

**Learning Log** is a Django web application built from scratch that allows users to track topics they're interested in and create journal entries as they learn about each topic. The app features user registration and authentication, ensuring that each user can access and manage their own data.

## Features

- **User Management**
  - User registration, login, and logout using Django’s built-in forms (e.g., `UserCreationForm`).
  - Ownership of topics and entries enforced via foreign keys.
  - Access restrictions using decorators and ownership checks.

- **Topic & Entry Management**
  - Users can create, edit, and view topics.
  - Journal entries for each topic can be added and updated.
  - Admin site configured for initial data entry and management.

- **Responsive Design**
  - Consistent, responsive, and professional theme across all pages using Bootstrap.

- **Data Persistence**
  - PostgreSQL setup for robust, production-ready data storage.

- **Deployment & Version Control**
  - Version controlled using Git.
  - Deployed to Platform.sh with production settings (`DEBUG=False`) and custom 404/500 error pages.

## My Contributions

- **Project Setup & Development**
  - Built the project from scratch: created a virtual environment, installed dependencies, and set up the Django project.
  - Defined models for topics and entries, and configured the database.
  - Created the `learning_log` app.

- **User & Content Management**
  - Developed URL patterns, view functions, and templates using Django’s template inheritance.
  - Utilized the Django shell for testing and refining view logic.
  - Implemented Django forms to allow users to add and edit topics and entries.
  - Created new app components and pages for user accounts (login, logout, and registration).

- **Security & Access Control**
  - Assigned ownership of entries via foreign keys to the current user.
  - Restricted access using decorators and entry ownership checks.

- **Design & Deployment**
  - Applied a consistent, responsive Bootstrap theme across the application.
  - Configured PostgreSQL for production.
  - Managed version control with Git.
  - Deployed the application to Platform.sh with production settings and custom error pages.

## Getting Started

To run the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tdcline1/Learning_Log_Django_Practice_Project.git
   cd Learning_Log_Django_Practice_Project

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv ll_env
   source ll_env/bin/activate

3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Run the development server:
  ```bash
  python manage.py runserver
  ```

5. Access the application by opening your browser and navigating to:
  ```cpp
  http://127.0.0.1:8000/
  ```

Enjoy exploring the Learning Log application!
