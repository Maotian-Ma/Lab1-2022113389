import re
import networkx as nx
import random
import matplotlib.pyplot as plt
#为B1修改Calculate.py

def find_shortest_path(graph, word1, word2):
    word1 = word1.lower()  # 转为小写
    word2 = word2.lower()  # 转为小写

    if word1 not in graph or word2 not in graph:
        print(f"No {word1} or {word2} in the graph!")
        return None, None

    # 使用Dijkstra算法计算最短路径
    try:
        path = nx.shortest_path(graph, source=word1, target=word2, weight='weight')
        path_length = sum(graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
        return path, path_length
    except nx.NetworkXNoPath:
        return None, None


def highlight_path_on_graph(graph, path):
    # 突出显示路径的节点和边
    pos = nx.spring_layout(graph)  # 布局
    plt.figure(figsize=(12, 12))

    # 绘制图
    node_color = ['lightblue' if node not in path else 'orange' for node in graph.nodes]
    edge_color = ['gray' if (u, v) not in zip(path, path[1:]) else 'red' for u, v in graph.edges]

    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color=node_color, font_size=10, font_weight='bold',
            edge_color=edge_color)
    plt.title(f"Graph with Shortest Path Highlighted")
    plt.show()


def display_all_shortest_paths(graph, word):
    word = word.lower()
    if word not in graph:
        print(f"No {word} in the graph!")
        return

    all_paths = {}
    for target in graph.nodes:
        if target != word:
            path, path_length = find_shortest_path(graph, word, target)
            if path:
                all_paths[target] = (path, path_length)

    for target, (path, path_length) in all_paths.items():
        print(f"Shortest path from {word} to {target}: {' -> '.join(path)} with length {path_length}")

def calcShortestPath(graph):
    # 查询最短路径
    word1 = input("\nEnter the first word to search for the shortest path: ").lower()
    word2 = input("Enter the second word to search for the shortest path: ").lower()
    path, path_length = find_shortest_path(graph, word1, word2)
    if path:
        print(f"The shortest path from {word1} to {word2} is: {' -> '.join(path)} with length {path_length}")
        highlight_path_on_graph(graph, path)
    else:
        print(f"No path found between {word1} and {word2}.")

        # 可选：显示该单词到所有其他单词的最短路径
    show_all_paths = input("\nDo you want to show shortest paths from one word to all other words? (y/n): ")
    if show_all_paths.lower() == 'y':
        word = input("Enter the word to compute shortest paths from: ").lower()
        display_all_shortest_paths(graph, word)