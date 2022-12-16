from time import sleep

#Para efeito de multiplicação digitar *

def chamarReagentes():

    listaReagentes = []

    print("AVISOS")
    sleep(1.2)
    print("DIGITAR APENAS A PARTE DOS REAGENTES")
    sleep(1.2)
    print("PARA CASOS DE MULTIPLICAÇÃO, UTILIZAR * PARA INFORMAR A MULTIPLICAÇÃO")
    sleep(1.2)

    print("Digite o primeiro Reagente. Considere digitar como já equilibrado - Exemplo: 2H2")
    print("Aviso - Para casos de multiplicação, digitar o valor já multiplicado. Exemplo: 2(H2 + O2) -> 2H2 e 2O2")

    reagente = input("Digite o reagente: ")
    listaReagentes.append(reagente)

    resposta = input("Existe mais algum reagente? (S / N)").lower()

    while resposta == "s":
        reagente = input("Digite o reagente: ")
        listaReagentes.append(reagente)

        resposta = input("Existe mais algum reagente? (S / N)").lower()

    print("Reagentes Finalizados")

    listValoresReagentes = []

    for reagentes in listaReagentes:
        
        valor = float(input(f"Digite o valor do reagente {reagentes}: "))
        listValoresReagentes.append(valor)

    return [listValoresReagentes, listaReagentes]




def chamarProdutos():

    listProdutos = []

    print("AVISOS")
    sleep(1.2)
    print("DIGITAR APENAS A PARTE DOS PRODUTOS")
    sleep(1.2)
    print("PARA CASOS DE MULTIPLICAÇÃO, UTILIZAR * PARA INFORMAR A MULTIPLICAÇÃO")
    sleep(1.2)

    print("Digite o primeiro Produto. Considere digitar como já equilibrado - Exemplo: 2H2")
    print("Aviso - Para casos de multiplicação, digitar o valor já multiplicado. Exemplo: 2(H2 + O2) -> 2H2 e 2O2")

    produto = input("Digite o Produto: ")
    listProdutos.append(produto)

    resposta = input("Existe mais algum produto? (S / N)").lower()

    while resposta == "s":
        produto = input("Digite o Produto: ")
        listProdutos.append(produto)

        resposta = input("Existe mais algum produto? (S / N)").lower()

    print("Reagentes Finalizados")

    listValoresProdutos = []

    for reagentes in listProdutos:
        
        valor = float(input(f"Digite o valor do produto {reagentes}: "))
        listValoresProdutos.append(valor)

    return [listValoresProdutos, listProdutos]


def main():
    # Declaração de Variáveis Estatícas
    tipoCombustivel = "CH4"
    umidadeAr = 0.6
    pEntradaAr = 1
    tEntradaAr = 298.15 #KELVIN
    tSaida = 800
    tCombustivel = 870.0
    taxaCalorPerdido = 512.56
    vazaoAr = 67.5
    vExcessoAr = 1.8

    PRESSAO_AMBIENTE = 101.325
    TEMPERATURA_ENTRADA = 298.15
    DPE = 0.9810 #PERDA DE PRESSÃO NO DUTO DE ENTRADA
    VAZAO_MASSA = 67.5
    NGG = 100.0
    RAZAO_PRESSAO = 17.9
    

    #Declarar Variável
    vazaoCombusivel = float(input("Digite a vazão do combustível: "))

    #Formula de Entropia
    print("Preparando a fórmula de entropia")
    sleep(1.5)

    entReagentes = chamarReagentes()
    entProdutos = chamarProdutos()



if __name__ == "__main__":
    main()