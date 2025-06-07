# test_blackbox.py

import unittest

from DAG_gen import showDirectedGraph
from bridge_word import queryBridgeWords, _queryBridgeWords  # 替换为你的模块和函数名
file_path = "C:\\Users\\ASUS\\Desktop\\24\\SE\\LAB1\\Easy Test.txt"
# 功能1，2: 生成DAG并展示
graph, words = showDirectedGraph(file_path)

class TestQueryBridgeWordsBlackBox(unittest.TestCase):

    def test_valid_bridge_word(self):
        """
        测试：输入有效且存在桥接词
        """
        word1 = "a"
        word2 = "report"
        expected_output = ['detailed']  # 你预期的桥接词
        result = _queryBridgeWords(graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_no_bridge_word(self):
        """
        测试：输入有效但不存在桥接词
        """
        word1 = "detailed"
        word2 = "report"
        expected_output = []  # 假设无桥接词时返回空字符串
        result = _queryBridgeWords(graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_empty_string_input(self):
        """
        测试：输入word1或者word2不存在
        """
        word1 = ""
        word2 = "scientist"
        expected_output = []  # 根据函数定义填写
        result = _queryBridgeWords(graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_nonexistent_word_input(self):
        """
                测试：输入word1或者word2不存在
                """
        word1 = "ma"
        word2 = "maotian"
        expected_output = []  # 根据函数定义填写
        result = _queryBridgeWords(graph, word1, word2)
        self.assertEqual(result, expected_output)

    def test_case_sensitivity(self):
        """
        测试大小写输入
        """
        word1 = "A"
        word2 = "REPORT"
        expected_output = []
        result = _queryBridgeWords(graph,word1, word2)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
