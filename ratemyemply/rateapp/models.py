from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CompanyType(models.Model):
    typename = models.CharField(max_length=255)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'companytype'
        verbose_name_plural = 'companytypes'

class Company(models.Model):
    companyname = models.CharField(max_length=255)
    companytype = models.ForeignKey(CompanyType, on_delete=models.DO_NOTHING)
    companylocation = models.CharField(max_length=255, null=True, blank=True)
    companydescription = models.TextField()

    def __str__(self):
        return self.companyname

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'companies'

class Employee(models.Model):
    employeename = models.CharField(max_length=255)
    employeeposition = models.CharField(max_length=255)
    employeecompany = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.employeename

    class Meta:
        db_table = 'employee'
        verbose_name_plural = 'employees'

class RatingNumber(models.Model):
    ratingnum = models.SmallIntegerField()

    def __str__(self):
        return str(self.ratingnum)

    class Meta:
        db_table = 'ratingnumber'
        verbose_name_plural = 'ratingnumbers'

class Review(models.Model):
    reviewtitle = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    reviewdate = models.DateField()
    reviewrating = models.ForeignKey(RatingNumber, on_delete=models.DO_NOTHING)
    reviewemployee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    reviewcompany = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    reviewdescription = models.TextField()

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table = 'review'
        verbose_name_plural = 'reviews'

