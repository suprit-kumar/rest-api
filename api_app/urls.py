from django.urls import path
from api_app.views import *
urlpatterns = [
    # path('', include('api_app.urls')),
    path('', home, name='home'),
    path('userdata/',post_data, name='post_data'),
    path('userupdate/<id>', updateUser, name='updateUser'),
    path('userdelete/<id>',deleteUser, name='deleteUser'),
    path('allbooks/', get_book, name='allbooks'),
    path('student/',StudentAPI.as_view()),
    path('register/',RegisterUser.as_view()),

]
