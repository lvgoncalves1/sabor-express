# Sistema de Restaurantes - Estudo POO 🍽️

Um pequeno projeto desenvolvido em Python com o objetivo de praticar e consolidar conceitos de Programação Orientada a Objetos (POO).

## 📌 O que foi praticado
Este código foca na modelagem de classes e na interação entre elas, utilizando:
* **Classes e Objetos:** Criação da classe `Restaurante` e `Avaliacao`.
* **Métodos de Classe (`@classmethod`):** Para gerenciar a lista de todos os restaurantes instanciados.
* **Properties (`@property`):** Para formatar a exibição do status (ativo/falso) e calcular a média das avaliações em tempo real.
* **Encapsulamento:** Uso de atributos protegidos (como `_ativo` e `_avaliacao`).

## 🛠️ Estrutura do Projeto
* `app.py`: Arquivo principal para executar o programa.
* `model/restaurante.py`: Contém a classe `Restaurante` e suas regras de negócio.
* `model/avaliacao.py`: Contém a classe `Avaliacao` para registrar as notas dos clientes.

## 🚀 Como executar

Certifique-se de ter o Python instalado na sua máquina. Pelo terminal, navegue até a pasta raiz do projeto e execute o arquivo principal:

```bash
python app.py