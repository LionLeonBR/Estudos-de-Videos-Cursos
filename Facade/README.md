# Documentação do GameStore (Padrão Facade)

## Visão Geral

Este projeto implementa um sistema simples de loja de jogos, seguindo o padrão de projeto **Facade**. A ideia do padrão Facade é fornecer uma interface simples e unificada para interagir com sistemas complexos. Neste caso, a classe `GameStore` funciona como a fachada que facilita a interação entre o cliente e os jogos disponíveis, ocultando os detalhes internos e complexos, como a verificação de saldo e a compra de jogos.

### Estrutura do Projeto

---

### 1. `Game`
Representa um jogo com nome e preço. Este é um dos componentes que a `GameStore` gerencia.

#### **Atributos**:
- `nome` (str): Nome do jogo.
- `preco` (float): Preço do jogo.

#### **Métodos**:
- `__init__(nome: str, preco: float)`: Inicializa um novo objeto `Game`.

---

### 2. `Cliente`
Representa um cliente com nome e saldo. Ele interage com a `GameStore` para comprar jogos.

#### **Atributos**:
- `nome` (str): Nome do cliente.
- `saldo` (float): Saldo disponível na conta do cliente.

#### **Métodos**:
- `__init__(nome: str, saldo: float)`: Inicializa um novo cliente.
- `pode_comprar(jogo: Game) -> bool`: Verifica se o cliente tem saldo suficiente para comprar um jogo.
- `comprar(jogo: Game)`: Efetua a compra do jogo, reduzindo o saldo do cliente.

---

### 3. `GameStore`
Esta é a classe que segue o padrão **Facade**, oferecendo uma interface simples para o cliente adquirir jogos sem precisar lidar com detalhes complexos de compra.

#### **Atributos**:
- `jogos` (List[Game]): Lista de jogos disponíveis na loja.

#### **Métodos**:
- `__init__()`: Inicializa a loja com uma lista vazia de jogos.
- `adicionar_jogos(jogo: Game)`: Adiciona um novo jogo à loja.
- `vender_jogo(cliente: Cliente, jogo_n: str)`: Simplifica o processo de venda, permitindo que o cliente compre um jogo pelo nome, gerenciando a lógica de busca e transação.

---

## Como Funciona o Padrão Facade

A `GameStore` atua como a fachada que simplifica as interações. Em vez de o cliente precisar entender como os jogos são armazenados ou como verificar seu saldo, ele apenas interage com a loja por meio de métodos simples como `vender_jogo`. A `GameStore` abstrai a complexidade de verificar se o jogo existe e se o cliente pode comprá-lo.

### Exemplo de Uso

#### Arquivo 1: `coisas.py`

```python
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
            print(f"Saldo insuficiente! Seu saldo é de: {self.saldo:.2f} e o valor do jogo é de: {jogo.preco:.2f}")

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
```

#### Arquivo 2: `main.py`

```python
from coisas import GameStore, Cliente, Game

# Teste básico
customer = Cliente("João", 150.00)
game1 = Game("The Witcher 3", 99.99)
game2 = Game("Cyberpunk 2077", 249.99)

loja = GameStore()
loja.adicionar_jogos(game1)
loja.adicionar_jogos(game2)

# João tenta comprar os jogos
loja.vender_jogo(customer, "The Witcher 3")    # Compra bem-sucedida
loja.vender_jogo(customer, "

Cyberpunk 2077")   # Saldo insuficiente
```

### Exemplo de Saída

```plaintext
João comprou o jogo: The Witcher 3 por: 99.99! Seu saldo atual é:50.01
Saldo insuficiente! Seu saldo é de: 50.01 e o valor do jogo é de: 249.99
```

## Como o Facade Facilita o Uso

Neste exemplo, a classe `GameStore` age como uma interface simplificada para as operações complexas. O cliente não precisa saber como os jogos são armazenados ou como o saldo é verificado — basta interagir com a fachada, que cuida de todos esses detalhes. Isso facilita a manutenção e o uso do código, mantendo o cliente e os jogos desacoplados da lógica interna de transação.

## Requisitos

- Python 3.6+

### Possíveis Expansões

- Implementar uma lista de compras do cliente.
- Adicionar descontos e promoções.
- Permitir que o cliente visualize os jogos disponíveis antes de comprar.

Com o padrão Facade, essas expansões podem ser facilmente integradas sem modificar a interface simples fornecida pela `GameStore`.
