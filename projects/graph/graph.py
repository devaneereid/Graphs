"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent vertex.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()
        # add starting vertex ID
        q.enqueue(starting_vertex)

        # create set for visited verts
        visited = set()

        # while queue is not empty
        while q.size() > 0:
            # dequeue 
            v = q.dequeue()

            # if not visited
            if v not in visited:
                print(v)
                # mark as visited
                visited.add(v)

                # add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


            # print(v)
            # visited.add(v)
            # for neighbor in self.get_neighbors(v):
            #     if neighbor not in visited:
            #         q.enqueue(neighbor)
            #         visited.add(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack
        s = Stack()
        s.push(starting_vertex)

        # create a set() - stores the visited vertices
        visited = set()

        # while queue is not empty
        while s.size() > 0:
            # pop the first index
            v = s.pop()
            print(v)

            visited.add(v)

            # add neighbors to top the the stack
            for next_vertex in self.get_neighbors(v):
                if next_vertex not in visited:
                    s.push(next_vertex)
                    visited.add(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # set up empty queue
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()

            if path[-1] == destination_vertex:
                return path
            else:
                for neighbor in self.get_neighbors(path[-1]):
                    # make a copy of the path
                    neighbors = path.copy()
                    neighbors.append(neighbor)
                    q.enqueue(neighbors)
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create empty stack
        s = Stack()

        s.push([starting_vertex])
         
        while s.size() > 0:
            # pop the first index
            path = s.pop()
            # check if path is the same as destination_vertex 
            if path[-1] == destination_vertex:
                return path
            else:
                for neighbor in self.get_neighbors(path[-1]):
                    # make a copy of the path
                    neighbors = path.copy()
                    # append node
                    neighbors.append(neighbor)
                    s.push(neighbors)
        return None


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        if path == None:
            path = []

        visited.add(starting_vertex)

        v = path + [starting_vertex]
        # neighbor = path.copy()
        # neighbor.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return v

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                neighbors = self.dfs_recursive(neighbor, destination_vertex, visited, v)
                if neighbors:
                    return neighbors
        return None

        # else:
        #     for neighbors in self.get_neighbors(starting_vertex):
        #         if neighbors not in visited:
        #             next_path = self.dfs_recursive(neighbors, destination_vertex, visited, neighbor)
        #         if next_path is not None:
        #             return next_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
