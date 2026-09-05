from queue import PriorityQueue
import matplotlib.pyplot as plt

grid = [
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,0,1,1],
    [0,0,1,0,0],
    [1,1,0,0,0]
]

start = (0, 0)
goal = (4, 4)

movements = [
    (-1, 0),  
    (1, 0),   
    (0, -1),  
    (0, 1)    
]

rows = len(grid)
columns = len(grid[0])

frontier = PriorityQueue()

frontier.put((0, start))

visited = set()
came_from = {start: None}
cost_so_far = {start: 0}
path_found = False


while not frontier.empty():

    priority, current = frontier.get()

    if current in visited:
        continue

    visited.add(current)

    print("Checking:", current)

    if current == goal:
        print("Goal reached!")
        path_found = True
        break

    for movement in movements:

        next_row = current[0] + movement[0]
        next_column = current[1] + movement[1]

        if 0 <= next_row < rows and 0 <= next_column < columns:

            neighbour = (next_row, next_column)

            if grid[next_row][next_column] == 0:

                new_cost = cost_so_far[current] + 1

                if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                    cost_so_far[neighbour] = new_cost

                    heuristic = (
                        abs(next_row - goal[0])
                        + abs(next_column - goal[1])
                    )
                    neighbour_priority = new_cost + heuristic

                    frontier.put((neighbour_priority, neighbour))
                    came_from[neighbour] = current

else:
    print("The goal cannot be reached.")

plt.imshow(grid, cmap="gray_r")

for row in range(5):
    for column in range(5):
        plt.text(
            column,
            row,
            f"({row},{column})",
            ha="center",
            va="center",
            color="blue"
        )


path = []

if path_found:
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    print("Ordered path:", path)
else:
    print("No path to draw.")

path_x = [position[1] for position in path]
path_y = [position[0] for position in path]

plt.plot(
    path_x,
    path_y,
    color="blue",
    linewidth=3,
    marker="o",
    label="UAV Path"
)

plt.scatter(
    start[1],
    start[0],
    label="Start",
    s=200,
    color="green"
)

plt.scatter(
    goal[1],
    goal[0],
    label="Goal",
    marker="x",
    s=200,
    color="red"
)

plt.xticks(range(columns))
plt.yticks(range(rows))
plt.grid()
plt.legend()
plt.title("UAV Path Planning ")

print("The cost is", len(path)-1)
plt.show()