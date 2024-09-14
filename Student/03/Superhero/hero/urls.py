from django.urls import path
from .views import IndexView, DeadPool, SpiderMan, SuperMan, BatMan

urlpatterns = [
    path('', IndexView.as_view()),
    path('deadpool',DeadPool.as_view()),
    path('spiderman', SpiderMan.as_view()),
    path('superman', SuperMan.as_view()),
    path('batman', BatMan.as_view()),
]
