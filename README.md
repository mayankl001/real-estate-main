# Real Estate Website

A full-stack real estate website built with HTML, CSS, Bootstrap, and Django backend.

## Features

- Responsive design
- Property search functionality
- Contact form
- User login system
- Professional UI inspired by Magicbricks

## Backend Setup

This project now includes a Django backend.

### Installation

1. Make sure you have Python installed (version 3.8 or higher)
2. Configure Python environment (virtualenv created)
3. Install Django:
   ```bash
   pip install django
   ```

### Running the Server

Start the Django development server:
```bash
python manage.py runserver
```

The server will run on http://127.0.0.1:8000

### Backend Routes

- `GET /` - Home page
- `GET /contact/` - Contact page
- `GET /login/` - Login page
- `POST /contact/` - Handle contact form submission
- `POST /login/` - Handle login with Django auth

### Forms

- Contact form posts to `/contact/` and shows success messages
- Login form posts to `/login/` with Django authentication

## File Structure

- `index.html` - Main homepage
- `contact.html` - Contact page
- `LOGIN.HTML` - Login page
- `manage.py` - Django management script
- `realestate/` - Django project settings
- `properties/` - Django app
- `style.css` - Main styles
- `css/` - Additional stylesheets
- `images/` - Image assets

## Development

To add more backend functionality:
- Database models for properties and users
- User registration/authentication
- Property CRUD operations
- Email sending for contact forms

## Technologies Used

- Frontend: HTML, CSS, Bootstrap, FontAwesome
- Backend: Django, SQLite
- Icons: Bootstrap Icons, FontAwesome

## File Structure

- `index.html` - Main homepage
- `contact.html` - Contact page
- `LOGIN.HTML` - Login page
- `server.js` - Express server
- `package.json` - Dependencies
- `style.css` - Main styles
- `css/` - Additional stylesheets
- `images/` - Image assets

## Development

To add more backend functionality:
- Database integration (MongoDB, PostgreSQL)
- User registration/authentication
- Property CRUD operations
- Email sending for contact forms

## Technologies Used

- Frontend: HTML, CSS, Bootstrap, FontAwesome
- Backend: Node.js, Express
- Icons: Bootstrap Icons, FontAwesome