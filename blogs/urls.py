
from django.urls import path
from blogs import views
from portfolio.views import home


app_name='blogs'


urlpatterns = [ 
    path('',views.all_blogs,name='all_blogs'),
    path('<int:blogs_id>/',views.details,name='details')
    
    
    

]

