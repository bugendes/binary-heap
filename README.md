# Binary Heap

A complete binary tree stored in a flat array, maintaining the heap property: every parent is smaller (min-heap) or larger (max-heap) than its children.

## How It Works

The tree lives in an array where node at index `i` has children at `2i+1` and `2i+2`, and parent at `(i-1)//2`.

**Push:** Append to the end, then "bubble up" — swap with parent while the heap property is violated. Takes O(log n) since the tree height is ⌊log₂n⌋.

**Pop:** Swap root with last element, remove last, then "sink down" — swap with the smaller (or larger) child while violated. O(log n).

**Heapify (Floyd's algorithm):** Start from the last non-leaf node and sift down each. Counter-intuitively, this is O(n), not O(n log n), because most nodes are near the bottom and sift very little.

**Pushpop:** Push then pop in one operation — if the new element is worse than the root, return it immediately. Otherwise replace root and sift down. More efficient than separate push+pop.

## Complexity

| Operation | Time | Notes |
|-----------|------|-------|
| push      | O(log n) | Bubble up from leaf |
| pop       | O(log n) | Sift down from root |
| peek      | O(1) | Root is always at index 0 |
| heapify   | O(n) | Floyd's bottom-up construction |
| pushpop   | O(log n) | Combined push + pop |

Space: O(n) for the array.

## Applications

**Priority Queues:** The standard implementation. Python's `heapq` module is a min-heap. Used in Dijkstra's, Prim's, A*, and Huffman coding.

**Heap Sort:** Build a max-heap in O(n), then repeatedly pop the root. O(n log n) worst case, in-place, not stable.

**Median Maintenance:** Two heaps (max-heap for lower half, min-heap for upper half) give O(1) median access and O(log n) insertion.

**Task Scheduling:** OS schedulers and job queues use heaps to efficiently find the highest-priority task.

**Graph Algorithms:** Dijkstra's shortest path and Prim's MST both use a heap to select the next edge/vertex.
