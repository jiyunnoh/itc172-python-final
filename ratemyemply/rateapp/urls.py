from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('gettypes/', views.gettypes, name = 'types'),
    path('getcompanies/', views.getcompanies, name = 'companies'),
    path('companydetails/<int:id>', views.companydetails, name = 'companydetails'),
    path('getemployees/', views.getemployees, name = 'employees'),
    path('employeedetails/<int:id>', views.employeedetails, name = 'employeedetails'),
    path('getreviews/', views.getreviews, name = 'reviews'),
    path('reviewdetails/<int:id>', views.reviewdetails, name = 'reviewdetails'),
    path('newCompany/', views.newCompany, name='newcompany'),
    path('newEmployee/', views.newEmployee, name='newemployee'),
    path('newReview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]