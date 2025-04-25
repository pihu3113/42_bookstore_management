# Bookstore Management System

A full-featured bookstore management system built with Django that includes user authentication, an admin panel for managing book inventory, and a shopping cart functionality.

## Features

- **Authentication**
  - User Registration
  - User Login/Logout
  - User Profiles

- **Admin Panel**
  - Add/Edit/Delete Books
  - Manage Book Inventory

- **User Features**
  - View Books with Ratings
  - Book Details
  - Shopping Cart (Session-based)

## Technical Specifications

- Built with Django
- MySQL Database
- Class-Based Views (CBV) throughout
- Custom admin interface (not using Django Admin)
- Manual HTML forms with custom validation
- Session-based shopping cart
- Dockerized environment with docker-compose
- CI/CD with Jenkins pipeline

## Installation

### Prerequisites

- Python 3.9+
- MySQL Server
- Docker and Docker Compose (optional)

### Local Development Setup

1. Clone the repository
   ```
   git clone https://github.com/your-username/bookstore.git
   cd bookstore
   ```

2. Create a virtual environment/ not necessary but recommended
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Configure MySQL Database
   - Create a database named 'bookstore_2'
   - Update settings.py if needed with your MySQL credentials

5. Run migrations
   ```
   python manage.py migrate
   ```

6. Create sample books
   ```
   python manage.py create_sample_books
   ```

7. Run the development server
   ```
   python manage.py runserver
   ```

8. Access the application at http://localhost:8000

### Docker Setup

1. Ensure Docker and Docker Compose are installed on your system

2. Build and run the Docker containers
   ```
   docker-compose up -d --build
   ```

3. The MySQL database will be created automatically with the name 'bookstore_2'

4. Create sample books in the container //only if books not visible
   ```
   docker-compose exec web python manage.py create_sample_books
   ```

5. Access the application at http://localhost:8000

## Quick Troubleshooting

If books aren't showing up on the home page:

1. Verify the database connection:
   ```
   python check_books.py
   ```

2. Check if migrations were applied:
   ```
   python manage.py showmigrations
   ```

3. Create sample books:
   ```
   python manage.py create_sample_books
   ```

## Admin Access

By default, you will need to create a superuser to access admin features:
```
python manage.py createsuperuser
```

## CI/CD Pipeline

The project includes a Jenkinsfile that configures a CI/CD pipeline with the following stages:
- Build
- Test
- Deploy (when on the main branch)

## License

This project is licensed under the MIT License. 