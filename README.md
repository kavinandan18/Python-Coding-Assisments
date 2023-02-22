# Python-Coding-Assisments


# ********************** Apprtment Hunting *********************

# find_optimal_block function 

 This function takes in a list of dictionaries representing city blocks and a list of requirements (such as the presence of a gym, school, or store) and returns the index of the block that is closest to all the requirements.

```python
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

```


# Requirements
```python
This program requires Python 3.x to be installed.
```



# Usage
The program can be run from the command line using the following command:
```python
python ApartmentHunting.py

```
By default, the program will use the sample data provided in the blocks and requirements variables in the code. If you want to use your own data, you can modify these variables in the code.



# Inputs
`blocks`: A list of `n` dictionaries, each representing a block. Each dictionary has three boolean keys: `gym`, `school`, and `store`. The value of each key is `True` if the corresponding facility is present in the block, and `False` otherwise.

`requirements`: A list of strings, representing the facilities that the user wants to be close to. The list can contain any combination of `"gym"`, `"school"`, and `"store`"

## Input Example
```python
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

```
# Output:
```python
3 // at index 3, the farthest you'd have to walk to reach a gym, a school, or a store is 1 block; at any other index, you'd have to walk farther

```