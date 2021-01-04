from django.urls import path

from . import views
urlpatterns = [
    path('select', views.select),
    # # path('shopping_mall/', mall_views.mall_views.as_view()),
    # path('shopping_mall/', include('mall_views.urls')),

]