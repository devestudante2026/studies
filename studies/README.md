Uso este repositório como forma de documentar meu progresso na linguagem Python

Cada "pasta" (pacote) é um tema estudado e praticado, nelas, existem arquivos .py (módulos) com soluções de exercícios

Até o dia 15/04/2026 estes módulos não eram perfeitamente estruturados. Eu deixava-os separados por "nível de dificuldade" de exercícios
A partir de 16/04/2026 eles começaram a ser separados corretamentes, onde cada módulo é uma solução de exercício, um script apenas


Abaixo seguem os temas e exercícios relacionados, descritos com mais detalhes.


*args_kwargs (pasta pré reformulação do repositório)
	- Contem exercícios deste tema separados apenas pelo nívelde dificuldade. (foi o início da jornada)
	
*decorators
Do 01 ao 05 Nível Fácil: Decorators de 2 Níveis (Sem argumentos)
Foco: Entender o wrapper e a execução de funções.

Do 06 ao 10 Nível Intermediário: Decorators de 3 Níveis (Com argumentos)
Foco: Entender a "fábrica" de decorators e o fechamento de escopo (closures).

Do 11 ao 15 Nível Avançado: Casos Complexos e Arquitetura
Foco: Decorators em classes, preservação de metadados e lógica de negócio.

Exercício 01:
	O Mensageiro: Crie um decorator que apenas imprima "Iniciando função..." 
	antes da função decorada rodar e "Função finalizada!" depois.
	
Exercício 02:
	Conversor de Maiúsculas: Crie um decorator que pegue o retorno de uma 
	função (supondo que ela retorne uma string) e o transforme todo em letras maiúsculas.
	
Exercício 03:
	Dobrador de Valor: Crie um decorator que multiplique por 2 o resultado numérico de qualquer função decorada.
	
Exercício 04:
	Verificador de Tipo: Crie um decorator que verifique se os argumentos 
	passados para a função são todos do tipo int. Se não forem, imprima um aviso.

Exercício 05:
	Contador de Chamadas: Crie um decorator que conte quantas vezes uma função foi 
	executada durante a execução do programa e imprima esse valor a cada chamada.
	
Exercício 06:
	Multiplicador Genérico: Crie um decorator @multiplicar(n) que multiplique o 
	resultado da função por um valor n definido no decorator.
	
Exercício 07:
	Prefixo Personalizado: Crie um decorator @prefixo(texto) que adicione uma 
	string personalizada antes do retorno de uma função que retorna texto.

Exercício 08:
	Validador de Intervalo: Crie um decorator @entre(min, max) que verifique 
	se o resultado de uma função está dentro do intervalo permitido. 
	Se não estiver, retorne um erro ou um valor padrão.
	
Exercício 09:
	Atraso na Execução: Crie um decorator @delay(segundos) que faça o 
	programa "dormir" (time.sleep) pelo tempo especificado antes de executar a função.
	
Exercício 10:
	Tentativas de Execução: Crie um decorator @retry(n) que, se a função 
	decorada der um erro (exceção), tente executá-la novamente até n vezes antes de desistir.
	
Exercício 11:
	O Cache de Resultados (Memoização): Crie um decorator @cache que armazene o 
	resultado de uma função para determinados argumentos. Se a função for chamada 
	com os mesmos argumentos de novo, retorne o valor salvo sem processar a função original.
	
Exercício 12:
	Preservação de Identidade: Pesquise sobre functools.wraps e aplique-o em um decorator para 
	garantir que, ao dar um print(minha_funcao.__name__), o Python mostre o nome original da 
	função e não o nome "wrapper".
	
Exercício 13:
	Autenticação por Perfil: Crie um decorator @requer_perfil("admin") que receba um objeto 
	usuario como primeiro argumento da função e só a execute se o usuario.perfil for igual ao exigido.
	
Exercício 14:
	Limitador de Taxa (Rate Limiting): Crie um decorator @limite(max_chamadas=5) que 
	impeça uma função de ser executada mais do que X vezes em um curto período de tempo.
	
Exercício 15:
	Decorator de Classe: Crie um decorator que não seja uma função, mas sim uma Classe (usando o método __call__), 
	que registre o horário exato de cada chamada da função decorada em um arquivo .txt.
	

