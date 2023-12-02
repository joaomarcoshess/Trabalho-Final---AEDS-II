from dados_criptomoedas import dados  # Importa os dados das criptomoedas
import networkx as nx
import matplotlib.pyplot as plt

class GrafoCriptomoedas:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def add_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    def encontrar(self, subset, i):
        if subset[i] == -1:
            return i
        return self.encontrar(subset, subset[i])

    def unir(self, subset, x, y):
        x_raiz = self.encontrar(subset, x)
        y_raiz = self.encontrar(subset, y)
        subset[x_raiz] = y_raiz

    def kruskal(self):
        resultado = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        subset = [-1] * self.V

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(subset, u)
            y = self.encontrar(subset, v)

            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                self.unir(subset, x, y)

        return resultado

# Criando o grafo com os dados das criptomoedas
num_criptos = len(dados)
grafo_cripto = GrafoCriptomoedas(num_criptos)

# Adicionando as arestas com base na diferença percentual dos valores de mercado das criptomoedas
for i in range(num_criptos):
    for j in range(i + 1, num_criptos):
        moeda1 = dados[i]
        moeda2 = dados[j]

        nome_moeda1, valor_mercado1, mudanca_24h_1, _, _, _, _ = moeda1
        nome_moeda2, valor_mercado2, mudanca_24h_2, _, _, _, _ = moeda2

        peso_aresta = abs((valor_mercado1 - valor_mercado2) / valor_mercado1) * 100
        grafo_cripto.add_aresta(i, j, peso_aresta)

resultado_kruskal = grafo_cripto.kruskal()

# Cria um grafo do NetworkX para visualização
G = nx.Graph()

# Adiciona as arestas e nós ao grafo do NetworkX
for u, v, peso in resultado_kruskal:
    nome_u, _, _, _, _, _, _ = dados[u]
    nome_v, _, _, _, _, _, _ = dados[v]
    G.add_edge(nome_u, nome_v, weight=peso)

# Define o layout do grafo e plota
pos = nx.spring_layout(G, seed=42)  # Definindo uma semente para a disposição dos nós
plt.figure(figsize=(12, 10))  # Ajustando o tamanho da figura

# Desenha os nós com bordas e cor azul clara
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1200, node_color='skyblue', font_size=10, edgecolors='black')

# Adiciona labels para as arestas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('Árvore Geradora Mínima das Criptomoedas')
plt.show()
