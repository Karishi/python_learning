class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set([v])
        else:
            self.graph[u].add(v)
        if v not in self.graph:
            self.graph[v] = set([u])
        else:
            self.graph[v].add(u)

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
