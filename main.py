
class Node:
    gCost = -1
    hCost = -1
    wall = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: Fail-safe
    def calculateGCost(self, node):
        add = 10
        if self.x != node.x and self.y != node.y:
            add = 14

        self.gCost = node.gCost + add

    def calculateHCost(self):
        minC = min(abs(endNode.x - self.x), abs(endNode.y - self.y))
        maxC = max(abs(endNode.x - self.x), abs(endNode.y - self.y))

        self.hCost = minC*14 + (maxC-minC)*10

    def fCost(self):
        return self.gCost + self.hCost

    def neighborNodes(self):
        neighbors = []
        if self.x-1 >= 0:
            if self.y-1 >= 0 and not grid[self.x-1][self.y-1].wall:
                neighbors.append(grid[self.x-1][self.y-1])
            if not grid[self.x-1][self.y].wall:
                neighbors.append(grid[self.x-1][self.y])
            if self.y+1 < HEIGHT and not grid[self.x-1][self.y+1]:
                neighbors.append(grid[self.x-1][self.y+1])

        if self.y - 1 >= 0 and not grid[self.x][self.y-1].wall:
            neighbors.append(grid[self.x][self.y - 1])
        if self.y + 1 < HEIGHT and not grid[self.x][self.y+1].wall:
            neighbors.append(grid[self.x][self.y + 1])

        if self.x+1 < WIDTH:
            if self.y-1 >= 0 and not grid[self.x-1][self.y-1].wall:
                neighbors.append(grid[self.x+1][self.y-1])
            if not grid[self.x + 1][self.y].wall:
                neighbors.append(grid[self.x+1][self.y])
            if self.y+1 < HEIGHT and not grid[self.x+1][self.y+1]:
                neighbors.append(grid[self.x+1][self.y+1])

        return neighbors

WIDTH = 80
HEIGHT = 80
grid = [[]]
for y in range(HEIGHT):
    for x in range(WIDTH):
        grid[x][y] = Node(x, y)

grid[0][2].wall = True
grid[1][2].wall = True
grid[2][2].wall = True

startNode = grid[1][1]
endNode = grid[20][10]


