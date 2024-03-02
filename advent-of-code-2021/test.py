def read_map(input_lines):
    graph = {}
    for line in input_lines:
        start, end = line.strip().split('-')
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
        if end in graph:
            graph[end].append(start)
        else:
            graph[end] = [start]
    print("Graph:", graph)
    return graph

def find_paths(graph, current_node, visited, path, double_visit_used):
    print(f"Visiting: {current_node}, Path so far: {'->'.join(path)}, Double visit used: {double_visit_used}")
    if current_node == "end":
        print(f"Found path: {'->'.join(path + [current_node])}")
        return [path + [current_node]]
    
    paths = []
    for next_node in graph[current_node]:
        print(f"Checking: {next_node} from {current_node}")
        if next_node.isupper() or next_node not in visited:
            paths += find_paths(graph, next_node, visited.union({next_node}), path + [current_node], double_visit_used)
        elif not double_visit_used and next_node not in ["start", "end"]:
            paths += find_paths(graph, next_node, visited, path + [current_node], True)
    
    return paths

def count_unique_paths_with_double_visit(input_lines):
    graph = read_map(input_lines)
    paths = find_paths(graph, "start", set(["start"]), [], False)
    return len(paths), paths

# Input lines
input_lines = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end"
]

# Count unique paths allowing a single lowercase node to be visited twice
num_paths, paths = count_unique_paths_with_double_visit(input_lines)
print(f"Total unique paths: {num_paths}")
for path in paths:
    print(" -> ".join(path))
