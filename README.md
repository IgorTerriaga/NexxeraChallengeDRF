# NexxeraChallengeDRF
Desafio proposto pela empresa Nexxera uitlizando Python3 e DRF

Neste desafio utilizei o DRF, python3 e o banco de dados sqlite para facilitar os testes.

Assista esse pequeno vídeo de 5 min e veja a demonstração:  https://www.loom.com/share/e18c6b1c2782475caa7f2d77061800fa

Para executar o projeto:

1 - Clone o repo e acesse a pasta dele

2 - Instale as dependências com -> pip3 install -r requirements.txt

3 - Faça as migrações! -> pyhon3 manage.py migrate

4 - Execute o projeto. -> python3 manage.py runserver

5 - Vá até seu navegador e digite localhost:8000 na barra de busca

Os recursos são:

  # Criar uma conta
  # Realizar um débito
  # Realizar um crédito
  # Exibir extrato (chamei de transacoes)
  # Filtar conta por titular
  # Filtrar transacoes por datas (range)

O que faltou  que ficaria bacana ter: 
  # Testes unitários
  # Utlizar a lib decouple para usar o 'config' e esconder as variaveis de ambiente
  # Mais validações de campos
  # Usar um BD na nuvem
  # Remover do input o saldo inicial e final, mesmo não sendo obrigatório/necessário passar.
