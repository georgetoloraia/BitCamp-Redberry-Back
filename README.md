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

`git clone https://github.com/yourusername/your-repository.git`
`cd BitCamp-Redberry-Back`


2. Setting Up a Virtual Environment (Optional but Recommended)
To create a virtual environment, run:

bash
Copy code
virtualenv venv
Activate the virtual environment:

On Windows, run:

bash
Copy code
.\venv\Scripts\activate
On macOS and Linux, run:

bash
Copy code
source venv/bin/activate
3. Installing Dependencies
Install the required packages using pip:

bash
Copy code
pip install -r requirements.txt
4. Running the Server
To run the server, execute:

bash
Copy code
python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

API Endpoints
The following endpoints are available:

GET /api/blogs/: List all blogs.
POST /api/blogs/create/: Create a new blog.
GET /api/blogs/<id>/: Retrieve a blog by ID.
GET /api/categories/: List all categories.
POST /api/register/: Register a new user.
POST /api/login/: Login a user.
Testing with Postman
To test the API endpoints with Postman:

Open Postman.
Choose the HTTP method (GET, POST).
Enter the request URL.
For POST requests, set the header Content-Type to application/json and include the request body as raw JSON.
Send the request and observe the response.
For example, to test user registration:

Set the method to POST.

Enter the URL http://127.0.0.1:8000/api/register/.

In the Headers section, add Content-Type application/json`.

In the Body section, choose raw and enter the user details in JSON format:

json
Copy code
{
"email": "user@redberry.ge",
"username": "username"
}
Click Send.

Credits
Created by George Toloraia.

License
MIT

vbnet
Copy code

### Notes:

- **Repository URL**:  `https://github.com/georgetoloraia/BitCamp-Redberry-Back`
- **Dependency Installation**: If you have a `requirements.txt` file in your repository, the command `pip install -r requirements.txt` will install all the required packages. Ensure this file exists and is properly populated.
- **Virtual Environment**: It's a best practice to use a virtual environment, but if your setup doesn't involve one, you can omit that section.
- **Endpoints**: Update the endpoint paths and descriptions based on your actual API.
- **Testing Instructions**: Adjust the testing instructions based on your actual API endpoints and data requirements.
- **License**: I've included a link to the MIT license as a placeholder. Ensure you use a license that suits your project.

Feel free to customize the content to match your project's specifics and personal style.
