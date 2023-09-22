from prettytable.colortable import ColorTable, Themes
import time
import art
x = ColorTable(theme=Themes.OCEAN)
x.field_names = ["Razão","Valor"]

def checar_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")
        
    

contador = 0
desligar = False

print(art.logo)
print(f"\nSeja bem-vindo à calculadora de perdas")
time.sleep(2)
while True:

    '''ganhos'''
    while not desligar:
        somar = checar_numero("Diga um valor de ganho: ")
        contador += somar
        origem = input("Diga a origem: ")
        x.add_row([f"{origem}", f"+ {somar}"])
        sair = input("Acabou? ")
        print("\n")
        if sair == "sim" or sair == "s":
            desligar = True
    desligar = False
    '''Perdas'''
    while not desligar:
        somar = checar_numero("Diga um valor de custo: ")
        origem = input("Diga a origem: ")
        contador -= somar
        x.add_row([f"{origem}", f"- {somar}"])
        sair = input("Acabou? ")
        print("\n")
        if sair == "sim" or sair == "s":
            desligar = True
    '''Reset e gráfico'''
    print(x)
    desligar = False
    finalizar = input("Deseja sair? ")
    if finalizar == "sim" or finalizar == "s":
        print("Vou calcular o total...")
        time.sleep(3)
        x.add_row(["TOTAL", contador])
        print(x)
        time.sleep(15)
        break
    print("\n ")
    
print("banana")