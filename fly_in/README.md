_This project has been created as part of the 42 curriculum by eberling._

## Description

**Goal:**  
Fly-In is about creating an environment to run a simulation of moving drones through a map.

**Overview:**  
This project doesn't include a graphical representation and only returns in the terminal the moves each drone makes according to the constraints defined in the map file.

You can run the program with `make run` and use a specific map by using `MAP=<path>`.

## Algorithm Choices

For this project, I implemented only a pathfinding algorithm. For space/time management with drones, I just send as many drones as possible to the paths I found previously, and it is enough to fulfill the project requirements.

I implemented BFS for pathfinding as this is the simplest and most intuitive. The way it looks for the path is by spreading to all possible ways through the map, and when it finds the end, it adds the path to a list of paths.

In most of the maps given with the subject, the algorithm only finds one path. Then I send all these drones to the paths found. If more than one path is found, I check the usage / total capacity of a path and send the drones to the one that has the lowest usage.

## Visual Representation Features

For visual representation, I only rely on terminal output. As the subject doesn't explicitly require graphics to be done, I preferred to implement the minimum required.

## Instructions

### Requirements & Installation

- Python >=3.10
- uv

### Installation

```bash
make install
```

### Execution

```bash
# Basic run
make run

# Run with a specific map
make run MAP=<map_path>

# For more commands
make help
```

## Resources

### References

- Makefile from my previously done projects
- https://www.youtube.com/watch?v=cS-198wtfj0
- https://www.geeksforgeeks.org/dsa/difference-between-bfs-and-dfs/

### AI Usage

- I used AI mostly to write down the pathfinding and parsing algorithms.
- To understand the code snippets I found on the internet / that AI gave me.

Also, to preview the objects I defined in a nice way, I like to copy the raw output of an object, give it to AI, and ask it to represent this raw Python object output in a more readable way.
