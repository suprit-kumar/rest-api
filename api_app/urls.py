from django.urls import path
from api_app import views

urlpatterns = [
    # path('', include('api_app.urls')),
    path('', views.home, name='home'),
    path('userdata/', views.post_data, name='post_data'),
    path('userupdate/<id>', views.updateUser, name='updateUser'),
    path('userdelete/<id>', views.deleteUser, name='deleteUser'),
]
