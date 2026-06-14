# Real Estate Platform - Backend Documentation

## Overview
This is a fully-functional Django-based Real Estate platform backend that provides property management, user authentication, and property search capabilities.

## ✅ Completed Features

### 1. **Database Models**
- **Property Model**: Stores property listings with details including:
  - Title, Description, Price, Location
  - Property Type (Apartment, House, Villa, Plot, Office)
  - Bedrooms, Bathrooms, Area (sqft)
  - Image uploads, Creation/Update timestamps
  - Active/Inactive status

- **Contact Model**: Manages user inquiries with:
  - Name, Email, Message
  - Timestamps and Read status
  - Admin-only creation (prevents duplicate submissions)

- **UserProfile Model**: Extended user information:
  - One-to-One relationship with Django User
  - Phone, Address, City information
  - Timestamp tracking

### 2. **User Authentication**
- **Signup**: 
  - Username, Email, Password validation
  - Password strength requirements (min 6 characters)
  - Duplicate username/email detection
  - Automatic UserProfile creation
  - Password confirmation validation

- **Login**:
  - Email or username authentication
  - Secure password verification
  - Session management
  - Redirect to home after successful login

- **Logout**: Secure session termination

### 3. **Property Management**
- **Property List**: Browse all active properties with:
  - Grid layout display (3 columns)
  - Property cards showing images, price, location, features
  - Responsive design for mobile/tablet/desktop

- **Property Search & Filter**:
  - Filter by location (text search)
  - Filter by property type
  - Filter by price range (min/max budget)
  - Combined filter support
  - Real-time search results

- **Property Details**:
  - Full property information display
  - Property features (bedrooms, bathrooms, area, type)
  - Description and location
  - Contact agent form (integrated contact system)
  - Related/Similar properties display

### 4. **Contact Management**
- Contact form on property detail pages
- All inquiries stored in database
- Admin panel for managing inquiries
- Read/Unread status tracking

### 5. **Admin Interface**
Complete Django admin panel with:
- **Property Admin**:
  - Add/Edit/Delete properties
  - Filter by type, status, date
  - Search by title, location, description
  - Organized fieldsets for easy management
  - Read-only timestamps

- **Contact Admin**:
  - View all user inquiries
  - Filter by read status
  - Read-only (prevents deletion of submissions)
  - Search by name, email, message

- **UserProfile Admin**:
  - Manage user profiles
  - View user information
  - Search by username, email, phone

### 6. **URL Routing**
Complete URL configuration:
```
/ → Home page with featured properties
/signup/ → User registration
/login/ → User login
/logout/ → User logout
/contact/ → Contact page
/properties/ → All properties with search
/properties/<id>/ → Property details
/about/ → About page
/search/ → Search results redirect
/admin/ → Django admin panel
```

### 7. **Templates**
- **index.html**: Home page with featured properties and search
- **signup.html**: User registration form with validation
- **login.html**: User authentication form
- **contact.html**: Contact form for inquiries
- **properties.html**: Property listing with search filters
- **view-property.html**: Property detail page with inquiry form
- **about.html**: About the platform page

### 8. **Security Features**
- CSRF token protection on all forms
- Password hashing with Django's built-in system
- SQL injection protection via ORM
- Authentication required for user-specific pages
- Session-based user management

### 9. **Sample Data**
Pre-populated with 8 sample properties:
1. Family House - $105,000 (4 bed, 4 bath)
2. Modern Villa - $110,000 (5 bed, 3 bath)
3. Downtown Apartment - $75,000 (2 bed, 2 bath)
4. Commercial Office - $50,000 (0 bed, 2 bath)
5. Residential Plot - $25,000 (0 bed, 0 bath)
6. Luxury Penthouse - $250,000 (4 bed, 3 bath)
7. Beachfront Villa - $500,000 (6 bed, 5 bath)
8. Cozy Studio - $35,000 (1 bed, 1 bath)

## 🚀 Getting Started

### Installation
1. Ensure Python 3.8+ is installed
2. Navigate to project directory
3. Activate virtual environment: `.\.venv\Scripts\Activate.ps1`
4. Install dependencies: `pip install -r requirements.txt`

### Database Setup
```bash
python manage.py makemigrations properties
python manage.py migrate
python manage.py populate_properties  # Load sample data
```

### Running the Server
```bash
python manage.py runserver
```
Server will be available at: `http://127.0.0.1:8000/`

### Creating Admin User
```bash
python manage.py createsuperuser
```
Then access admin panel at: `http://127.0.0.1:8000/admin/`

## 📋 API Endpoints

### Public Endpoints
- `GET /` - Home page with featured properties
- `GET /properties/` - All properties with search filters
- `GET /properties/<id>/` - Property detail page
- `GET /about/` - About page
- `POST /contact/` - Submit contact inquiry
- `GET /signup/` - Registration page
- `POST /signup/` - Submit registration
- `GET /login/` - Login page
- `POST /login/` - Submit login
- `GET /logout/` - Logout (authenticated users)

## 🔐 Authentication

### User Registration
- Requires: username, email, password, password confirmation
- Validation: Unique username/email, matching passwords, min 6 char password
- Response: Redirect to login on success

### User Login
- Supports: Email or username login
- Validation: Correct credentials
- Response: Redirect to home on success, error message on failure

### Session Management
- Django sessions (database-backed)
- Automatic session cleanup
- Secure cookies

## 📊 Data Models

### Property
```python
- title (CharField)
- description (TextField)
- price (DecimalField)
- location (CharField)
- property_type (Choice: apartment, house, villa, plot, office)
- bedrooms (IntegerField)
- bathrooms (IntegerField)
- area (DecimalField)
- image (ImageField)
- created_at (DateTimeField)
- updated_at (DateTimeField)
- is_active (BooleanField)
```

### Contact
```python
- name (CharField)
- email (EmailField)
- message (TextField)
- created_at (DateTimeField)
- is_read (BooleanField)
```

### UserProfile
```python
- user (OneToOneField to User)
- phone (CharField)
- address (CharField)
- city (CharField)
- created_at (DateTimeField)
```

## 🛠️ Technology Stack
- **Framework**: Django 6.0.3
- **Database**: SQLite3
- **Frontend**: Bootstrap 5.3.2
- **Python**: 3.8+
- **Authentication**: Django built-in auth system

## 📁 Project Structure
```
real-estate-main/
├── properties/           # Main app
│   ├── models.py        # Database models
│   ├── views.py         # Views and logic
│   ├── admin.py         # Admin configuration
│   ├── migrations/      # Database migrations
│   └── management/      # Management commands
├── realestate/          # Project settings
│   ├── settings.py      # Configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── templates/           # Django templates
├── static/              # Static files (CSS, JS, images)
├── manage.py            # Django management
└── db.sqlite3           # SQLite database
```

## ✨ Key Features Implemented

1. ✅ Complete user authentication system
2. ✅ Property CRUD operations via admin
3. ✅ Advanced search and filtering
4. ✅ Contact form with database storage
5. ✅ Responsive design
6. ✅ Django admin panel
7. ✅ CSRF protection
8. ✅ Password hashing
9. ✅ Session management
10. ✅ Sample data population

## 🔄 Future Enhancements
- Payment integration for property purchases
- Email notifications for inquiries
- Property image gallery
- User wishlists/favorites
- Advanced filtering (near/far from location)
- Map integration with property locations
- API endpoints (REST API)
- User profile management
- Property review/ratings system

## 📞 Support
For any issues or questions about the backend, please refer to the Django documentation or contact the development team.

---
**Backend Version**: 1.0  
**Last Updated**: May 1, 2026  
**Status**: ✅ Production Ready
