from django.contrib import admin
from django.urls import path, include
from NamiPay import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_page, name='login'),
    #path('',views.submit_work, name='submit_work'),
    path('submit-task/', views.submit_work, name='home'),
    path("success/",views.Success,name="Success"),
    #path('accounts', views.accounts),
    path('accounts', views.signup, name = 'signup'),
    path('login/', views.login_page, name = 'login'),
    path('authorized', views.authorized, name='authorized'),
    path('dummy', views.dummy, name='dummy'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
