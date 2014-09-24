netopt
======

netopt is a network topology optimization tool written in Python. It provides tools to monitor a network topology via MySQL database, runs optimizaiton algorithm and output the resulting streaming structure back to the same database. 

Prerequisite
-----

MySQL

Python 2.7

SQLAlchemy

NetworkX


Code description
-----

Data access objects are put under ./model directory, which manages the database operations for nodes, edges, and topologies.

Algorithms are put under ./algorithm directory, which runs different optimization algorithms. Now only Kruskal's minimum spanning tree and a power-based heuristic algorithm (Fast-Mesh) is provided.

How to use
-----

In model/__init__.py, modify the database url, and then simply run

```python
python main.py
```

It is a simple example that generates a random network topology, optimize it, and then store the resulting structure together with the origion topology in the database.


Limitations and future extensions
-----

The current model only supports single tree topology, which can be extended to multi-source, multi-tree(channel).
