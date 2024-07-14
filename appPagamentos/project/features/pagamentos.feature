Feature: Gerenciamento de pagamentos

  Scenario: Adicionar um novo pagamento
    Given que eu tenho os detalhes do pagamento
    When eu faço o cadastro de um pagamento
    Then eu devo receber uma resposta com o código de status 201

  Scenario: Consultar um pagamento
    When eu faço a consulta dos pagamentos cadastros
    Then eu devo receber uma resposta com o código de status 200

  Scenario: Editar um pagamento existente
    Given que eu tenho os detalhes atualizados do pagamento
    When eu faço uma atualização de um pagamento
    Then eu devo receber uma resposta com o código de status 200
