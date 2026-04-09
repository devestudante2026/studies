"""Nível Intermediário (Lógica)
4- Multiplicador Flexível: Crie uma função que receba um número multiplicador fixo 
e uma lista variável de números (*args). Retorne uma lista com todos os números 
multiplicados pelo primeiro parâmetro.

5- Filtro de Strings: Crie uma função que aceite *args e retorne apenas as strings que possuem mais de 5 caracteres.

6- Gerador de Tags HTML: Crie uma função tag_html(nome_tag, conteudo, **attrs). 
Ela deve retornar uma string como <p class="texto" id="p1">Conteúdo</p>. Os atributos dentro da tag vêm do **kwargs.

7- Concatenação com Separador: Crie uma função que receba um caractere separador (keyword-only) e vários textos (*args). 
Ela deve juntar todos os textos usando esse separador."""

#Exercício 4:
def multiplicador(num_fixo, *args):
    multiplicados = []
    for num in args:
        resultado = num_fixo * num
        multiplicados.append(resultado)
    return multiplicados

#esta função abaixo é a mesma da de cima só que mais "enxuta" digamos assim
def multiplicator(n, *args):
    new_list = [x * n for x in args]
    return new_list

lista_nums = [1, 2, 3, 4, 5, 6, 7]
mult = 5

print(multiplicator(mult, *lista_nums))
print(multiplicador(mult, *lista_nums))


#Exercício 5:
def str_filter(*args):
    big_words = []
    for word in args:
        if len(word) > 5:
            big_words.append(word)
    return big_words

#a mesma função de cima, só que usando list copmrehension
def str_filter_aprimorated(*args):
    bigger_words = [big_word for big_word in args if len(big_word) > 5]
    return bigger_words

words = ["carro", "elefante", "rinoceronte", "abelha", "futebol", "bola", "casa"]

print(str_filter(*words))
print(str_filter_aprimorated(*words))


#Exercício 6:
def tag_html(nome_tag, conteudo, **attrs):
    atributos = []
    for atributo, valor in attrs.items():
        atributo_formatado = f'{atributo}="{valor}"'
        atributos.append(atributo_formatado)

        string_atributos = " ".join(atributos)

        if string_atributos:
            string_atributos = " " + string_atributos
            
    return f"<{nome_tag}{string_atributos}>{conteudo}</{nome_tag}>"    

# def OKtag_html(nome_tag, conteudo, **attrs):
#     atributos_lista = []
    
#     for chave, valor in attrs.items():
#         # HTML usa o padrão chave="valor"
#         # Usamos aspas simples por fora para poder usar aspas duplas dentro
#         formatado = f'{chave}="{valor}"'
#         atributos_lista.append(formatado)
    
#     # Juntamos a lista em uma string separada por espaços
#     string_atributos = " ".join(atributos_lista)
    
#     # Se houver atributos, adicionamos um espaço antes deles para não grudar no nome da tag
#     if string_atributos:
#         string_atributos = " " + string_atributos

#     return f"<{nome_tag}{string_atributos}>{conteudo}</{nome_tag}>"

    
print(tag_html("p", "nada a declarar", classe="texto", id="p1"))