import unittest
import networkx as nx
from io import StringIO
import sys

from bridge_word import _queryBridgeWords


# 测试类
class TestQueryBridgeWords(unittest.TestCase):

    def setUp(self):
        # 重定向 stdout 捕获打印信息
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        # 恢复 stdout
        sys.stdout = self.original_stdout

    def test_word_not_in_graph(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        result = _queryBridgeWords(graph, "X", "B")
        self.assertEqual(result, [])
        self.assertIn('No "X" or "B" in the graph!', self.held_output.getvalue())

    def test_word2_not_in_graph(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        result = _queryBridgeWords(graph, "A", "Z")
        self.assertEqual(result, [])
        self.assertIn('No "A" or "Z" in the graph!', self.held_output.getvalue())

    def test_no_bridge_words(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        graph.add_edge("C", "D")
        result = _queryBridgeWords(graph, "A", "D")
        self.assertEqual(result, [])
        self.assertIn("No bridge words from word1 to word2!", self.held_output.getvalue())

    def test_single_bridge_word(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        result = _queryBridgeWords(graph, "A", "C")
        self.assertEqual(result, ["B"])

    def test_multiple_bridge_words(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "D")
        graph.add_edge("B", "C")
        graph.add_edge("D", "C")
        result = _queryBridgeWords(graph, "A", "C")
        self.assertCountEqual(result, ["B", "D"])  # 无顺序要求

    def test_empty_graph(self):
        graph = nx.DiGraph()
        result = _queryBridgeWords(graph, "A", "B")
        self.assertEqual(result, [])
        self.assertIn('No "A" or "B" in the graph!', self.held_output.getvalue())

if __name__ == '__main__':
    unittest.main()
