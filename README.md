# Redberry Blog API

## Overview

This project is a blog API developed with Django and Django REST Framework. It allows users to perform CRUD operations on blog posts, view categories, and handle user registration and login.

## Features

- List, create, and retrieve blog posts.
- List categories.
- User registration and login.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (optional but recommended for creating isolated Python environments)

### 1. Cloning the Repository

To clone the repository and navigate into the project directory, run:

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```


### 2. Setting Up a Virtual Environment (Optional but Recommended)
#### To create a virtual environment, run:

```
python -m venv venv
```
#### Activate the virtual environment:
- On Windows:
```
.\venv\Scripts\activate
```
- On macOS and Linux:
```
source venv/bin/activate
```
### 3. Installing Dependencies
#### Install the project dependencies:
```
pip install -r requirements.txt
```

### 4. Running the Server
#### Start the Django development server:
```
python manage.py runserver
```

The API will now be accessible at `http://127.0.0.1:8000/api/`

API Endpoints
You can perform the following operations with the API:

- GET `/api/blogs/`: Retrieve a list of all blog posts.
- POST `/api/blogs/create/`: Create a new blog post.
- GET `/api/blogs/<id>/`: Retrieve a specific blog post by its ID.
- GET `/api/categories/`: Retrieve a list of all categories.
- POST `/api/register/`: Register a new user.
- POST `/api/login/`: Log in an existing user.

## Testing with Postman
### You can test the API using Postman by following these steps:

1. Install and open Postman.
2. Create a new request and select the appropriate HTTP method (GET, POST, etc.).
3. Enter the request URL for the endpoint you want to test.
4. For POST requests:
- - In the Headers section, add Content-Type: application/json.
- - In the Body section, select raw and enter the required data in JSON format.
5. Send the request and observe the response.

Example for user registration:

- Method: POST
- URL: `http://127.0.0.1:8000/api/register/`
- Headers: `Content-Type: application/json`
- Body:
```
{
    "email": "user@redberry.ge",
    "username": "username"
}
```
1. Click `Send`

## Credits
### This project was created by George Toloraia
