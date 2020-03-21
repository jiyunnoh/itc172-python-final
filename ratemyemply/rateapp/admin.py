from django.contrib import admin
from .models import CompanyType, Company, Employee, RatingNumber, Review

# Register your models here.
admin.site.register(CompanyType)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(RatingNumber)
admin.site.register(Review)
