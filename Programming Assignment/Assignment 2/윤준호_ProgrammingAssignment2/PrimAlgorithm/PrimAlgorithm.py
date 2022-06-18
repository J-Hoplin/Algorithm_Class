'''
Source Code Written by : Hoplin

Written Date : 2022 / 06 / 18
'''
from typing import Any,MutableSequence,Dict
import networkx as ntx
import matplotlib.pyplot as plt
from copy import deepcopy
from collections import deque
from math import inf

class PrimAlgorithm(object):
    class GraphRenderingFailException(Exception):
        def __init__(self):
            super().__init__("Fail to render Graph!")

    class IntegrityBrokenException(Exception):
        def __init__(self):
            super().__init__("Some value break integrity!")

    def __init__(self,graph_matrix:MutableSequence[MutableSequence[int]],starting_node:int):
        self.edges = []
        self.matrix = graph_matrix
        self.start = starting_node
        self.graph_visual_data = self.group_graph_edges(graph_matrix)
        self.prim_visual_data = []
        self.check_graph_integrity()
        self.check_starting_point_integrity()


    def group_graph_edges(self,graph_matrix:MutableSequence[MutableSequence[int]]):
        val = []
        for i,j in enumerate(graph_matrix):
            for n,m in enumerate(j):
                if (i != n) and (m != inf):
                    self.edges.append((i,n,m))
                    # starting : [(end,weight)]
                    val.append([i,n])
        return val

    def visualizeInitialGraph(self):
        self.__visualizer(self.graph_visual_data)

    def visualizePrimMST(self):
        self.__visualizer(self.prim_visual_data)

    def __visualizer(self,edge_sequence):
        g = ntx.Graph()
        g.add_edges_from(edge_sequence)
        ntx.draw_networkx(g)
        plt.show()

    def check_starting_point_integrity(self):
        if self.start < 0 or self.start > len(self.matrix) - 1:
            raise PrimAlgorithm.IntegrityBrokenException

    def check_graph_integrity(self):
        try:
            length = len(self.matrix[0])
            for i in self.matrix:
                if len(i) != length:
                    raise PrimAlgorithm.IntegrityBrokenException
        except TypeError:
            raise PrimAlgorithm.IntegrityBrokenException

    def change_starting_node(self,node):
        self.start = node
        self.check_starting_point_integrity()

    def change_graph(self,graph_matrix:MutableSequence[MutableSequence[int]]):
        self.matrix = graph_matrix
        self.group_graph_edges()
        self.check_graph_integrity()

    def prim(self):
        # Clear Prim Visual Data
        self.prim_visual_data = []
        size = len(self.matrix)
        Q = deque([i for i in range(size)])
        S = deque([])
        costs = [inf for _ in range(size)]
        edges = deepcopy(self.edges)
        # Set startpoint cost to 0
        costs[self.start] = 0
        # Append to Spanning Tree
        S.append(self.start)
        # Remove from left tree
        Q.remove(self.start)
        edges.sort(key=lambda x: x[2])
        while Q:
            filter_edges = list(filter(lambda x:x[0] in S and x[1] in Q,edges))
            least_common_edge = filter_edges[0]
            nextNode = least_common_edge[1]
            for i,j,l in filter_edges:
                if costs[j] > l:
                    costs[j] = l
            self.prim_visual_data.append((least_common_edge[0],nextNode))
            S.append(nextNode)
            Q.remove(nextNode)
        self.primSummary(costs)

    def primSummary(self,costs:MutableSequence):
        print("[ Prim MST's edge information ]\n")
        for i,j in enumerate(self.prim_visual_data):
            n, m = j
            print(f"{n} -> {m} | Weight : {costs[m]}")
        print("\n[ Prim MST's Visualization ]")
        self.visualizePrimMST()



if __name__ == "__main__":
    graph = [
        [0, 2, 5, 1, inf, inf],
        [2, 0, 3, 2, inf, inf],
        [5, 3, 0, 3, 1, 5],
        [1, 2, 3, 0, 1, inf],
        [inf, inf, 1, 1, 0, 2],
        [inf, inf, 5, inf, 2, 0]
    ]
    p = PrimAlgorithm(graph,0)
    p.visualizeInitialGraph()
    p.prim()
