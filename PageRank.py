import re
import networkx as nx
#测试pagerank。py更改

import random
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
def compute_pagerank(graph, d=0.85, max_iter=100, tol=1e-6):
    # 计算PageRank值
    pagerank = nx.pagerank(graph, alpha=d, max_iter=max_iter, tol=tol)
    return pagerank

def adjust_initial_pagerank(graph, words, method="tfidf"):
    # 调整初始的PageRank值
    if method == "tfidf":
        # 使用TF-IDF调整初始PR值
        corpus = [' '.join(words)]  # 将所有单词组合成一个大文本（可以根据需求拆分成更细的部分）
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(corpus)
        feature_names = vectorizer.get_feature_names_out()

        # 获取每个单词的TF-IDF值
        tfidf_scores = tfidf_matrix.toarray().flatten()

        # 更新图的初始PR值
        initial_pr = {word: tfidf_scores[i] for i, word in enumerate(feature_names) if word in graph.nodes}

        return initial_pr
    else:
        return None

def display_pagerank(graph, pagerank):
    # 可视化PageRank值
    pos = nx.spring_layout(graph)  # 布局
    plt.figure(figsize=(12, 12))

    # 绘制图
    node_color = [pagerank[node] for node in graph.nodes]
    node_size = [pagerank[node] * 10000 for node in graph.nodes]  # 节点大小根据PR值调整

    nx.draw(graph, pos, with_labels=True, node_size=node_size, node_color=node_color, cmap=plt.cm.Blues, font_size=10, font_weight='bold')
    plt.title("PageRank of Words in the Text")
    plt.show()

def calPageRank(graph, words):
    # 用户输入阻尼因子
    d = float(input("Enter the damping factor (d) for PageRank (default is 0.85): ") or 0.85)

    # 计算PageRank值
    pagerank = compute_pagerank(graph, d)

    # 可选：调整初始PageRank值
    adjust_option = input("\nDo you want to adjust initial PageRank values using TF-IDF? (y/n): ")
    if adjust_option.lower() == 'y':
        initial_pr = adjust_initial_pagerank(graph, words)
        if initial_pr:
            print("Initial PageRank adjusted using TF-IDF.")
            # 更新Pagerank值
            for word in graph.nodes:
                pagerank[word] = pagerank.get(word, 0) + initial_pr.get(word, 0)

    # 展示PageRank值
    display_pagerank(graph, pagerank)