
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("hello", views.hello_world_view),
    path("date/", views.date_view),
    path("", views.blog_view),
    path("<int:pk>/change/", views.PostChangeView.as_view()),
    path("create/", views.BlogCreateView.as_view()),
    path("<int:pk>/", views.post_detail, name="post-detail"),
    path("<int:pk>/comment/", views.create_comment),
 ] \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)