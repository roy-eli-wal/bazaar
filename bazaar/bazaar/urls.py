from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views 
from django.conf import settings
from django.conf.urls.static import static 

from core.views import index, contact, items, userRegisterion, user_logout, privacypolicy, about, termofuse
from item.views import item_detail, new_listing, panel,delete_item
from core.reg_forms import SigninForm
# from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from chat.views import chat_start,chatbox,description


app_name = items

urlpatterns = [
    path('chatbox/', chatbox, name='chatbox'),
    path('<int:pk>/', description, name='description'),
    path('new/<int:item_pk>/', chat_start, name='chatstart'),

    path('', index, name="index"),
    path('contact/', contact, name= "contact"),
    path('privacypolicy/', privacypolicy, name="privacypolicy"),
    path('about/', about, name="about"),
    path('termofuse/', termofuse, name="termofuse"),
    path('signin/', views.LoginView.as_view(template_name='core/signin_form.html', authentication_form=SigninForm), name='signin'),
    path('user-reg/', userRegisterion, name="user-registerion"),
    path('all-items/', items, name="all-items"),
    path('contact/', contact, name= "contact"),
    path('new-listing/',new_listing, name= 'new-listing'),
     path('items/<int:pk>/delete/', delete_item, name="delete-item"),
    path('items/<int:pk>/', item_detail, name="item-detail"),
    path('mylistings/', panel, name= "my-listings"),
    # path('logout/', auth_views.LogoutView.as_view(), name='user-logout'),
    #  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user-logout/', user_logout, name='user-logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
