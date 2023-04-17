<h1 align="center"> Aplicação MQTT </h1>

<p>Esse projeto foi criado para simular a transferência de dados entre clientes de uma aplicação MQTT.</p>

<h2>Conteúdos</h2>
  <ul>
    <li><a href="#Aplicação">Aplicação</a></li>
    <li><a href="#Utilização">Utilização</a></li>
     <li><a href="#Tecnologias Utilizadas">Tecnologias Utilizadas</a></li>
  </ul>

<h2>Aplicação</h2>
  <p>O sistema criado simula uma possível transmissão de dados entre componentes de uma máquina AVAC (Ar-condicionado, Ventilação e Aquecimento). Ela possui um módulo de aquecimento do ar por resistências elétricas, um módulo de resfriamento por válvulas de água fria e um ventilador para a movimentação das massas de ar que serão distribuídas ao ambiente. No duto de distribuição, existe um sensor de temperatura e um de pressão para o controle das funcionalidades da máquina. Eles emitem, respectivamente, medições de temperatura – necessárias para o controle do acionamento das resistências aquecedoras e das válvulas de água fria – e medições de pressão – necessárias para o controle da velocidade de rotação do ventilador.</p>
  <p>O modelo de comunicação utilizado é o MQTT. Os publishers são os sensores de pressão e temperatura, que fazem a leitura de suas variáveis e enviam aos respectivos tópicos hospedados no broker. O broker utilizado é o Mosquitto. Os subscribers são os componentes que atuam sobre a massa de ar movimentada pela máquina e que precisam das variáveis obtidas pelos sensores para funcionar. O ventilador está inscrito no tópico pressão e as resistências e válvulas estão inscritas no tópico temperatura. Os códigos de cada um dos componentes foram desenvolvidos em Python.</p>
  
<h2>Utilização</h2>
   <p>É necessário instalar e rodar um servidor Mosquitto e ativar os clientes Python.</p>  

<h2>Tecnologias Utilizadas</h2>
<ul>
  <li>Python</li>
  <li>Mosquitto</li>
  <li>Paho MQTT</li>
</ul>

<h2>Exemplo de Funcionamento</h2>
  <img src="https://user-images.githubusercontent.com/129123498/232361826-937e96a1-8a20-4997-9c33-37b5c9656f16.png" alt="Programa sendo executado">
