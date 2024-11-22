from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView,RetrieveUpdateAPIView, DestroyAPIView
from .models import Category, WorkerCategory, EmployerCategory, Country, City, Worker, Employer, VacancyCategory, VacancyLocation, Vacancy, Application
from .serializers import CategorySerializer, WorkerCategorySerializer, EmployerCategorySerializer, CountrySerializer, CitySerializer, WorkerSerializer, EmployerSerializer, VacancyCategorySerializer, VacancyLocationSerializer, VacancySerializer, ApplicationSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class WorkerCategoryListAPIView(ListAPIView):
    queryset = WorkerCategory.objects.all()
    serializer_class = WorkerCategorySerializer

class WorkerCategoryCreateAPIView(CreateAPIView):
    queryset = WorkerCategory.objects.all()
    serializer_class = WorkerCategorySerializer

class WorkerCategoryRetrieveAPIView(RetrieveAPIView):
    queryset = WorkerCategory.objects.all()
    serializer_class = WorkerCategorySerializer

class WorkerCategoryUpdateAPIView(UpdateAPIView):
    queryset = WorkerCategory.objects.all()
    serializer_class = WorkerCategorySerializer

class WorkerCategoryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = WorkerCategory.objects.all()
    serializer_class = WorkerCategorySerializer

class WorkerCategoryDestroyAPIView(DestroyAPIView):
    queryset = WorkerCategory.objects.all()
    serializer_class = WorkerCategorySerializer

class EmployerCategoryListAPIView(ListAPIView):
    queryset = EmployerCategory.objects.all()
    serializer_class = EmployerCategorySerializer

class EmployerCategoryCreateAPIView(CreateAPIView):
    queryset = EmployerCategory.objects.all()
    serializer_class = EmployerCategorySerializer

class EmployerCategoryRetrieveAPIView(RetrieveAPIView):
    queryset = EmployerCategory.objects.all()
    serializer_class = EmployerCategorySerializer

class EmployerCategoryUpdateAPIView(UpdateAPIView):
    queryset = EmployerCategory.objects.all()
    serializer_class = EmployerCategorySerializer

class EmployerCategoryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = EmployerCategory.objects.all()
    serializer_class = EmployerCategorySerializer

class EmployerCategoryDestroyAPIView(DestroyAPIView):
    queryset = EmployerCategory.objects.all()
    serializer_class = EmployerCategorySerializer

class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryCreateAPIView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryRetrieveAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryUpdateAPIView(UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDestroyAPIView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityListAPIView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityCreateAPIView(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityRetrieveAPIView(RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityUpdateAPIView(UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDestroyAPIView(DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class WorkerListAPIView(ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerCreateAPIView(CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerRetrieveAPIView(RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerUpdateAPIView(UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class WorkerDestroyAPIView(DestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class EmployerListAPIView(ListAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerCreateAPIView(CreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerRetrieveAPIView(RetrieveAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerUpdateAPIView(UpdateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerDestroyAPIView(DestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class VacancyCategoryListAPIView(ListAPIView):
    queryset = VacancyCategory.objects.all()
    serializer_class = VacancyCategorySerializer

class VacancyCategoryCreateAPIView(CreateAPIView):
    queryset = VacancyCategory.objects.all()
    serializer_class = VacancyCategorySerializer

class VacancyCategoryRetrieveAPIView(RetrieveAPIView):
    queryset = VacancyCategory.objects.all()
    serializer_class = VacancyCategorySerializer

class VacancyCategoryUpdateAPIView(UpdateAPIView):
    queryset = VacancyCategory.objects.all()
    serializer_class = VacancyCategorySerializer

class VacancyCategoryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = VacancyCategory.objects.all()
    serializer_class = VacancyCategorySerializer

class VacancyCategoryDestroyAPIView(DestroyAPIView):
    queryset = VacancyCategory.objects.all()
    serializer_class = VacancyCategorySerializer

class VacancyLocationListAPIView(ListAPIView):
    queryset = VacancyLocation.objects.all()
    serializer_class = VacancyLocationSerializer

class VacancyLocationCreateAPIView(CreateAPIView):
    queryset = VacancyLocation.objects.all()
    serializer_class = VacancyLocationSerializer

class VacancyLocationRetrieveAPIView(RetrieveAPIView):
    queryset = VacancyLocation.objects.all()
    serializer_class = VacancyLocationSerializer

class VacancyLocationUpdateAPIView(UpdateAPIView):
    queryset = VacancyLocation.objects.all()
    serializer_class = VacancyLocationSerializer

class VacancyLocationRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = VacancyLocation.objects.all()
    serializer_class = VacancyLocationSerializer

class VacancyLocationDestroyAPIView(DestroyAPIView):
    queryset = VacancyLocation.objects.all()
    serializer_class = VacancyLocationSerializer

class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyCreateAPIView(CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyRetrieveAPIView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyUpdateAPIView(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDestroyAPIView(DestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class ApplicationListAPIView(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationCreateAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationRetrieveAPIView(RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationUpdateAPIView(UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationDestroyAPIView(DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
