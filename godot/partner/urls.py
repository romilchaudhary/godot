from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "partner"
urlpatterns = [
    path('', views.index, name="index"),
    path('add_new_partner', views.add_edit_partner, name="add_new_partner"),
    path('add_edit_partner/<int:pk>', views.add_edit_partner, name="edit_partner"),
    path('members_list/<int:pk>', views.add_edit_member, name="members_list"),
    path('member_ajax/<int:pk>', views.member_ajax_save, name="member_ajax"),
    path('api/member_save', views.save_member_api, name="member_save_api"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
