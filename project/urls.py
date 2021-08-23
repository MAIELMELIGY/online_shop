from django.contrib import admin
from django.urls import path , include
from pet import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/pets/', views.pet_list.as_view()),
    path('api/v1/pets/<int:pk>', views.pet_update.as_view()),
    path('api/v1/orders/',views.order_list.as_view()),
    path('api/v1/breed/',views.breed_list.as_view()),

    
]