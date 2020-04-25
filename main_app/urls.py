from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blogposts/', views.blogposts_index, name='index'),
    path('blogposts/all/', views.blogposts_all, name='blogposts_all'),
    path('blogposts/create/', views.BlogpostCreate.as_view(),
         name='blogposts_create'),
<<<<<<< HEAD
=======
    path('blogposts/<int:blogpost_id>/add_photo/',
         views.add_photo, name='add_photo'),
>>>>>>> b8a7472c38a771a57e57d1504060b5be7add47fc
    path('blogposts/<int:blogpost_id>/', views.blogposts_detail, name='detail'),
    path('blogposts/<int:pk>/update/',
         views.BlogpostUpdate.as_view(), name='blogposts_update'),
    path('blogposts/<int:pk>/delete/',
         views.BlogpostDelete.as_view(), name='blogposts_delete'),
    path('blogposts/<int:blogpost_id>/add_comment/',
         views.add_comment, name='add_comment'),
    path('accounts/signup/', views.signup, name='signup'),
<<<<<<< HEAD
    path('blogposts/<int:blogpost_id>/add_photo/',
         views.add_photo, name='add_photo'),
=======
>>>>>>> b8a7472c38a771a57e57d1504060b5be7add47fc

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
