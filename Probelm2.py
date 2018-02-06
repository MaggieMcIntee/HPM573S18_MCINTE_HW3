
class Node:
    """ base class """
    def __init__(self, name, cost, health_utility):
        self.name = name
        self.cost = cost
        self.health_utility = health_utility

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def get_expected_health_utility(self):
        """ abstract method to be overridden in derived classes
        :returns expected utility of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class ChanceNode(Node):

    def __init__(self, name, cost, health_utility, future_nodes, probs):
        """

        :param name: name of this chance node
        :param cost: cost of this chance node
        :param health_utility: utility of this chance node
        :param future_nodes: the terminal nodes that you could have from the chance nodes
        :param probs: probability of each terminal node that you can get from a chance node pathway
        """
        Node.__init__(self, name, cost, health_utility)
        """
        """
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_health_utility(self):
        """

        :return: expected health utility of this chance node
        """
        exp_health_utility = self.health_utility #expected health utility initialized with the health utility of the current node
        i = 0
        for node in self.futureNodes:
            exp_health_utility += self.probs[i]*node.get_expected_health_utility()
            i += 1
        return exp_health_utility

class TerminalNode(Node):

    def __init__(self, name, cost, health_utility):
        Node.__init__(self, name, cost, health_utility)

    def get_expected_cost(self):
        """
        :return: cost of this terminal node
        """
        return self.cost

    def get_expected_health_utility(self):
        """

        :return: health utility of this terminal
        """
        return self.health_utility

class DecisionNode(Node):

    def __init__(self, name, cost, health_utility, future_nodes):
        Node.__init__(self, name, cost, health_utility)
        self.futureNode = future_nodes

    def get_expected_costs(self):
        """ returns the expected costs of future nodes"""
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes[node.name] = node.get_expected_cost()

        return outcomes

    def get_expected_health_utility(self):
        outcomes1 = dict () #dictionary to store the expected health utility of the alternatives
        for node in self.futureNode:
            outcomes1[node.name] = node.get_expected_health_utility()

        return outcomes1
#######################
# See figure DT3.png (from the project menu) for the structure of this decision tree
########################

# create the terminal nodes (name, cost, health utility)
T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)

# create C2 (name, cost, health utility, future nodes, probabilities)
C2 = ChanceNode('C2', 35, 0, [T1, T2], [0.7, 0.3])
# create C1
C1 = ChanceNode('C1', 25, 0, [C2, T3], [0.2, 0.8])
# create C3
C3 = ChanceNode('C3', 45, 0, [T4, T5], [0.1, 0.9])

# create D1 (name, cost, utility, future nodes)
D1 = DecisionNode('D1', 0, 0, [C1, C3])

# print the expect cost of C1
print(D1.get_expected_costs(), D1.get_expected_health_utility())
