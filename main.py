from Calculate import calcShortestPath
from DAG_gen import showDirectedGraph
from PageRank import calPageRank
from RandomWalk import randomWalk
from bridge_word import generateNewText, queryBridgeWords


def main():
    #功能1，2: 生成DAG并展示
    graph,words = showDirectedGraph()
    #功能3，4: 查询桥接词，根据桥接词生成新文本
    queryBridgeWords(graph)
    generateNewText(graph)
    #功能5: 最短路径
    calcShortestPath(graph)
    #功能6: PageRank
    calPageRank(graph, words)
    #功能7: 随机游走
    randomWalk(graph)

if __name__ == '__main__':
    main()