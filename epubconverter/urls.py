from django.urls import path
from .views import pdf_upload_view  # Certifique-se de que a view está importada corretamente

urlpatterns = [
    path('', pdf_upload_view, name='pdf_upload'),  # Caminho vazio para mapear a URL base
]
