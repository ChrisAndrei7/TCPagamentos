from behave import given, when, then
import requests

BASE_URL = 'http://localhost:8001'

@given('que eu tenho os detalhes do pagamento')
def step_impl(context):
    context.pagamento_data = {
        'pedido_id': '1',
        'status': 'PAGO',
        'valor': '15.80',
    }

@given('que eu tenho os detalhes atualizados do pagamento')
def step_impl(context):
    context.updated_pagamento_data = {
        'pedido_id': '1',
        'status': 'AGUARDANDO_PAGAMENTO',
        'valor': '17.99',
    }

@when('eu faço o cadastro de um pagamento')
def step_impl(context):
    context.response = requests.post(f"{BASE_URL}/pagamentos/create", json=context.pagamento_data)

@when('eu faço uma atualização de um pagamento')
def step_impl(context):
    context.response = requests.put(f"{BASE_URL}/pagamentos/update/1", json=context.updated_pagamento_data)

@when('eu faço a consulta dos pagamentos cadastros')
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/pagamentos")

@when('eu faço a exclusão de um pagamento')
def step_impl(context):
    context.response = requests.delete(f"{BASE_URL}/pagamentos/delete/1")

@then('eu devo receber uma resposta com o código de status 201')
def step_impl(context):
    assert context.response.status_code == 201

@then('eu devo receber uma resposta com o código de status 200')
def step_impl(context):
    assert context.response.status_code == 200
