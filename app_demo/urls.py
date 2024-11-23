from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('student/',views.post_student, name='student'),
    path('update-student/<id>/',views.update_student, name='update_student'),
    path('delete-student/<id>/',views.delete_student, name='delete_student'),
]
