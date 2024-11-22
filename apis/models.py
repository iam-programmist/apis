from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name
    
class WorkerCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    worker_category = models.CharField(max_length = 100)

    def __str__(self):
        return self.worker_category
    
class EmployerCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    employer_category = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.employer_category
    
class Country(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class City(models.Model):
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Worker(AbstractUser):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 100, unique = True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length = 15, unique = True)
    image = models.ImageField(upload_to = 'media/images', null = True, blank = True)
    country =  models.ForeignKey(Country, on_delete = models.CASCADE)
    city =  models.ForeignKey(City, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.username} - {self.age} - {self.phone_number} - {self.country} - {self.city}'
    
class Employer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 100, unique = True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length = 15, unique = True)
    image = models.ImageField(upload_to = 'media/images', null = True, blank = True)
    country =  models.ForeignKey(Country, on_delete = models.CASCADE)
    city =  models.ForeignKey(City, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.username} - {self.age} - {self.phone_number} - {self.country} - {self.city}'
    
class VacancyCategory(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.name
    
class VacancyLocation(models.Model):
    vacancy_category = models.ForeignKey(VacancyCategory, on_delete = models.CASCADE)
    vacancy_location = models.CharField(max_length = 100)

    def __str__(self):                  
        return self.vacancy_location

class Vacancy(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'media/images', null = True, blank = True)
    description =  models.TextField()
    salary = models.IntegerField()
    work_schedule = models.CharField(max_length = 50)
    type_of_employment = models.CharField(max_length = 50)
    location = models.ForeignKey(VacancyLocation, on_delete = models.CASCADE)
    category = models.ForeignKey(VacancyCategory, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True) 

    def __str__(self):
        return f'{self.title} - {self.description} - {self.salary} - {self.work_schedule} - {self.type_of_employment} - {self.location} - {self.category} - {self.created_at} - {self.is_active}'
    
class Application(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 100, unique = True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length = 15, unique = True)
    image = models.ImageField(upload_to = 'media/images', null = True, blank = True)
    country =  models.ForeignKey(Country, on_delete = models.CASCADE)
    city =  models.ForeignKey(City, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.username} - {self.age} - {self.phone_number} - {self.country} - {self.city}'