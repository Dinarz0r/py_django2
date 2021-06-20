from django.urls import path
from .views import upload_files, model_form_upload, upload_files_view

urlpatterns = [
    path('upload_file/', upload_files, name='upload-file'),
    path('model_form_upload_file/', model_form_upload, name='model_form_upload_file'),
    path('upload_files/', upload_files_view, name='upload_files'),

]
