from django.contrib import admin

from .models import PropertyType, State, City, Category, Transation, Property, Review

admin.site.register(PropertyType)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Transation)
admin.site.register(Property)
admin.site.register(Review)