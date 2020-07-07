from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', include('Blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
