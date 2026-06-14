from django.core.management.base import BaseCommand
from properties.models import Property


class Command(BaseCommand):
    help = 'Populate database with sample properties'

    def handle(self, *args, **options):
        properties = [
            {
                'title': 'Family House',
                'description': 'Comfortable villa in Los Angeles. Perfect for a growing family with modern amenities.',
                'price': 105000,
                'location': '2234 Southlea, Los Angeles',
                'property_type': 'house',
                'bedrooms': 4,
                'bathrooms': 4,
                'area': 2647,
            },
            {
                'title': 'Modern Villa',
                'description': 'Spacious villa with contemporary design in Beverly Hills.',
                'price': 110000,
                'location': '5678 Oak Street, Beverly Hills',
                'property_type': 'villa',
                'bedrooms': 5,
                'bathrooms': 3,
                'area': 3500,
            },
            {
                'title': 'Downtown Apartment',
                'description': 'Luxury apartment in the heart of downtown with stunning city views.',
                'price': 75000,
                'location': '123 Main Street, Downtown',
                'property_type': 'apartment',
                'bedrooms': 2,
                'bathrooms': 2,
                'area': 1200,
            },
            {
                'title': 'Commercial Office',
                'description': 'Prime commercial office space perfect for startups and established businesses.',
                'price': 50000,
                'location': '456 Business Ave, Corporate Center',
                'property_type': 'office',
                'bedrooms': 0,
                'bathrooms': 2,
                'area': 2000,
            },
            {
                'title': 'Residential Plot',
                'description': 'Empty plot in a prime location, perfect for building your dream home.',
                'price': 25000,
                'location': '789 Green Way, Suburbs',
                'property_type': 'plot',
                'bedrooms': 0,
                'bathrooms': 0,
                'area': 5000,
            },
            {
                'title': 'Luxury Penthouse',
                'description': 'Stunning penthouse with panoramic views and top-tier amenities.',
                'price': 250000,
                'location': '999 Sky Tower, Luxury District',
                'property_type': 'apartment',
                'bedrooms': 4,
                'bathrooms': 3,
                'area': 4000,
            },
            {
                'title': 'Beachfront Villa',
                'description': 'Exclusive beachfront property with direct beach access.',
                'price': 500000,
                'location': '111 Beach Paradise, Coastal Area',
                'property_type': 'villa',
                'bedrooms': 6,
                'bathrooms': 5,
                'area': 6000,
            },
            {
                'title': 'Cozy Studio',
                'description': 'Perfect starter apartment for young professionals.',
                'price': 35000,
                'location': '222 Spring Lane, Arts District',
                'property_type': 'apartment',
                'bedrooms': 1,
                'bathrooms': 1,
                'area': 600,
            },
        ]

        for prop in properties:
            if not Property.objects.filter(title=prop['title']).exists():
                Property.objects.create(**prop)
                self.stdout.write(self.style.SUCCESS(f"Created property: {prop['title']}"))
            else:
                self.stdout.write(f"Property already exists: {prop['title']}")

        self.stdout.write(self.style.SUCCESS('Successfully populated properties'))
