import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances


def check_mst(adj_mat: np.ndarray, 
              mst: np.ndarray, 
              expected_weight: int, 
              allowed_error: float = 0.0001):
    """
    
    Helper function to check the correctness of the adjacency matrix encoding an MST.
    Note that because the MST of a graph is not guaranteed to be unique, we cannot 
    simply check for equality against a known MST of a graph. 

    Arguments:
        adj_mat: adjacency matrix of full graph
        mst: adjacency matrix of proposed minimum spanning tree
        expected_weight: weight of the minimum spanning tree of the full graph
        allowed_error: allowed difference between proposed MST weight and `expected_weight`

    TODO: Add additional assertions to ensure the correctness of your MST implementation. For
    example, how many edges should a minimum spanning tree have? Are minimum spanning trees
    always connected? What else can you think of?

    """

    def approx_equal(a, b):
        return abs(a - b) < allowed_error

    total = 0
    edge_number = 0
    node_number = adj_mat.shape[0]
    for i in range(mst.shape[0]):
        for j in range(i+1):
            total += mst[i, j]
            if mst[i, j]>0:edge_number += 1 

    #Given assertion
    assert approx_equal(total, expected_weight), 'Proposed MST has incorrect expected weight'
    #My assertion 1: minimum spanning trees always connected and the edges number is N-1. N:node number
    assert node_number - 1  == edge_number , 'Proposed MST has incorrect expected edges number'
    #My assertion 2: MST and original graph must have the same dimensions.
    assert mst.shape == adj_mat.shape, "MST and original graph must have the same dimensions."



def test_mst_small():
    """
    
    Unit test for the construction of a minimum spanning tree on a small graph.
    
    """
    file_path = './data/small.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 8)


def test_mst_single_cell_data():
    """
    
    Unit test for the construction of a minimum spanning tree using single cell
    data, taken from the Slingshot R package.

    https://bioconductor.org/packages/release/bioc/html/slingshot.html

    """
    file_path = './data/slingshot_example.txt'
    coords = np.loadtxt(file_path) # load coordinates of single cells in low-dimensional subspace
    dist_mat = pairwise_distances(coords) # compute pairwise distances to form graph
    g = Graph(dist_mat)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 57.263561605571695)


def test_mst_student():
    """
    
    TODO: Write at least one unit test for MST construction.
    
    """
    #My unit test 1: Input test type
    with pytest.raises(Exception, match='Input must be a valid path or an adjacency matrix'):
        g_single_node = Graph(0)
        g_single_node.construct_mst()

    #My unit test 2: Input test, make sure all the edge are positive.
    negInput = 'data/small_neg.csv'
    with pytest.raises(Exception, match='Edge could not be negative'):
        g_neg = Graph(negInput)
    
