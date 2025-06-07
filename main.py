##

from Calculate import calcShortestPath
from DAG_gen import showDirectedGraph
from PageRank import calPageRank
from RandomWalk import randomWalk
from bridge_word import generateNewText, queryBridgeWords
#测试main.py更改

def main():
    # 用户输入文件路径
    file_path = "C:\\Users\\ASUS\\Desktop\\24\\SE\\LAB1\\Easy Test.txt"
    #功能1，2: 生成DAG并展示
    graph,words = showDirectedGraph(file_path)
    #功能3，4: 查询桥接词，根据桥接词生成新文本
    queryBridgeWords(graph)
    #generateNewText(graph)
    #功能5: 最短路径
    #calcShortestPath(graph)
    #功能6: PageRank
    #calPageRank(graph, words)
    #功能7: 随机游走
    #randomWalk(graph)

if __name__ == '__main__':
    main()


#pylint main.py 检查规范性
#bandit main.py 检查安全问题


#coverage run --source=bridge_word -m unittest test_blackbox.py
#coverage report -m
#coverage html
#htmlcov\index.html
