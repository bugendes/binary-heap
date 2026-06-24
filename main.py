#!/usr/bin/env python3
"""Binary Heap demo."""

from binary_heap import BinaryHeap


def main():
    print("=== Binary Heap Demo ===
")

    h = BinaryHeap()
    data = [15, 3, 8, 1, 12, 6, 20, 2]
    print(f"Pushing: {data}")
    for x in data:
        h.push(x)
        print(f"  push({x}) -> peek={h.peek()}, size={h.size}")

    print(f"
Heap: {h}")
    print(f"Heapify demo: ", end="")
    h2 = BinaryHeap(min_heap=False)
    h2.heapify([5, 3, 7, 1, 9])
    print(f"max-heap from [5,3,7,1,9] -> {h2}")


if __name__ == "__main__":
    main()
