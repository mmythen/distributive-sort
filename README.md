# Distributive Sort
Goofball algorithm I made that constructs a sorted array by distributing sum differences rather than comparing elements.

## How it Works
1. Creates a base sorted array `[min, min+1, min+2, ...]`
2. Calculates difference between original sum and base array sum
3. Distributes values either up or down depending on difference by cycling through array positions

Results in an array where all elements are very as close together as possible while maintaining the original sum and containing no duplicates.
Cannot imagine it to be useful but was pretty fun to make.

## Complexities
- **Time Complexity**: O(n + |difference in sums|)
- **Space Complexity**: O(n)




