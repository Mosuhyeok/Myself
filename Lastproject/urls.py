
from django.contrib import admin
from django.urls import path
import main.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main.views.home,name="home"),
    path('gs/',main.views.gs, name='gs'),
    path('hiphop/',main.views.hiphop, name="hiphop"),
    path('bal/',main.views.bal, name='bal'),
    path('dance/',main.views.dance, name="dance"),
    path('about/',main.views.about, name="about"),
]
