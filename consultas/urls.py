from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_consultas),
    path('criar/', views.criar_consulta),
    path('<int:consulta_id>/', views.detalhe_consulta),
    path('profissional/<int:profissional_id>/', views.consultar_consultas_por_profissional),
    path('atualizar/<int:consulta_id>/', views.atualizar_consulta),
    path('deletar/<int:consulta_id>/', views.deletar_consulta),  # outras rotas, se houver
    path('profissionais/', views.listar_profissionais), # listar todos os profissionais
    path('profissionais/<int:profissional_id>/', views.detalhe_profissional), # detalhar um profissional
    path('profissionais/criar/', views.criar_profissionais),  # criar novos profissionais
    path('profissionais/atualizar/<int:profissional_id>/', views.atualizar_profissional),  # atualizar um profissional
    path('profissionais/deletar/<int:profissional_id>/', views.deletar_profissional),  # deletar um profissional
]
