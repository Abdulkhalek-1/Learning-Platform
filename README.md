# Learning Platform

## Description

The Learning Platform is an advanced online education system designed to revolutionize the way students learn and instructors teach. It offers a comprehensive suite of features to enhance the learning experience, foster collaboration, and promote interactive learning environments.

### Key Features

- **Courses:** Explore a vast collection of courses spanning various disciplines and skill levels, curated by industry experts and educators.
- **Interactive Lessons:** Immerse yourself in interactive lessons with multimedia content, real-time collaboration tools, and personalized learning paths.
- **Quizzes and Assessments:** Assess your knowledge and skills through dynamic quizzes, assessments, and real-world projects to gauge understanding and progress.
- **Discussion Forums:** Engage in vibrant discussion forums to ask questions, share insights, and collaborate with a global community of learners and mentors.
- **Progress Monitoring:** Monitor your learning journey with detailed progress tracking, performance analytics, and personalized recommendations for continuous improvement.
- **User Roles and Permissions:** Customize user roles and permissions for administrators, instructors, students, and mentors to streamline workflows and manage access effectively.

### Technologies Used

- [x] Django: Robust backend framework for building scalable, secure, and high-performance web applications.
- [x] PostgreSQL: Advanced relational database management system for efficient data storage and retrieval.
- [x] Docker Compose: Container orchestration tool for seamless development, testing, and deployment workflows.
- [x] HTML/CSS/JavaScript: Frontend technologies for responsive, intuitive, and engaging user interfaces.
- [x] Django REST Framework: Powerful API framework for creating RESTful APIs to interact with the platform programmatically.
- [x] Strawberry GraphQL: Modern GraphQL implementation for flexible and efficient data querying and manipulation.
- [x] Django Channels: Real-time communication channels for interactive features, live updates, and notifications.
- [x] Tailwind CSS: Utility-first CSS framework for designing modern, customizable, and accessible user interfaces.

## Getting Started

### Prerequisites

Before getting started, ensure you have the following installed on your system:

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abdulkhalek-1/Learning-Platform.git
   cd Learning-Platform
   ```

2. Create a `.env` folder based on `.env-template` and update the environment variables as needed.

3. Build and start the containers using Docker Compose:
   ```bash
   docker-compose build
   ```

### Configuration

- Modify the `secrets.dev.env` and `secrets.prod.env` file to set environment variables such as `SECRET_KEY`, `DEBUG`, etc.
- Customize Docker Compose configurations in `docker-compose.yml` for development, staging, and production environments.

### Creating a Superuser

To access the Django admin interface and manage the platform, follow these steps to create a superuser:

1. Open a new terminal window.
2. Navigate to the project directory.
3. Run the following command to enter the Django container:
   ```bash
   docker-compose exec django bash
   ```

4. Inside the container, run the following command to create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Follow the prompts to enter the superuser's username, email, and password.

6. Exit the container by typing `exit`.
## Usage

1. Start the containers:
   ```bash
   docker-compose up
   ```

2. Access the Learning Platform at http://localhost:8000/ and start exploring courses, lessons, quizzes, and forums.

## Project Structure

- `Dockerfile`: Defines instructions for building the Docker image for the Django application.
- `docker-compose.yml`: Orchestrates Docker containers for the Django app, PostgreSQL database, and other services.
- `start.sh`: Script to initialize and manage the Django application within Docker containers.
- `.env`: Configuration file for environment variables (ignored by version control) for local development settings.
- `src/`: Directory containing the Django project source code.
- `LICENSE`: License file specifying the terms of use and distribution for the project.
- `README.md`: Main README file providing an overview of the project, setup instructions, and usage guidelines.
