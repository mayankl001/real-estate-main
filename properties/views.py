from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from .models import Property, Contact, UserProfile

# Create your views here.

def home(request):
    properties = Property.objects.filter(is_active=True)[:6]
    context = {
        'properties': properties,
    }
    return render(request, 'index.html', context)


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
        else:
            messages.error(request, 'Please fill all fields.')
        return redirect('contact')
    return render(request, 'contact.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        # Validation
        if not username or not email or not password or not cpassword:
            messages.error(request, 'Please fill all fields.')
            return redirect('signup')
        
        if password != cpassword:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('signup')
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        UserProfile.objects.create(user=user)
        
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    
    return render(request, 'signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('email')  # HTML form uses 'email' field
        password = request.POST.get('password')
        
        # Try authenticating with username first, then email
        user = None
        if User.objects.filter(email=username).exists():
            user_obj = User.objects.get(email=username)
            user = authenticate(request, username=user_obj.username, password=password)
        else:
            user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email/username or password.')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')


def property_list(request):
    properties = Property.objects.filter(is_active=True)
    
    # Search and filter
    location = request.GET.get('location')
    property_type = request.GET.get('type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if location:
        properties = properties.filter(location__icontains=location)
    
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    if min_price:
        try:
            properties = properties.filter(price__gte=float(min_price))
        except:
            pass
    
    if max_price:
        try:
            properties = properties.filter(price__lte=float(max_price))
        except:
            pass
    
    context = {
        'properties': properties,
        'location': location or '',
        'property_type': property_type or '',
        'min_price': min_price or '',
        'max_price': max_price or '',
    }
    return render(request, 'properties.html', context)


def property_detail(request, id):
    try:
        property_obj = Property.objects.get(id=id, is_active=True)
    except Property.DoesNotExist:
        messages.error(request, 'Property not found.')
        return redirect('property_list')
    
    # Get related properties
    related_properties = Property.objects.filter(
        property_type=property_obj.property_type,
        is_active=True
    ).exclude(id=id)[:3]
    
    context = {
        'property': property_obj,
        'related_properties': related_properties,
    }
    return render(request, 'view-property.html', context)


def about_view(request):
    return render(request, 'about.html')


def search_properties(request):
    location = request.GET.get('location', '')
    property_type = request.GET.get('type', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    
    return redirect(f'properties/?location={location}&type={property_type}&min_price={min_price}&max_price={max_price}')
