from django.urls import path
from . import views
from diulibrary.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
#    path('',views.stdisplay, name="stdisplay"),
#    path('team_create',views.stinsert, name="stinsert"),
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)

]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)