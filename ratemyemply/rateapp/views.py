from django.shortcuts import render, get_object_or_404
from .models import CompanyType, Company, Employee, RatingNumber, Review
from .forms import CompanyForm, EmployeeForm, ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index (request):
    return render(request, 'rateapp/index.html')

def gettypes(request):
    type_list = CompanyType.objects.all()
    return render(request, 'rateapp/types.html', {'type_list': type_list})

def getcompanies(request):
    companies_list = Company.objects.all()
    return render(request, 'rateapp/companies.html', {'companies_list': companies_list})

def companydetails(request, id):
    comp = get_object_or_404(Company, pk=id)

    compreviews = Review.objects.filter(reviewcompany=id).count()
    context = {
        'comp': comp,
        'compreviews': compreviews,
    }
    return render(request, 'rateapp/companydetails.html', context = context)

def getemployees(request):
    employees_list = Employee.objects.all()
    return render(request, 'rateapp/employees.html', {'employees_list': employees_list})

def employeedetails(request, id):
    emp = get_object_or_404(Employee, pk=id)

    empreviews = Review.objects.filter(reviewemployee=id).count() #It has to match the name of the field in model
    context = {
        'emp': emp,
        'empreviews': empreviews,
    }
    return render(request, 'rateapp/employeedetails.html', context = context)

def getreviews(request):
    reviews_list = Review.objects.all()
    return render(request, 'rateapp/reviews.html', {'reviews_list': reviews_list})

def reviewdetails(request, id):
    rvw = get_object_or_404(Review, pk=id)
    return render(request, 'rateapp/reviewdetails.html', {'rvw': rvw})

@login_required
def newCompany(request):
    form=CompanyForm
    if request.method=='POST':
        form=CompanyForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=CompanyForm()
    else:
        form=CompanyForm()
    return render(request, 'rateapp/newcompany.html', {'form': form})

@login_required
def newEmployee(request):
    form=EmployeeForm
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EmployeeForm()
    else:
        form=EmployeeForm()
    return render(request, 'rateapp/newemployee.html', {'form': form})

@login_required
def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'rateapp/newreview.html', {'form': form})

def loginmessage(request):
    return render(request, 'rateapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'rateapp/logoutmessage.html')

