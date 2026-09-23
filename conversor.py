import requests
from colorama import init, Fore, Style

init(autoreset=True) #autoreset Makes the colour come back to normal after each print

def converter_moeda(moeda_origem, moeda_destino, valor):
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{moeda_origem}.json"
    
    resposta = requests.get(url)
    dados = resposta.json()

    if moeda_origem not in dados:
        return None

    if moeda_destino not in dados[moeda_origem]:
        return None
    
    cotacao = dados[moeda_origem][moeda_destino]
    valor_convertido = valor * cotacao
    
    return valor_convertido


def mostrar_menu_moedas():
    print(Fore.CYAN + "\nMoedas populares:")
    print(Fore.CYAN + " usd - Dólar americano")
    print(Fore.CYAN + " eur - Euro")
    print(Fore.CYAN + " brl - Real brasileiro")
    print(Fore.CYAN + " gbp - Libra esterlina")
    print(Fore.CYAN + " jpy - Iene japonês")
    print(Fore.CYAN + " ars - Peso argentino")


# Programa principal
print(Fore.YELLOW + Style.BRIGHT + "=== Conversor de Moedas ===")
continuar = True

while continuar:
    mostrar_menu_moedas()
    moeda_origem = input("\nDigite a moeda de origem: ").lower().strip()
    moeda_destino = input("Digite a moeda de destino: ").lower().strip()

    try:
        valor = float(input("Digite o valor a converter: "))
    except ValueError:
        print("\n⚠️ Valor inválido! Digite apenas números (ex: 100 ou 99.50)")
        continue

    resultado = converter_moeda(moeda_origem, moeda_destino, valor)

    if resultado is None:
        print(Fore.RED + f"\n⚠️ Moeda inválida! Verifique se '{moeda_origem}' ou '{moeda_destino}' existem.")
    else:
        print(Fore.GREEN + f"\n✅ {valor} {moeda_origem.upper()} = {resultado:.2f} {moeda_destino.upper()}")

    resposta = input(Style.RESET_ALL + "\nDeseja fazer outra conversão? (s/n): ").lower().strip()
    if resposta != "s":
        continuar = False

print(Fore.YELLOW + "\nObrigado por usar o conversor!")