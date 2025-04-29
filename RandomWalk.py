import re
import networkx as nx
import random
import os


def random_walk(graph):
    # 随机选择一个起始节点
    start_node = random.choice(list(graph.nodes))
    print(f"Starting random walk from: {start_node}")

    visited_nodes = [start_node]
    visited_edges = set()
    current_node = start_node

    # 开始遍历
    while True:
        # 获取当前节点的所有出边
        neighbors = list(graph.neighbors(current_node))

        if not neighbors:
            print(f"No outgoing edges from node '{current_node}', stopping walk.")
            break

        # 随机选择一个邻居
        next_node = random.choice(neighbors)

        # 检查是否已经经过这条边
        edge = (current_node, next_node)
        if edge in visited_edges:
            print(f"Edge {edge} already visited, stopping walk.")
            break

        # 记录当前边和节点
        visited_edges.add(edge)
        visited_nodes.append(next_node)

        # 更新当前节点
        current_node = next_node

        # 用户可以随时停止
        stop = input(f"Current path: {' -> '.join(visited_nodes)}. Do you want to stop? (y/n): ")
        if stop.lower() == 'y':
            break

    return visited_nodes


def save_walk_to_file(visited_nodes, filename="random_walk.txt"):
    # 将遍历的节点输出到文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(" -> ".join(visited_nodes))
    print(f"Random walk saved to '{filename}'")


def randomWalk(graph):
    # 执行随机游走
    visited_nodes = random_walk(graph)

    # 将遍历的节点保存到文件
    save_option = input("\nDo you want to save the random walk to a file? (y/n): ")
    if save_option.lower() == 'y':
        file_name = input("Enter the file name to save (default: random_walk.txt): ")
        if not file_name:
            file_name = "random_walk.txt"
        save_walk_to_file(visited_nodes, file_name)
