# from django.urls import path
# from .views import HomepageView

# urlpattrens =[
#     path('', HomepageView , name='home')
# ]

from django.urls import path
from .views import homePageView
urlpatterns = [

    path('', homePageView, name='home')

]
