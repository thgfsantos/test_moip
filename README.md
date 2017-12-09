# test_moip
Desenvolvimento de testes automatizados utilizando a linguagem Python com as bibliotecas requests e pytest para os seguintes endpoins: /customer; /orders; /payments

# Pré-requisitos
  Python >= 2.7.3
  
  pip >= 0.9
  
  requests >= 2.18
  
  pytest >= 3.3.1 (compatível com a versão 2.7.3 do python)
  
  json -- (built in)

# Instalação
Instalando o Python 2.7.3 no Ubuntu


  Instale as seguintes dependencias:
  
  sudo apt-get install build-essential checkinstall
  
  sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
  

  Fazer o download do Python 2.7
  wget https://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz

  tar -xvf Python-$version.tgz

  cd Python-$version

  Executar 
  
  ./configure
  
  make
  
  sudo checkinstall

# Instalando as bibliotecas do Python para usar nos Testes

  Instalando o pip (gerenciador para instalar as outras bibliotecas)
  
  sudo apt-get install python-pip

  Instalando a dependencia: requests
  
  Com pip instalado basta executar:
  
  pip install requests

  Instalando a dependencia: pytest
  
  pip install  pytest 

# Obtendo o projeto
  
  Em uma pasta executar o git clone do projeto

Ex: 
cd /tmp
git clone [url do projeto]

# Para executar os Testes

  Entrar na pasta onde o projeto se encontra e executar:
  python test_moip/exec_test_moip.py
Ex: 
cd /tmp
python test_moip/exec_test_moip.py

# Estrutura do Projeto
## Arquivo de Configuração

Neste arquivo encontra-se os ítens necessários de ambientes para utilização dos testes, como, host/port/endpoints.

  test_moip
    |--config
      |-- env (arquivo json)
    
 ## Classes Auxiliares

 test_moip
  |-- helper
    |--Customer.py - Cria o post/get com respectivos headers e com os devidos payloads para o endpoint de /customers.
    |--Payments.py - Cria o post/get com respectivos headers e com os devidos payloads para o endpoint de /payments.
    |--Orders.py - Cria o post/get com respectivos headers e com os devidos payloads para o endpoint de /orders.
    |--Config.py - Carrega o arquivo de configuração em config/env
 
 ## Desenvolvimento dos Testes

Desenvolvimento dos testes utilizando Python com request(dsl para requests http/https) e pytest(auxiliar na execução dos testes) e json para realizar os parses e navegar nas respostas obtidas dos POST/GET.
 
 test_moip
  |--test_customers.py - test cases para o endpoint de customers
  |--test_orders.py - test cases para o endpoint de orders
  |--test_paymentss.py - test cases para o endpoint de payments

## Execução dos Testes
test_moip
  |--exec_test_moip.py - Arquivos que contem os testes (test_customers.py/test_orders.py/test_payments.py) para execução. 
