from django.urls import path
from pro2app import views
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('raisecomplaint', views.raise_complaint, name='raise_complaint'),
    path('mycomplaints', views.mycomplaints, name='mycomplaints'),
    path('head', views.headbase, name="headbase"),
    path('todo', views.todo, name='todo'),
    path('complaints/<int:pk>/solve/', views.solvefunc, name='solvefunc'),
    path('solved', views.solved, name='solved'),
    path('complaints/<int:pk>/like/', views.addlike, name='addlike'),
    path('complaints/<int:pk>/dislike/', views.adddislike, name='adddislike'),
    path('complaints/<int:pk>/tododes/', views.tododes, name='tododes'),
]
