
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/<int:pk>', views.student_list),
    path('studentsall', views.student_all),
     path('studentcreate/', views.student_create),

path('studentclass/', views.StudentAll.as_view()),
path('studentclass/<int:pk>', views.StudentAll.as_view()),

#for mixins 
path('studentclassm/', views.StudentMList.as_view()),
path('studentclassm/<int:pk>', views.StudentM_URD.as_view()),

#for generic views
path('studentclassg/', views.StudentListCreateGeneric.as_view()),
path('studentclassg/<int:pk>', views.StudentRUD.as_view())




]
