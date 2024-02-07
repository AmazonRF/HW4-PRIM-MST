import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """
        self.mst = None

        
        # Short variable for readability.
        graph = self.adj_mat.copy()

        # Use a value greater than the maximum edge weight in the graph as a placeholder, i am not use inf here because the format issue
        maxi_val = np.max(graph) + 2
        graph[graph ==0] = maxi_val  # Replace zero weights to avoid considering non-edges.
        # List to keep track of vertices included in the MST.
        mst_node = []

        # Number of vertices in the graph.
        graph_node_no = int(graph.shape[0])

        # Initialize an empty adjacency matrix for the MST.
        output_path = np.zeros(graph.shape)

        # Start MST with the first vertex.
        mst_node.append(0)

        # Construct the MST by adding one edge at a time.
        for _ in range(graph_node_no):
            # Lists to keep track of potential next nodes and edges to add to the MST.
            potential_next_node = []
            potential_next_edge = []

            # For each node already in the MST, find the edge with minimum weight to a node not yet in the MST.
            for node in mst_node:
                t = np.argmin(graph[node])
                potential_next_node.append(t)
                potential_next_edge.append(graph[node][t])
            
            # Determine the next node to add based on the minimum edge weight.
            next_node = potential_next_node[np.argmin(potential_next_edge)]
            next_node_mother = mst_node[np.argmin(potential_next_edge)]
            
            # Break the loop if no valid next node is found (i.e., all remaining edges are maxi_val).
            # if np.min(potential_next_edge) <=0 or np.min(potential_next_edge)==maxi_val:break
            
            # Update the MST adjacency matrix to include the new edge.
            output_path[next_node][next_node_mother] = 1
            output_path[next_node_mother][next_node] = 1

            # Mark the newly added edge as maxi_val in the original graph to prevent it from re-visit
            for node_ in mst_node:
                graph[node_][next_node] = maxi_val
                graph[next_node][node_] = maxi_val
            mst_node.append(next_node)
            # print(mst_node,len(mst_node))

        self.mst = output_path*self.adj_mat
