from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_consultas, name='listar_consultas'),
    path('criar/', views.criar_consulta, name='criar_consulta'),
    path('<int:consulta_id>/', views.detalhe_consulta, name='detalhe_consulta'),
    path('profissional/<int:profissional_id>/', views.consultar_consultas_por_profissional, name='consultar_consultas_por_profissional'),
    path('atualizar/<int:consulta_id>/', views.atualizar_consulta, name='atualizar_consulta'),
    path('deletar/<int:consulta_id>/', views.deletar_consulta, name='deletar_consulta'),
    path('profissionais/', views.listar_profissionais),
    path('profissionais/<int:profissional_id>/', views.detalhe_profissional),
    path('profissionais/criar/', views.criar_profissionais),
    path('profissionais/atualizar/<int:profissional_id>/', views.atualizar_profissional),
    path('profissionais/deletar/<int:profissional_id>/', views.deletar_profissional),
]
