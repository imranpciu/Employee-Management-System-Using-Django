from django.urls import path
from .views.add_emp_view import *
from .views.index_view import *
from .views.delete_emp_view import*
from .views.update_emp_view import *

urlpatterns = [
    path('', index),
    path('index/', index),
    path('add_employee/',add_emp),
    path('emp_delete/<int:id>', emp_delete),
    path('emp_update/<int:id>', emp_update),
    path('emp_do_update/<int:id>', emp_do_update),
]
