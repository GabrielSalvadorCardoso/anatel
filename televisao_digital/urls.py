from django.urls import path, include, re_path
from .views import *

app_name = "televisao_digital"
urlpatterns = [
    path('', APIRoot.as_view(), name="root"),

    path('estacoes/<path:operation>/', EstacaoList.as_view(), name='Estacao_list_operation'),
    path('estacoes/<int:pk>', EstacaoDetail.as_view(), name='Estacao_detail'),
    path('estacoes', EstacaoList.as_view(), name='Estacao_list'),
]