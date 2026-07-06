from model.restaurante import Restaurante

restaurante_praca = Restaurante("Restaurante da Praça", "Brasileira")

restaurante_praca.receber_avaliacao("João", 5)
restaurante_praca.receber_avaliacao("Maria", 4)
restaurante_praca.receber_avaliacao("Pedro", 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
