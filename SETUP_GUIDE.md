# Real Estate Platform - Quick Setup Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Windows 10/11 or Linux/Mac

## Step-by-Step Setup

### 1. Virtual Environment Setup
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.\.venv\Scripts\Activate.ps1

# Or for Linux/Mac:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Initialization
```bash
# Apply migrations
python manage.py migrate

# Create migrations for properties app
python manage.py makemigrations properties

# Apply app migrations
python manage.py migrate properties
```

### 4. Load Sample Data
```bash
# Populate database with 8 sample properties
python manage.py populate_properties
```

### 5. Create Admin User
```bash
# Create superuser for admin access
python manage.py createsuperuser

# Follow the prompts to create username, email, and password
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## Access Points

### Home Page
- URL: `http://127.0.0.1:8000/`
- View featured properties and search

### Admin Dashboard
- URL: `http://127.0.0.1:8000/admin/`
- Username/Password: (created in step 5)
- Manage properties, contacts, and users

### User Signup
- URL: `http://127.0.0.1:8000/signup/`

### User Login
- URL: `http://127.0.0.1:8000/login/`

### Properties Listing
- URL: `http://127.0.0.1:8000/properties/`

## Testing the Backend

### Test Signup
1. Go to `/signup/`
2. Enter: username, email, password, confirm password
3. Click "Sign Up"
4. Should redirect to login page with success message

### Test Login
1. Go to `/login/`
2. Enter: email (or username) and password
3. Click "Login"
4. Should redirect to home page with username in navbar

### Test Property Search
1. Go to `/properties/`
2. Enter search criteria (location, type, price range)
3. Click "Search"
4. Results should filter based on criteria

### Test Contact Form
1. Go to any property detail page (`/properties/<id>/`)
2. Scroll to "Interested in this property?" section
3. Fill in name, email, message
4. Click "Send Inquiry"
5. Check admin panel for the inquiry

## Database Management

### View Database Contents
```bash
# Access Django shell
python manage.py shell

# Example queries:
from properties.models import Property, Contact, UserProfile
Property.objects.all()
Contact.objects.all()
```

### Reset Database
```bash
# WARNING: This deletes all data!
python manage.py flush

# Then run migrations again:
python manage.py migrate
python manage.py populate_properties
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"
**Solution**: Ensure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: "Port 8000 already in use"
**Solution**: Use a different port
```bash
python manage.py runserver 8001
```

### Issue: "No such table: properties_property"
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Issue: CSRF token missing
**Solution**: Ensure you're using Django templates (not plain HTML)
- Templates must be in `/templates/` folder
- Must use `{% csrf_token %}` in forms
- Must use `{% load static %}` for static files

## Development Tips

### Hot Reload
- Django automatically reloads when files are saved
- CSS/JS changes require browser refresh

### Debug Mode
- `DEBUG = True` in settings.py (for development only)
- Shows detailed error pages

### Database Backup
```bash
# Export data
python manage.py dumpdata > backup.json

# Import data
python manage.py loaddata backup.json
```

## Production Deployment

### Before Production
1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a random value
3. Set `ALLOWED_HOSTS` to your domain
4. Use a production database (PostgreSQL recommended)
5. Use a production web server (Gunicorn, uWSGI)
6. Set up proper logging
7. Enable HTTPS
8. Collect static files: `python manage.py collectstatic`

### Deploy with Gunicorn
```bash
pip install gunicorn
gunicorn realestate.wsgi
```

## Support & Documentation

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Bootstrap Documentation: https://getbootstrap.com/docs/

---
**Setup Guide Version**: 1.0  
**Last Updated**: May 1, 2026
