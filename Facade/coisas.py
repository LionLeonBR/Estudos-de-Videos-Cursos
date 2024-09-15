from typing import List

class Game():
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

class Cliente():
    def __init__(self, nome: str, saldo: float) -> None:
        self.nome = nome
        self.saldo = saldo
    def pode_comprar(self, jogo: Game) -> bool:
        return self.saldo >= jogo.preco
    
    def comprar(self, jogo: Game):
        if self.pode_comprar(jogo):
            self.saldo -= jogo.preco
            print(f"{self.nome} comprou o jogo: {jogo.nome} por: {jogo.preco:.2f}! Seu saldo atual é:{self.saldo:.2f}")
        else:
            print(f"Saldo insuficiente! seu saldo é de: {self.saldo:.2f} e o valor do jogo é de: {jogo.preco}")


class GameStore():
    def __init__(self) -> None:
        self.jogos = []

    def adicionar_jogos(self, jogo: Game):
        self.jogos.append(jogo)

    def vender_jogo(self, cliente: Cliente, jogo_n: str):
        jogo = next((g for g in self.jogos if g.nome == jogo_n), None)
        if jogo:
            cliente.comprar(jogo)
        else:
            print(f"Nenhum jogo com o nome {jogo_n} foi encontrado.")
    