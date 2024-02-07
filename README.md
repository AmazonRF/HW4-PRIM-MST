![BuildStatus](https://github.com/AmazonRF/HW4-PRIM-MST/actions/workflows/pytest.yml/badge.svg?event=push)

## Minimum Spanning Tree Implementation and Validation

This project includes an implementation of Prim's algorithm to construct a Minimum Spanning Tree (MST) from a given undirected, weighted graph. The implementation is provided in Python and utilizes NumPy for matrix operations. Additionally, the project includes validation functions to ensure the correctness of the constructed MST based on several key properties.

## Features

- **Prim's Algorithm Implementation**: Constructs an MST from an adjacency matrix representing an undirected, weighted graph.
- **MST Validation**: Includes checks for the correct number of edges, connectivity, absence of cycles, and minimum total weight to validate the constructed MST.
- **Graph Representations**: Supports loading graphs from both NumPy arrays and CSV files containing adjacency matrices.

## Getting Started

### Prerequisites

- Python 3.x
- NumPy

### Installation

Ensure you have Python and NumPy installed. You can install NumPy using requirments.txt if you haven't already:


### Usage

1. **Graph Initialization**: Initialize a `Graph` object with an adjacency matrix or a path to a CSV file containing the adjacency matrix.

    ```python
    from graph import Graph
    graph = Graph(adjacency_mat='path/to/your/adjacency_matrix.csv')
    # OR
    graph = Graph(adjacency_mat=your_numpy_array)
    ```

2. **Constructing the MST**: Call the `construct_mst` method on your `Graph` object to construct the MST.

    ```python
    graph.construct_mst()
    ```

3. **Validating the MST**: Use the provided validation assertions within the `verify_mst_properties` function to ensure the correctness of the constructed MST. Implement the necessary functions for connectivity and weight checks as required.

Readme file above are generated with the help of chatGPT.
## Grading

### Code (6 points)

* Minimum spanning tree construction works correctly (6)
    * Correct implementation of Prim's algorithm (4)
    * Produces expected output on small graph (1) 
    * Produces expected output on single cell data (1) 

### Unit tests (3 points)

* Complete function "check_mst" (1)
* Write at least two unit tests for MST construction (2)

### Style (1 points)

* Readable code with clear comments and method descriptions (1)

### Extra credit (0.5)

* Github actions/workflow (0.5)
