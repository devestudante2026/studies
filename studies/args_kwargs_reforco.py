"""1. Formatador de Endereços (kwargs + strings)
Muitos sistemas de prefeitura ou fiscais recebem endereços picados. 
Crie uma função formatar_endereco(logradouro, numero, **kwargs) que:

Receba obrigatoriamente a rua e o número.

Receba via **kwargs informações como bairro, cidade, estado e cep.

Retorne uma string única bem formatada. Se o bairro existir, ele deve aparecer, se não, deve ser ignorado.

Exemplo de saída: "Rua XV de Novembro, 100 - Bairro: Centro - Guaíra/SP"""

def formatador_enderecos(logradouro, numero, **kwargs):
    # if "rua" not in kwargs or "numero" not in kwargs:
    #     return False, "Faltam parametros obrigatórios rua/numero"
    return f"{str(logradouro).title()}, {numero} - Bairro: {str(kwargs.get("bairro", "-")).title()} - {str(kwargs.get("cidade", "-")).title()}/{str(kwargs.get("estado", "-")).upper()} - CEP: {str(kwargs.get("cep", "-"))[:5] + "-" + str(kwargs.get("cep", "-"))[5:]}"

print(formatador_enderecos("orbis clube", "44", cidade="guaira", estado="sp", bairro="jardim palmares", cep=14790010))



"""2. Validador de Tipos de Dados (*args)
Crie uma função apenas_numeros(*args) que receba vários argumentos de qualquer tipo 
(strings, ints, floats, booleans). 
A função deve retornar uma nova lista contendo apenas os números (int e float) que foram passados.

Dica: Use a função isinstance(item, (int, float))."""

def apenas_numeros(*args):
    numeros = [numero for numero in args if isinstance(numero, (int, float))]
    return numeros

lista_nums = apenas_numeros("pedra", "papel", 144, 10.8, True, "35", "A10")

print(lista_nums)


"""3. Gerador de Query String (kwargs)
Em URLs de sistemas web, usamos "query strings" como ?usuario=admin&setor=fiscal. 
Crie uma função gerar_url_busca(base_url, **filtros) 
que pegue a URL base e anexe os filtros passados no **kwargs seguindo o padrão &chave=valor.

Exemplo: gerar_url_busca("www.guaira.sp.gov.br", tributo="iptu", ano=2024)

Saída: "www.guaira.sp.gov.br?tributo=iptu&ano=2024"""

def gerar_url_busca(base_url, **filtros):
    lista_filtros = [f"{k}={v}" for k,v in filtros.items()]
    string_unificada_filtros = "&".join(lista_filtros)
    return f"{base_url}?{string_unificada_filtros}"

print(gerar_url_busca("www.google.com", tributo="iptu", ano="2026"))