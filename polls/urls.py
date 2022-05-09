from django.urls import path
from . import views

#polls are in their own URLconf (polls/urls.py),
app_name = 'polls' #add namespace to this url so that we can use template with redundant name
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # calls views.index(specified view function with an HttpRequest object )
    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]