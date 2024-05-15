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
<img width="1506" alt="Screenshot 2024-03-28 at 12 17 49 AM" src="https://github.com/YaChunT/student_management_system/assets/162515094/8edefba6-8586-4f4a-9039-5e42b29a35ee">
</div>

<br> <!-- Line break -->
<br> <!-- Line break -->
## Getting Started🏃‍♂️

Follow these steps to get the project up and running on your local machine.

### - Prerequisites

- Docker installed on your system

### - Run Database with Docker

1. Clone this repository:

    ```bash
    git clone https://github.com/YaChunT/student_management_system.git
    ```

2. Navigate into the project directory:

    ```bash
    cd student_management_system
    ```

3. Build the Docker image:

    ```bash
    docker-compose up --build
    ```

### - Run the Spring Boot Application
1. Build the project using Maven:
    ```bash
    ./mvnw clean package
    ```
2. Run the application:
    ```bash
    java -jar target/student_management_system-0.0.1-SNAPSHOT.jar
    ```
### - Access the application:

    Open http://localhost:8080 in your web browser.
   
