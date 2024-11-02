# Resume Builder Using Django

A web application that helps users create professional resumes with ease using Django framework.

## Features

- User-friendly interface for creating and editing resumes
- Custom template tags for enhanced functionality
- Multiple resume templates to choose from
- Admin panel for managing user data and resumes
- SQLite database for storing user information and resume data

## Project Structure

```
Resume_Builder/
├── core/
│   └── _pycache_/
│   └── migrations/
│   └── templates/
│       └── static/
│       └── index.html
│       └── resume.html
├── templatetags/
│   └── _pycache_/
│   └── __init__.py
│   └── custom_filters.py
│   └── admin.py
│   └── apps.py
│   └── models.py
│   └── tests.py
│   └── urls.py
│   └── views.py
├── Resume_Builder/
│   └── _pycache_/
│   └── __init__.py
│   └── asgi.py
│   └── settings.py
│   └── urls.py
│   └── wsgi.py
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

## Prerequisites

- Python 3.x
- Django
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
```bash
git clone https://github.com/prathamesh-patil-5090/Resume_Builder_Using_Django.git
```

2. Navigate to the project directory:
```bash
cd Resume_Builder_Using_Django
```

3. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
```

4. Install required dependencies:
```bash
pip install -r requirements.txt
```

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application at `http://127.0.0.1:8000`

## Usage

1. Register/Login to your account
2. Choose a resume template
3. Fill in your personal information, education, experience, and skills
4. Preview your resume
5. Download or save your resume

## Project Components

- **core**: Main application containing the core functionality
- **templatetags**: Custom template tags and filters
- **templates**: HTML templates for the frontend
- **static**: CSS, JavaScript, and other static files
- **models.py**: Database models for user data and resumes
- **views.py**: View functions for handling requests
- **urls.py**: URL routing configuration
- **admin.py**: Admin panel configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Prathamesh Patil

## Acknowledgments

- Django Documentation
- Bootstrap for frontend styling
- Contributors and community members

## Support

For support, email [prathampatil7798@gmail.com] or create an issue in the repository.
