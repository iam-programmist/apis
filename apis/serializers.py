from rest_framework import serializers
from .models import Category, WorkerCategory, EmployerCategory, Country, City, Worker, Employer, VacancyCategory, VacancyLocation, Vacancy, Application

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class WorkerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerCategory
        fields = '__all__'

class EmployerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerCategory
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

class VacancyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyCategory
        fields = '__all__'

class VacancyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyLocation
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
