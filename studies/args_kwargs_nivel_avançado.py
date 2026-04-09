"""Nível Avançado (Manipulação de Dados)
8- Calculadora de Notas: Crie uma função que receba o nome do aluno e várias notas via *args. 
Calcule a média e retorne um dicionário contendo o nome, as notas e se ele foi aprovado (média >= 7).

9- Validador de Cadastro: Crie uma função que receba dados de um usuário via **kwargs. 
Se faltarem as chaves "email" ou "id", a função deve retornar um erro. Caso contrário, retorna "Cadastro válido".

10- O "Pass-through" (Decorador Simples): Crie uma função chamada log_execucao(funcao, *args, **kwargs). 
Ela deve imprimir "Executando função...", chamar a função passada com todos os argumentos fornecidos e retornar o resultado dessa função."""


#Exercício 8:
def calc_notas(nome_aluno, *args):
    media = sum(args)/len(args)
    if media >= 7:
        aprovado = "Sim"
    else:
        aprovado = "Não"
    dados_aluno = {
            "nome" : nome_aluno,
            # "Notas" : [nota for nota in args], #esta era como eu tinha feito antes 
            "notas" : list(args), #esta é a forma sugerida pela IA
            "aprovado" : aprovado,
            # "Média" : f"{media:.2f}" #maneira que eu havia feito antes;
            "media" : round(media, 2)     
            }  
    # return dados_aluno #assim era como era retornado a função, mas achei melhor retornar a fstring abaixo para não ter que ficar formatando os prints
    return f"Aluno(a): {dados_aluno['nome']}\nMédia: {dados_aluno['media']}\nStatus: {dados_aluno['aprovado']}\nNotas: {dados_aluno['notas']}"

# aluno = calc_notas("Jubiscreide", 9, 7, 6, 6.8)
# print(f"Aluno(a): {aluno['nome']}\nMédia: {aluno['media']}\nStatus: {aluno['aprovado']}\nNotas: {aluno['notas']}")
print(calc_notas("Eu", 10, 4, 7, 8))


#Exercício 9:
def valida_cadastro(**kwargs):
    if "email" not in kwargs or "id" not in kwargs:
        # print("erro") #assim eu havia feito;
        return False, "Erro: Faltam campos obrigatórios"
    else:
        # print("Cadastro válido") #igual a comentada acima
        return True, "Cadastro válido"


print(valida_cadastro(teste="nome", email="nome@email.com", idade=41, id=18385))


#Exercício 10:
def log_execucao(funcao, *args, **kwargs):
    print(f"- Iniciando execução da faunção: {funcao.__name__} - ")
    resultado = funcao(*args, **kwargs)
    print(f"- Execução finalizada com sucesso -")
    return resultado

