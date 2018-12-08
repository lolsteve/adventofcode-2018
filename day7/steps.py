class Graph:
    def __init__(self):
        self.nodes = {}
        self.root_nodes = set()

    def isEmpty(self):
        return len(self.root_nodes) == 0

    def remove_next(self):
        to_remove = min(self.root_nodes)
        for successor in to_remove.successors:
            successor.predecessors.remove(to_remove)
            if len(successor.predecessors) == 0:
                self.root_nodes.add(successor)
        self.root_nodes.remove(to_remove)
        return to_remove

    def get_or_create(self, id):
        if id not in self.nodes:
            new_node = Node(id)
            self.nodes[id] = new_node
            self.root_nodes.add(new_node)
            return new_node
        else:
            return self.nodes[id]

    def add_edge(self, predecessor_id, successor_id):
        predecessor = self.get_or_create(predecessor_id)
        successor = self.get_or_create(successor_id)

        predecessor.successors.add(successor)
        successor.predecessors.add(predecessor)
        if successor in self.root_nodes:
            self.root_nodes.remove(successor)

class Node:
    def __init__(self, id):
        self.id = id
        self.successors = set()
        self.predecessors = set()

    def __lt__(self, other):
        return self.id < other.id

def parse_line(string):
    return (string[5], string[36])

def main():
    graph = Graph()
    with open('input.txt') as file:
        for line in file:
            predecessor_id, successor_id = parse_line(line)
            graph.add_edge(predecessor_id, successor_id)

    order = []
    while not graph.isEmpty():
        order.append(graph.remove_next().id)

    print(''.join(order))

if __name__ == '__main__':
    main()
