<h1> Desafio RPA </h1>

Este projeto foi criado para completar o desafio RPA do site https://rpachallenge.com/.

Objetivos:

<ul>
  <li>O robô deve preencher um formulário com dados de uma planilha.</li>
  <li>Os campos do formulário podem mudar de posição a cada rodada.</li>
  <li>O robô deve identificar corretamente os campos da planilha e do formulário.</li>
  <li>O robô deve gerar um arquivo de log da execução.</li>
</ul>

O que eu fiz:
<ul>
  <li>Validação de seletores: o robô valida os seletores dos campos do formulário para garantir que eles sejam encontrados corretamente.</li>
  <li>Busca dinâmica: o robô usa uma busca dinâmica para encontrar os campos do formulário, mesmo que eles mudem de posição.</li>
  <li>Sinalização de erros: o robô sinaliza erros para o usuário, caso ocorram.</li>
  <li>Geração de arquivo de log: o robô gera um arquivo de log da execução, que inclui informações sobre o progresso do robô e quaisquer erros que ocorreram.</li>
  <li>Código comentado e explicativo: o código está comentado e explicativo para facilitar o entendimento do funcionamento do robô.</li>
</ul>

Como executar:
<ol>
  <li>Instale as dependências: pip install -r requirementos.txt</li>
  <li>Execute o robô: python challenge.py</li>
</ol>

Para obter mais informações sobre o desafio RPA, visite o site https://rpachallenge.com/.
