class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def getAvarages(root):
    queue = [root]
    level = -1
    levels = []
    while len(queue):
        length = len(queue)
        level += 1
        levels.append([])
        while length:
            current = queue.pop(0)
            levels[level].append(current.val)
            
            if current.left: 
                queue.append(current.left)
            
            if current.right: 
                queue.append(current.right)
            
            length -= 1

    return list(map(lambda x: sum(x) / len(x), levels))

if __name__ == "__main__":
    n3 = Node(3)
    n9 = Node(9)
    n20 = Node(20)
    n15 = Node(15)
    n7 = Node(7)

    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7

    print(getAvarages(n3))