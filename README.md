# Django Tweet App

This is a simple Tweet App built using Django. The app allows users to post tweets and view tweets from other users. This README will guide you through setting up the project locally.

## Features

- User registration and authentication
- Posting tweets
- Viewing tweets from all users

## Prerequisites

- Python 3.x
- Git
- Virtualenv

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### 1. Clone the Repository

First, clone the repository to your local machine using Git.

```bash
git clone https://github.com/yourusername/django-tweet-app.git
cd django-tweet-app
```
### 2. Create a Virtual Environment

Create a virtual environment to install the project's dependencies. This is recommended to avoid conflicts with other projects.

```bash
Copy code
python3 -m venv venv
```
Activate the virtual environment:

On Windows:

```bash
Copy code
venv\Scripts\activate
```
On macOS and Linux:
```
bash
Copy code
source venv/bin/activate
```
### 3. Install Dependencies

Install the necessary dependencies using `pip`.
```
bash
Copy code
pip install -r requirements.txt
```
### 4. Apply Migrations
Apply the database migrations to set up the database schema.
```
bash
Copy code
python manage.py migrate
```
### 5. Run the Development Server
Start the Django development server.
```
bash
Copy code
python manage.py runserver
```
Open your web browser and navigate to http://127.0.0.1:8000/ to see the app in action.
