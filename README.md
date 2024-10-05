# SearchAlgo

**SearchAlgo** is a Python library that provides a collection of efficient search algorithms and graph traversal techniques. This library aims to offer users a variety of methods for searching and traversing data structures, making it easier to implement and understand various algorithms.

## Features

- **Search Algorithms**:
  - Linear Search
  - Binary Search
  - Jump Search
  - Interpolation Search
  - Exponential Search
  - Fibonacci Search

- **Graph Traversal Algorithms**:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)

## Installation ##

You can install the library via pip:

```bash
pip install SearchAlgo

If you want to install the latest version directly from GitHub, use:

pip install -U https://github.com/SANS002/SearchAlgo.git

Usage:
Here’s a quick example of how to use the library:

from SearchAlgo import linear_search, binary_search, bfs, dfs

# Example data
arr = [1, 2, 3, 4, 5]
target = 3

# Using Linear Search
index = linear_search(arr, target)
print(f'Linear Search: Element found at index {index}')

# Using Binary Search
index = binary_search(arr, target)
print(f'Binary Search: Element found at index {index}')

# Example Graph for BFS and DFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Using BFS
bfs_result = bfs(graph, 'A', 'F')
print(f'BFS: {bfs_result}')

# Using DFS
dfs_result = dfs(graph, 'A', 'F')
print(f'DFS: {dfs_result}')


Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

Steps to Contribute:

Fork the repository
Create a new branch for your feature or fix
Commit your changes
Push to the branch
Create a pull request