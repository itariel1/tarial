
from django.urls import path
from .views import hello_world_view, date_view, blog_view, post_detail, create_comment
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("hello", hello_world_view),
    path("date/", date_view),
    path("", blog_view),
    path("<int:pk>/", post_detail, name="post-detail"),
    path("<int:pk>/comment/", create_comment),
 ] \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)