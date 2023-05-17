uid = 0
class Node:
    def __init__(self, energy, distBs, head=False, member=False, area=10, members=[], x=0, y=0):
        global uid 
        self.id = uid
        uid += 1
        self.energy = energy
        self.distBs = distBs
        self.head = head
        self.member = member
        self.area = area
        self.members = members
        self.x = x  # x-coordinate of the node
        self.y = y  # y-coordinate of the node

    def __str__(self):
        if self.head : 
            return f"{self.id}, {[x.id  for x in self.members]}"
        else :
            return f"{self.id}"

# Print the initial list of nodes
if __name__ == "__main__":
    # Def
    # Create a sample list of nodes
    S = [
        Node(5, 10),
        Node(8, 15),
        Node(3, 7),
        Node(12, 9),
        Node(6, 11)
    ]
    print("Initial list:")
    for node in S:
        print(f"Energy: {node.energy}, Distance to BS: {node.distBs}")
