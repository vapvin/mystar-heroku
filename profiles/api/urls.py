from django.urls import path
from profiles.api.views import ProfileList, ChangePasswordView
from .views import CustomObtainAuthToken


profiles_list = ProfileList.as_view({"get": "list", "put": "update"})

urlpatterns = [
    path("log-in/", CustomObtainAuthToken.as_view(), name="log-in"),
    path("profiles/", profiles_list, name="profiles"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
