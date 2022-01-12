
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/<int:pk>', views.student_list),
    path('studentsall', views.student_all)
]
