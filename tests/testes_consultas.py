from django.test import TestCase, Client
from django.urls import reverse
from consultas.models import Consulta, Profissional
import json

class ConsultaTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.profissional = Profissional.objects.create(nome="Dr. Smith")
        self.consulta = Consulta.objects.create(profissional=self.profissional, data_consulta="2023-12-01")

    def test_listar_consultas(self):
        response = self.client.get(reverse('listar_consultas'))
        self.assertEqual(response.status_code, 200)

    def test_criar_consulta(self):
        data = {
            'profissional_id': self.profissional.id,
            'data_consulta': '2024-01-01'
        }
        response = self.client.post(reverse('criar_consulta'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Consulta.objects.count(), 2)

    def test_detalhe_consulta(self):
        response = self.client.get(reverse('detalhe_consulta', kwargs={'consulta_id': self.consulta.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], self.consulta.id)

    def test_consultar_consultas_por_profissional(self):
        response = self.client.get(reverse('consultar_consultas_por_profissional', kwargs={'profissional_id': self.profissional.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_atualizar_consulta(self):
        data = {
            'profissional_id': self.profissional.id,
            'data_consulta': '2024-02-01'
        }
        response = self.client.put(reverse('atualizar_consulta', kwargs={'consulta_id': self.consulta.id}), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.consulta.refresh_from_db()
        self.assertEqual(str(self.consulta.data_consulta), '2024-02-01')

    def test_deletar_consulta(self):
        response = self.client.delete(reverse('deletar_consulta', kwargs={'consulta_id': self.consulta.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Consulta.objects.count(), 0)
