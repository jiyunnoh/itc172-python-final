from django import forms
from .models import CompanyType, Company, Employee, Review
from django.test import TestCase


class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'

#Form tests
class Company_Form_Test(TestCase):
    def test_companyform_is_valid(self):
        form=CompanyForm(data={'companyname': "comp1", 'companylocation': "123"})
        self.assertTrue(form.is_valid())

    def test_companyform_minus_descript(self):
        form=CompanyForm(data={'companyname': "comp1"})
        self.assertTrue(form.is_valid())

    def test_companyform_empty(self):
        form=CompanyForm(data={'companyname': ""})
        self.assertFalse(form.is_valid())

class Employee_Form_Test(TestCase):
    def test_employeeform_is_valid(self):
        form=EmployeeForm(data={'employeename': "comp1", 'employeeposition': "123"})
        self.assertTrue(form.is_valid())

    def test_employeeform_minus_descript(self):
        form=EmployeeForm(data={'employeename': "comp1"})
        self.assertTrue(form.is_valid())

    def test_employeeform_empty(self):
        form=EmployeeForm(data={'employeename': ""})
        self.assertFalse(form.is_valid())

class Review_Form_Test(TestCase):
    def test_reviewform_is_valid(self):
        form=ReviewForm(data={'reviewtitle': "comp1", 'reviewdescription': "123"})
        self.assertTrue(form.is_valid())

    def test_reviewform_minus_descript(self):
        form=ReviewForm(data={'reviewtitle': "comp1"})
        self.assertTrue(form.is_valid())

    def test_reviewform_empty(self):
        form=ReviewForm(data={'reviewtitle': ""})
        self.assertFalse(form.is_valid())
