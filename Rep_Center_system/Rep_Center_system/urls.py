from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('schedule/', include('schedule.urls')),
    path('payments/', include('payments.urls')),
    path('courses/', include('courses.urls'))

]
