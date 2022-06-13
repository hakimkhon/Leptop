from django.urls import path
from.views import KompListView, KompDetailView

urlpatterns = [
    path('', KompListView.as_view()),
    path('<pk>/', KompDetailView.as_view()),
]
