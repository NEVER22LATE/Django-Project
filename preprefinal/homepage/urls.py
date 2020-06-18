from django.urls import path


from .views import (
    HomepageListView,
    HomepageDetailView,
    HomepageCreateView,
    HomepageUpdateView,
    HomepageDeleteView,
)


urlpatterns = [
    path("post/<int:pk>/delete/", HomepageDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/edit", HomepageUpdateView.as_view(), name="post_edit"),
    path("post/new/", HomepageCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", HomepageDetailView.as_view(), name="post_detail"),
    path("", HomepageListView.as_view(), name="home"),
]
