import re
import networkx as nx
import random
import matplotlib.pyplot as plt
#为B1修改bridge_word.py
from DAG_gen import save_graph_image


def _queryBridgeWords(graph, word1, word2):
    if word1 not in graph or word2 not in graph:
        print(f"No \"{word1}\" or \"{word2}\" in the graph!")
        return []

    # 查找所有桥接词：word1 -> word3 -> word2
    bridge_words = []
    for word3 in graph.nodes:
        if graph.has_edge(word1, word3) and graph.has_edge(word3, word2):
            bridge_words.append(word3)
    if len(bridge_words) == 0:
        print("No bridge words from word1 to word2!")
    return bridge_words


def generate_text_with_bridge_words(graph, new_text):
    words = new_text.split()
    new_words = []

    for i in range(len(words) - 1):
        word1 = words[i].lower()
        word2 = words[i + 1].lower()

        bridge_words = _queryBridgeWords(graph, word1, word2)

        # 如果存在桥接词，随机选择一个并插入
        if bridge_words:
            bridge_word = random.choice(bridge_words)
            new_words.append(word1)
            new_words.append(bridge_word)
        else:
            new_words.append(word1)

    # 添加最后一个单词
    new_words.append(words[-1])

    # 输出生成的新文本
    return " ".join(new_words)


def queryBridgeWords(graph):
    word1 = input("Input first word: ")
    word2 = input("Input second word: ")
    bridge_words = _queryBridgeWords(graph, word1, word2)
    if len(bridge_words) != 0:
        print(f"The bridge words from \"{word1}\" to \"{word2}\" are: " + ", ".join(bridge_words))
    return bridge_words

def generateNewText(graph):
    # 生成新文本并展示
    new_text = input("\nEnter a new sentence: ")
    new_text_with_bridge_words = generate_text_with_bridge_words(graph, new_text)
    print(f"Generated text with bridge words: {new_text_with_bridge_words}")

