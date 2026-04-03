import networkx as nx
import matplotlib.pyplot as plt

# 육각형 구조(Triangular Lattice Graph) 생성
# 육각형 셀의 인접 관계는 수학적으로 '삼각 격자 그래프'와 동형입니다.
G = nx.triangular_lattice_graph(3, 4)

# 색칠 알고리즘 적용 (Greedy Coloring)
# 인접한 노드끼리 다른 색을 갖도록 함
coloring = nx.greedy_color(G, strategy='largest_first')

# 색상 매핑 (0, 1, 2 -> Red, Blue, Green)
colors = ['red', 'blue', 'green', 'orange']
node_colors = [colors[coloring[n] % 4] for n in G.nodes()]

plt.figure(figsize=(6, 5))
pos = nx.get_node_attributes(G, 'pos')

# 노드(기지국) 그리기
nx.draw(G, pos, node_color=node_colors, with_labels=False, 
        node_size=800, edge_color='gray', width=2)

plt.title("[Fig 5] Frequency Reuse in Cellular Network")
plt.axis('equal')
plt.axis('off')
plt.show()