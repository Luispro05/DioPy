def verificador_ano_bissexto():
    ano = int(input())
    if ano % 4 == 0 or ano % 400 == 0:
        print("Sim")
    else:
        print("Não")

    

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:


verificador_ano_bissexto()