# Password Derivation
#A common security method used for online banking is to ask the user for three random characters from a passcode. 
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply
# would be: 317.
#The text file, keylog.txt, contains fifty successful login attempts.

#Given that the three characters are always asked for in order, 
# analyse the file so as to determine the shortest possible secret passcode of unknown length

def derive_passcode():
    # Read the login attempts from the file.
    with open(r"C:\Users\ioank\OneDrive\Desktop\Project Euler\problem_79_password.txt") as f:
        attempts = [line.strip() for line in f if line.strip()]
    
    # Collect all digits that appear.
    nodes = set()
    for attempt in attempts:
        nodes.update(attempt)
    
    # Build a graph: for each attempt, if the attempt is "abc",
    # then a must come before b, and b before c (and hence a before c).
    graph = {node: set() for node in nodes}
    indegree = {node: 0 for node in nodes}
    
    for attempt in attempts:
        # For each pair of characters in the attempt, add an edge.
        for i in range(len(attempt)):
            for j in range(i+1, len(attempt)):
                if attempt[j] not in graph[attempt[i]]:
                    graph[attempt[i]].add(attempt[j])
                    indegree[attempt[j]] += 1

    # Perform topological sort.
    result = []
    # Copy the nodes set because we'll be removing items from it.
    nodes_remaining = set(nodes)
    while nodes_remaining:
        # Find all nodes with no incoming edge.
        zero_indegree = [node for node in nodes_remaining if indegree[node] == 0]
        if not zero_indegree:
            # Should not happen if there are no cycles.
            break
        # If more than one candidate exists, we can choose arbitrarily.
        current = zero_indegree[0]
        result.append(current)
        nodes_remaining.remove(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1

    return ''.join(result)

print(derive_passcode())

