# Real-Time Chat Application

## Overview

- **Project Name**: Real-Time Chat Application
- **Description**: A real-time chat system developed using Flask and Flask-SocketIO.
- **Authors**: [Abdulrhman Adel](https://github.com/abdulrhman-adel) & [Abdulrhman Zakaria]()
- **GitHub Repository**: https://github.com/abdulrhman-adel/Real-Time-Chat


## Installation

- Clone the repository from GitHub: `https://github.com/abdulrhman-adel/Real-Time-Chat` 
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
- Install project dependencies: `pip install -r requirements.txt`
- Copy and rename the `.env.example` file to `.env` to configure your application.

## Configuration

- Configuration settings are stored in the `.env` file using the `python-dotenv` library. You can customize settings such as the secret key, debug mode, and more in the `.env` file.

## Usage

1. Run the application:

    ```bash
    python run.py
    ```

2. Access the application in your web browser at `http://127.0.0.1:5000` (or a different URL as specified).

## Features

- Real-time chat functionality.
- User authentication and registration.
- and more ... 

## Code Structure

- **`app`**: The core of the application.
    - **`__init__.py`**: Initializes the Flask application and configures it.
    - **`config.py`**: Manages configuration settings using `python-dotenv`.
    - **`routes.py`**: Contains route definitions.


- **`app/templates`**: Contains HTML files for rendering the chat interface and user-related pages.

- **`app/static`**: Stores static assets such as CSS and JavaScript files.

- **`run.py`**: The entry point of the application. Run this script to start the server.

