import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo
G = nx.Graph()

# Adicionando componentes eletrônicos como nós
componentes = ['Resistor', 'Capacitor', 'Transistor', 'Diodo', 'Fonte de Energia', 'Amplificador']
G.add_nodes_from(componentes)

# Adicionando arestas com pesos (custos de conexão)
edges_with_weights = [
    ('Resistor', 'Capacitor', {'tipo': 'conexão', 'resistência': 3}),
    ('Resistor', 'Transistor', {'tipo': 'conexão', 'resistência': 2}),
    ('Capacitor', 'Transistor', {'tipo': 'conexão', 'resistência': 4}),
    ('Transistor', 'Diodo', {'tipo': 'conexão', 'resistência': 5}),
    ('Fonte de Energia', 'Resistor', {'tipo': 'alimentação', 'resistência': 1}),
    ('Fonte de Energia', 'Amplificador', {'tipo': 'alimentação', 'resistência': 2}),
    ('Amplificador', 'Transistor', {'tipo': 'sinal', 'resistência': 3}),
    ('Amplificador', 'Diodo', {'tipo': 'sinal', 'resistência': 4}),
]

G.add_edges_from(edges_with_weights)

# Visualizando o grafo
pos = nx.spring_layout(G)  # Layout para posicionar os nós
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
labels = nx.get_edge_attributes(G, 'resistência')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo Representando Componentes Eletrônicos e Conexões')
plt.show()

# Algoritmo de Kruskal para encontrar a Árvore de Abrangência Mínima (MST)
MST = nx.minimum_spanning_tree(G)

# Visualizando a Árvore de Abrangência Mínima (MST)
plt.figure()
pos = nx.spring_layout(MST)
nx.draw(MST, pos, with_labels=True, node_color='lightgreen', font_weight='bold')
labels = nx.get_edge_attributes(MST, 'resistência')
nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels)
plt.title('Árvore de Abrangência Mínima (MST) usando Kruskal para Design de Circuitos Eletrônicos')
plt.show()
