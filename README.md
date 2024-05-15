# Django PictaGram

PictaGram is a Django-based social media platform featuring Two-Factor Authentication (2FA) for enhanced security. The project leverages Python, CSS, JavaScript, and HTML to create a robust and user-friendly experience.

<div align="center">
  <img width="1024" alt="Screenshot 2024-05-14 at 11 18 52 PM" src="https://github.com/YaChunT/PictaGram/assets/162515094/3785b32d-b193-4bf5-b433-5221858f9887">
</div>



## Table of Contents
- [About](#about)
- [Architecture Diagram](#architecture-diagram-%EF%B8%8F)
- [User Interface](#user-interface-)
- [Getting Started](#getting-started%EF%B8%8F)




<br> <!-- Line break -->
<br> <!-- Line break -->
## About📌  
PictaGram ensures that users can secure their accounts with multiple layers of protection, making it a secure choice for social media interactions. Here are the key details:

<br> <!-- Line break -->
<br> <!-- Line break -->
## Architecture Diagram 🏗️

<div align="center">
  <img width="1024" alt="Screenshot 2024-05-15 at 5 34 31 PM" src="https://github.com/YaChunT/PictaGram/assets/162515094/d9672f61-8f3c-4616-a147-dddb13f11911">
</div>

<br> <!-- Line break -->


PictaGram is a secure social media platform built with Django, featuring advanced Two-Factor Authentication (2FA) and multiple authentication methods inspired by Google's Two-Step Authentication.
<br> <!-- Line break -->

## Key Features

- **Two-Factor Authentication (2FA)**: 
  Built using the django-otp framework and Django's built-in authentication system (django.contrib.auth), PictaGram offers seamless integration of 2FA into Django projects.
  <br>

- **Multiple Authentication Methods**: 
  Inspired by Google's Two-Step Authentication, PictaGram allows users to authenticate via:
  - Phone call
  - Text message (SMS)
  - Token generator apps like Google Authenticator
  - Optional YubiKey hardware token generator
  <br>

PictaGram ensures that users can secure their accounts with multiple layers of protection, making it a secure choice for social media interactions.
<br>

<br> <!-- Line break -->
<br> <!-- Line break -->
## User Interface 📊 
- **Sign-in page for web application**
<div align="center">
<img width="1024" alt="Screenshot 2024-05-15 at 5 53 04 PM" src="https://github.com/YaChunT/PictaGram/assets/162515094/eee0b2d1-7a10-4728-82ba-93713dcda2f0">
</div>
- **Home page for web application**
<div align="center">
<img width="1024" alt="Screenshot 2024-05-15 at 5 54 22 PM" src="https://github.com/YaChunT/PictaGram/assets/162515094/2acce733-b88b-46e4-ba0a-db35906296e6">
</div>


<br> <!-- Line break -->
<br> <!-- Line break -->
## Getting Started🏃‍♂️

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.8+
- pip (Python package installer)
- virtualenv (for creating virtual environments)


### Installation
1. **Clone the Repository**

```bash
git clone https://github.com/YaChunT/PictaGram.git
```

2. **Navigate into the project directory**

    ```bash
    cd "Social Book"
    cd social_book
    ```

3. **(Optional) Create and Activate a Virtual Environment**

    It's recommended to use a virtual environment to manage dependencies:

    - Create a virtual environment:
        ```bash
        python3 -m venv venv
        ```

    - Activate the virtual environment:
        - On Windows:
            ```bash
            venv\Scripts\activate
            ```
        - On macOS/Linux:
            ```bash
            source venv/bin/activate
            ```
4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up the Database**

    Apply migrations to set up the database schema:

    ```bash
    python3 manage.py migrate
    ```
6. **Create a Superuser**

    Create a superuser to access the Django admin interface:

    ```bash
    python3 manage.py createsuperuser
    ```

    Follow the prompts to create your admin user with your own chosen username and password.

7. **(Optional) Collect Static Files**

    This step is typically necessary for production environments, but you can also run it during development to test the static file collection process:

    ```bash
    python3 manage.py collectstatic
    ```

8. **Run the Development Server**

    Start the Django development server:

    ```bash
    python3 manage.py runserver
    ```

    Your application should now be running at `http://127.0.0.1:8000/`.

### Running Tests

To run tests for the application, use the following command:

```bash
python3 manage.py test
   
