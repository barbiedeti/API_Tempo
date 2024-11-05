# Clima e Tempo com API


Weather Information API

Este é um script em Python que consulta a API do OpenWeatherMap para obter informações climáticas sobre uma cidade específica e exibe detalhes como temperatura, sensação térmica, umidade, clima geral, horário do nascer e do pôr do sol. A cidade padrão é “Natal”.

Funcionalidades

	•	Consulta a temperatura e a sensação térmica em graus Celsius.
	•	Exibe a umidade e uma descrição do clima atual.
	•	Informa o horário do nascer e pôr do sol, considerando o fuso horário local da cidade consultada.

Pré-requisitos

	•	Python 3
	•	Biblioteca requests para requisições HTTP (para instalar, use pip install requests)

Como Usar

	1.	Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git


	2.	Acesse o diretório do projeto:

cd seu-repositorio


	3.	Substitua API_KEY no código pelo seu OpenWeatherMap API Key.
	4.	Execute o script:

python nome_do_arquivo.py


	5.	O script exibirá os dados climáticos no console. Exemplo de saída:

Temperatura em Natal: 27°C
Sensação térmica em Natal: 29°C
Umidade em Natal: 70%
Clima Geral em Natal: Nublado
Nascer do Sol em Natal: 05:34
Pôr do Sol em Natal: 17:46



Personalização

Para consultar o clima de outra cidade, modifique a variável CITY no código:

CITY = "Nova Cidade"

Estrutura do Código

	•	Função kelvin_to_celsius: Converte a temperatura de Kelvin para Celsius.
	•	Requisição à API: Utiliza a biblioteca requests para enviar uma requisição GET à API do OpenWeatherMap.
	•	Tratamento de Resposta: Extrai as informações do JSON retornado pela API e as formata para exibição.

Dependências

	•	Requests: Biblioteca para requisições HTTP.

Instale com:

pip install requests

Licença

Este projeto é de uso livre. Sinta-se à vontade para utilizá-lo e modificar conforme necessário.
