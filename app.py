from model.restaurante import Restaurante

restaurante_praca = Restaurante("Restaurante da Praça", "Brasileira")


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()