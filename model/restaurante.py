from model.avaliacao import Avaliacao
from model.menu.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False 
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) 

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}"
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f"{restaurante.nome} - {restaurante.categoria} - Ativo: {restaurante.ativo}, Avaliacão Média: {restaurante.media_avaliacao}")
    
    @property
    def ativo(self):
        return "verdadeiro" if self._ativo else "falso"
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        total = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(total / len(self._avaliacao), 1)
    
    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        if not self._cardapio:
            print("Cardápio vazio.")
        else:
            print(f"Cardápio do {self.nome}:")
            for item in self._cardapio:
                print(f"- {item._nome} - R${item._preco:.2f}")
                if hasattr(item, 'descricao'):
                    print(f"  Descrição: {item.descricao}")
                else:
                    print(f"  Tamanho: {item.tamanho}")