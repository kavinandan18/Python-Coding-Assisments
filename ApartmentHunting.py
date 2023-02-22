def find_optimal_block(blocks, requirements):
    min_farthest_distance = float('inf')
    optimal_blocks = []

    for i, block in enumerate(blocks):
        distances = [0 if block[req] else float('inf') for req in requirements]
        for j, other_block in enumerate(blocks):
            if other_block == block:
                continue
            for k, req in enumerate(requirements):
                if other_block[req]:
                    distances[k] = min(distances[k], abs(i - j))
        farthest_distance = max(distances)
        if farthest_distance < min_farthest_distance:
            min_farthest_distance = farthest_distance
            optimal_blocks = [i]
        elif farthest_distance == min_farthest_distance:
            optimal_blocks.append(i)

    return optimal_blocks, farthest_distance


blocks =  [
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": True,
    "school": False,
    "store": False,
  },
  {
    "gym": True,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": True,
  },
]

requirements = ["gym", "school", "store"] 
optimal_blocks, farthest_distance = find_optimal_block(blocks, requirements)

print(f"{optimal_blocks[0]} // at index {optimal_blocks[0]}, the farthest you'd have to walk to reach a gym, a school, or a store is {farthest_distance} block(s); at any other index, you'd have to walk farther")
