from coisas import GameStore, Cliente, Game

# teste base
customer = Cliente("João", 150.00)
game1 = Game("The Witcher 3", 99.99)
game2 = Game("Cyberpunk 2077", 249.99)

loja = GameStore()
loja.adicionar_jogos(game1)
loja.adicionar_jogos(game2)

loja.vender_jogo(customer, "The Witcher 3")
loja.vender_jogo(customer, "Cyberpunk 2077")


