from model.restaurante import Restaurante
from model.menu.prato import Prato
from model.menu.bebida import Bebida


restaurante_praca = Restaurante("Restaurante da Praça", "Brasileira")
bebida_suco = Bebida("Suco de Maça", 10.0, "500ml")
prato_pizza = Prato("Pizza", 25.0, "Pizza de calabresa com borda recheada")

bebida_suco.aplicar_desconto()
prato_pizza.aplicar_desconto()

restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_pizza)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == "__main__":
    main()