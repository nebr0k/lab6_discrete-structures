import unittest

from main import adjacency_matrix


class TestAdjacencyMatrix(unittest.TestCase):

    def test_empty_edges(self):
        n = 4
        edges = []
        adj_matrix = adjacency_matrix(n, edges)
        expected_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(adj_matrix, expected_matrix)

    def test_single_edge(self):
        n = 2
        edges = [(1, 2)]
        adj_matrix = adjacency_matrix(n, edges)
        expected_matrix = [[0, 1], [0, 0]]
        self.assertEqual(adj_matrix, expected_matrix)

    def test_multiple_edges(self):
        n = 4
        edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
        adj_matrix = adjacency_matrix(n, edges)
        expected_matrix = [[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
        self.assertEqual(adj_matrix, expected_matrix)

if __name__ == '__main__':
    unittest.main()
