from django.test import TestCase
from .models import CompanyType, Company, Employee, RatingNumber, Review
from .views import index, gettypes, getcompanies, getemployees, getreviews, companydetails
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
#test for models
class CompanyTypeTest(TestCase):
    def test_string(self):
        type = CompanyType(typename="store")
        self.assertEqual(str(type), type.typename)

    def test_table(self):
        self.assertEqual(str(CompanyType._meta.db_table), 'companytype')

class CompanyTest(TestCase):
    def setup(self):
        type = CompanyType(typename="coffeeshop")
        company = Company(companyname="doomsday", companytype=type, companylocation="132", companydescription="test")
        return company
    def test_string(self):
        comp = self.setup()
        self.assertEqual(str(comp), comp.companyname)

    def test_type(self):
        comp = self.setup()
        self.assertEqual(str(comp.companytype), 'coffeeshop')

    def test_table(self):
        self.assertEqual(str(Company._meta.db_table), 'company')

class EmployeeTest(TestCase):
    def setup(self):
        comp = Company(companyname="doomsday")
        employee = Employee(employeename="Michael", employeeposition="cashier", 
                        employeecompany=comp)
        return employee
    def test_string(self):
        emp = self.setup()
        self.assertEqual(str(emp), emp.employeename)

    def test_company(self):
        emp = self.setup()
        self.assertEqual(str(emp.employeecompany), 'doomsday')

    def test_table(self):
        self.assertEqual(str(Employee._meta.db_table), 'employee')

class RatingNumberTest(TestCase):
    def test_string(self):
        num = RatingNumber(ratingnum='5')
        self.assertEqual(str(num), num.ratingnum)

    def test_table(self):
        self.assertEqual(str(RatingNumber._meta.db_table), 'ratingnumber')

class ReviewTest(TestCase):
    def setup(self):
        rating = RatingNumber(ratingnum='3')
        emp = Employee(employeename='Jiyun')
        com = Company(companyname='doomsday')
        review = Review(reviewtitle='goodservice', reviewrating=rating, 
                    reviewemployee=emp, reviewcompany=com)
        return review
    def test_string(self):
        rvw = self.setup()
        self.assertEqual(str(rvw), rvw.reviewtitle)

    def test_emp(self):
        rvw = self.setup()
        self.assertEqual(str(rvw.reviewemployee), 'Jiyun')

    def test_com(self):
        rvw = self.setup()
        self.assertEqual(str(rvw.reviewcompany), 'doomsday')

    def test_rating(self):
        rvw = self.setup()
        self.assertEqual(str(rvw.reviewrating), '3')

    def test_table(self):
        self.assertEqual(str(Review._meta.db_table), 'review') 
    
#tests for views
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetTypesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('types'))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.type=CompanyType.objects.create(typename='coffeeshop')

class GetCompaniesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('companies'))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.u=User.objects.create(username='j')
        self.type=CompanyType.objects.create(typename='coffeeshop')
        # self.emp=Employee.objects.create(employeename='jiyun')
        self.comp=Company.objects.create(companyname='brittle', companytype=self.type,
            companylocation='123', companydescription='test')
        # self.rev1=Review.objects.create(reviewtitle='good', reviewdate='2020-03-03',
        # reviewemployee=self.emp, reviewcompany=self.comp, user=self.u, reviewdescription='good')
        # self.rev1.user.add(self.u)
      
    def test_company_detail_success(self):
        response=self.client.get(reverse('companydetails', args=(self.comp.id,)))
        self.assertEqual(response.status_code, 200)

    # def test_number_of_reviews(self):
    #     reviews=Review.objects.filter(company=self.comp).count()
    #     self.assertEqual(reviews, 1)

class GetEmployeesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('employees'))
        self.assertEqual(response.status_code, 200)

    # def setUp(self):
    #     self.comp=Company.objects.create(companyname='dooms')
        # self.emp=Employee.objects.create(employeename='juno', employeeposition='123', 
        #     employeecompany='doom')
      
    # def test_employee_detail_success(self):
    #     response=self.client.get(reverse('employeedetails', args=(self.emp.id,)))
    #     self.assertEqual(response.status_code, 200)

class GetReviewsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('reviews'))
        self.assertEqual(response.status_code, 200)
