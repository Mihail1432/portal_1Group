from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.PortfolioHomeView.as_view(), name='home'),
    path('create/', views.PortfolioCreateView.as_view(), name='portfolio-create'),
    path('<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('<int:pk>/update/', views.PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('<int:pk>/delete/', views.PortfolioDeleteView.as_view(), name='portfolio-delete'),
]

app_name = "portfolio"