from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Consulta, Profissional
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import logging
import json

@csrf_exempt
def listar_consultas(request):
    consultas = Consulta.objects.all().values()
    return JsonResponse(list(consultas), safe=False)

@csrf_exempt
def criar_consulta(request):
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
                profissional_id = data.get('profissional_id')
                data_consulta = data.get('data_consulta')
            else:
                profissional_id = request.POST.get('profissional_id')
                data_consulta = request.POST.get('data_consulta')

            logger.info(f"ID do Profissional recebido: {profissional_id}")
            logger.info(f"Data da Consulta recebida: {data_consulta}")

            if not profissional_id or not data_consulta:
                logger.error('Campos obrigatórios ausentes')
                return JsonResponse({'status': 'error', 'message': 'Campos obrigatórios ausentes'})

            consulta = Consulta(profissional_id=profissional_id, data_consulta=data_consulta)
            consulta.save()

            logger.info(f"Consulta criada com ID: {consulta.id}")
            return JsonResponse({'status': 'ok', 'id': consulta.id})
        except Exception as e:
            logger.exception(f"Erro ao criar a consulta: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
def detalhe_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, pk=consulta_id)
    if request.method == 'GET':
        return JsonResponse({
            'id': consulta.id,
            'profissional_id': consulta.profissional_id,
            'data_consulta': consulta.data_consulta
        })
    
@csrf_exempt
def consultar_consultas_por_profissional(request, profissional_id):
    logger = logging.getLogger(__name__)

    try:
        consultas = Consulta.objects.filter(profissional_id=profissional_id).values()
        return JsonResponse(list(consultas), safe=False)
    except Exception as e:
        logger.exception(f"Erro ao consultar as consultas do profissional ID {profissional_id}: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
def atualizar_consulta(request, consulta_id):
    logger = logging.getLogger(__name__)
    consulta = get_object_or_404(Consulta, pk=consulta_id)

    if request.method == 'PUT':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
                consulta.profissional_id = data.get('profissional_id', consulta.profissional_id)
                consulta.data_consulta = data.get('data_consulta', consulta.data_consulta)
            else:
                consulta.profissional_id = request.POST.get('profissional_id', consulta.profissional_id)
                consulta.data_consulta = request.POST.get('data_consulta', consulta.data_consulta)

            consulta.save()
            logger.info(f"Consulta ID {consulta.id} atualizada")
            return JsonResponse({'status': 'ok'})
        except Exception as e:
            logger.exception(f"Erro ao atualizar a consulta: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

@csrf_exempt
def deletar_consulta(request, consulta_id):
    try:
        consulta = get_object_or_404(Consulta, pk=consulta_id)
        if request.method == 'DELETE':
            consulta.delete()
            return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Delete request failed'})

@method_decorator(csrf_exempt, name='dispatch')
def criar_profissionais(request):
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
                nome = data.get('nome')
                nome_social = data.get('nome_social')
            else:
                nome = request.POST.get('nome')
                nome_social = request.POST.get('nome_social')

            logger.info(f"Nome recebido: {nome}")
            logger.info(f"Nome social recebido: {nome_social}")

            if not nome:
                logger.error('Campo "nome" é obrigatório')
                return JsonResponse({'status': 'error', 'message': 'Campo "nome" é obrigatório'})

            profissional = Profissional(nome=nome, nome_social=nome_social)
            profissional.save()

            logger.info(f"Profissional criado com ID: {profissional.id}")
            return JsonResponse({'status': 'ok', 'id': profissional.id})
        except Exception as e:
            logger.exception(f"Erro ao criar o profissional: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)})

@method_decorator(csrf_exempt, name='dispatch')
def listar_profissionais(request):
    if request.method == 'GET':
        profissionais = Profissional.objects.all().values()
        return JsonResponse(list(profissionais), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
def detalhe_profissional(request, profissional_id):
    profissional = get_object_or_404(Profissional, pk=profissional_id)
    if request.method == 'GET':
        return JsonResponse({
            'id': profissional.id,
            'nome': profissional.nome,
            'nome_social': profissional.nome_social
        })

@method_decorator(csrf_exempt, name='dispatch')
def atualizar_profissional(request, profissional_id):
    logger = logging.getLogger(__name__)
    profissional = get_object_or_404(Profissional, pk=profissional_id)

    if request.method == 'PUT':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
                profissional.nome = data.get('nome', profissional.nome)
                profissional.nome_social = data.get('nome_social', profissional.nome_social)
            else:
                profissional.nome = request.POST.get('nome', profissional.nome)
                profissional.nome_social = request.POST.get('nome_social', profissional.nome_social)

            profissional.save()
            logger.info(f"Profissional ID {profissional.id} atualizado")
            return JsonResponse({'status': 'ok'})
        except Exception as e:
            logger.exception(f"Erro ao atualizar o profissional: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})
    
@method_decorator(csrf_exempt, name='dispatch')
def deletar_profissional(request, profissional_id):
    try:
        profissional = get_object_or_404(Profissional, pk=profissional_id)
        if request.method == 'DELETE':
            profissional.delete()
            return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Delete request failed'})
