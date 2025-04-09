# Magic 5-gon Ring

from itertools import permutations

def generate_magic_5gon_strings():
    """Finds the largest 16-digit string for a magic 5-gon ring."""
    max_string = ""

    # The numbers 1 to 10 must be used exactly once
    for perm in permutations(range(1, 11)):
        # Define the 5-gon ring structure:
        outer = [perm[5], perm[6], perm[7], perm[8], perm[9]]  # Outer nodes
        inner = [perm[0], perm[1], perm[2], perm[3], perm[4]]  # Inner nodes

        # Construct the five groups
        groups = [
            [outer[0], inner[0], inner[1]],
            [outer[1], inner[1], inner[2]],
            [outer[2], inner[2], inner[3]],
            [outer[3], inner[3], inner[4]],
            [outer[4], inner[4], inner[0]]
        ]

        # Check if all groups sum to the same value
        total = sum(groups[0])
        if all(sum(group) == total for group in groups):
            # Find the numerically lowest external node (to ensure unique representation)
            min_index = min(range(5), key=lambda i: groups[i][0])
            ordered_groups = groups[min_index:] + groups[:min_index]  # Rotate to start with min

            # Convert to string representation
            string_representation = "".join("".join(map(str, group)) for group in ordered_groups)

            # Ensure it's exactly 16 digits (avoiding 17-digit cases)
            if len(string_representation) == 16:
                max_string = max(max_string, string_representation)

    return max_string

# Run the function to find the result
result = generate_magic_5gon_strings()
print("Maximum 16-digit string for a magic 5-gon ring:", result)
