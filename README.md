# Videoflow

A lightweight Django-based video streaming platform inspired by modern video sharing apps.

## Features included in this milestone
- Django project setup with modular app structure
- Custom user authentication and profile management
- Channel and subscription models
- Upload workflow for videos with metadata and tags
- Search and home page listing
- Video detail page and comments UI
- Responsive dark theme frontend
- Docker support and environment template

## Quick start

### 1. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
```

### 3. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser
```bash
python manage.py createsuperuser
```

### 5. Start the development server
```bash
python manage.py runserver
```

### 6. Open the app
- Homepage: http://localhost:8000/
- Login: http://localhost:8000/accounts/login/
- Signup: http://localhost:8000/accounts/signup/

## Docker
```bash
docker compose up --build
```

## Notes
This is the first working milestone. It supports a functional minimum viable product with core user, channel, upload, and browsing flow. FFmpeg/HLS streaming and advanced processing will be implemented in later milestones.
