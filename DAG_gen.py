import re
import networkx as nx
import random
import matplotlib.pyplot as plt


def process_text(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 处理文本：移除非字母字符，换行符和回车符转换为空格
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # 替换非字母字符为空间
    text = text.replace('\n', ' ').replace('\r', ' ').lower()  # 换行符和回车符替换为空格

    # 分割为单词列表
    words = text.split()

    return words


def build_directed_graph(words):
    # 创建有向图
    graph = nx.DiGraph()

    # 构建图的邻接关系：单词与相邻单词之间有向边
    for i in range(len(words) - 1):
        word_a = words[i]
        word_b = words[i + 1]

        if graph.has_edge(word_a, word_b):
            graph[word_a][word_b]['weight'] += 1  # 增加边的权重
        else:
            graph.add_edge(word_a, word_b, weight=1)  # 添加边，权重为1

    return graph

def display_graph_cli(graph):
    print("Directed Graph Representation (CLI):")
    for node in graph.nodes:
        # 输出每个节点及其相邻的节点和边的权重
        print(f"\nNode '{node}' has edges to:")
        for neighbor in graph.neighbors(node):
            weight = graph[node][neighbor]['weight']
            print(f"  -> '{neighbor}' with weight {weight}")


def save_graph_image(graph, filename="graph.png"):
    # 可视化并保存图形
    pos = nx.spring_layout(graph)  # 布局
    plt.figure(figsize=(12, 12))
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold',
            edge_color='gray')
    plt.title("Directed Graph of Words in Text")

    # 保存为文件
    plt.savefig(filename)
    print(f"\nGraph image saved as '{filename}'")


def showDirectedGraph():
    # 用户输入文件路径
    file_path = input("Enter the path to the text file: ")

    # 处理文本并构建有向图
    words = process_text(file_path)
    graph = build_directed_graph(words)

    # 在CLI展示有向图
    display_graph_cli(graph)

    # 可选：保存图形文件
    save_option = input("\nDo you want to save the graph as an image file? (y/n): ")
    if save_option.lower() == 'y':
        file_name = input("Enter the file name to save (default: graph.png): ")
        if not file_name:
            file_name = "graph.png"
        save_graph_image(graph, file_name)

    return graph, words
