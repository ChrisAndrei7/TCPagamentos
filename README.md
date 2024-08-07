<h1 align="center"> TCFoodSystem - Sistema de pedidos para lanches </h1>
Bem-vindo ao Sistema de Pedidos para Lanchonete! Este projeto está em desenvolvimento como atividade do Tech Challenge para a FIAP, curso Software Architecture.	
<br/>
<b>Neste repositório, temos o microsserviço de pagamentos.</b>
<br/>
:construction: Projeto em construção :construction:
<br/>

# :computer: Endpoint base da aplicação
http://localhost:8001/
<br/>
<br/>

# :hammer: Subida da aplicação
### Subida completa da aplicação via docker:

#### - Subida no docker:
1. Entre no diretório do projeto: `cd appPagamentos`
2. Efetue a criação/subida do banco de dados: `docker compose up -d dbPagamentos`
3. Efetue a criação da aplicação: `docker compose build`                                                                                                                                                                                                                                                     
      <b>Nota Importante:
      Ao realizar a primeira inicialização, ocasionalmente pode ocorrer o erro "No installed app with label 'pagamentos'". Como solução temporária, sugerimos a seguinte abordagem: caso o erro mencionado ocorra na primeira subida, modifique o arquivo "django.sh" na linha       3, substituindo "pagamentos" por "application" e efetue novamente o passo 3 antes de seguir para o passo 4.</b>
4. Efetue a subida da aplicação: `docker compose up`
<br/>
  
# :arrow_forward: Uso 
Abaixo, fluxos principais com processo e endpoint desse microsserviço. Para maior detalhe dos campos, temos no projeto(Na pasta appPagamentos/Documentos) o arquivo do Postman com a collection estruturando todos as APIs com descrição e valores a serem informados no json.

1 - Criar o pagamento: http://localhost:8001/pagamentos/create

2 - Consultar pagamentos: http://localhost:8001/pagamentos/

3 - Atualizar pagamento: http://localhost:8001/pagamentos/update/{id_do_pagamento}

4 - Deletar pagamento: http://localhost:8001/pagamentos/delete/{id_do_pagamento}

# :page_with_curl: Collection
Disponibilizamos uma collection do postman para ajudar na utilização, contendo todas as APIs deste microserviço e com os campos necessários para preenchimento. 

# :test_tube: Testes
Para executar os testes, localizados dentro da pasta "feature", deve ser processado o comando behave abaixo após aplicação estar no ar.
OBS: BDD está dentro do arquivo "pagamentos.feature"

#### behave appPagamentos/project/features/pagamentos.feature

# Evidência dos testes:

![image](https://github.com/user-attachments/assets/7eaee919-3db2-46e5-afe5-39f96c94f4ba)
