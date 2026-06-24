"""Binary heap implementation (min-heap by default).

A complete binary tree stored in a flat array. Parent at index i has
children at 2i+1 and 2i+2. The heap property ensures the root is always
the minimum (or maximum) element.

Operations:
  - push: O(log n) — bubble up
  - pop: O(log n) — sink down
  - peek: O(1)
  - heapify: O(n) — Floyd's algorithm

Used in: priority queues, Dijkstra's algorithm, heap sort, scheduling.
"""

from __future__ import annotations

from typing import Any, Callable, Generic, List, Optional, TypeVar

T = TypeVar("T")


class BinaryHeap(Generic[T]):
    """Binary min-heap (or max-heap).

    Args:
        min_heap: If True (default), root is the minimum element.
        key: Optional key function for custom comparison.
    """

    def __init__(self, min_heap: bool = True, key: Callable = None) -> None:
        self._data: List[T] = []
        self._min_heap = min_heap
        self._key = key or (lambda x: x)

    def _compare(self, a: T, b: T) -> bool:
        """Return True if a should be above b in the heap."""
        ka, kb = self._key(a), self._key(b)
        return ka < kb if self._min_heap else ka > kb

    @property
    def size(self) -> int:
        return len(self._data)

    @property
    def is_empty(self) -> bool:
        return len(self._data) == 0

    def push(self, item: T) -> None:
        """Add an element and restore heap property (bubble up)."""
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> T:
        """Remove and return the root. Raises IndexError if empty."""
        if self.is_empty:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self._data) - 1)
        result = self._data.pop()
        if self._data:
            self._sift_down(0)
        return result

    def peek(self) -> T:
        """Return the root without removing it."""
        if self.is_empty:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def pushpop(self, item: T) -> T:
        """Push item then pop root. More efficient than push+pop separately."""
        if self.is_empty or self._compare(item, self._data[0]):
            return item
        result = self._data[0]
        self._data[0] = item
        self._sift_down(0)
        return result

    def heapify(self, items: List[T]) -> None:
        """Build a heap from a list in O(n) using Floyd's algorithm."""
        self._data = list(items)
        # Start from last non-leaf and sift down
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._sift_down(i)

    def clear(self) -> None:
        self._data.clear()

    def to_sorted(self) -> List[T]:
        """Return elements in sorted order (destructive)."""
        result = []
        while not self.is_empty:
            result.append(self.pop())
        return result

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self._compare(self._data[idx], self._data[parent]):
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _sift_down(self, idx: int) -> None:
        n = len(self._data)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self._compare(self._data[left], self._data[smallest]):
                smallest = left
            if right < n and self._compare(self._data[right], self._data[smallest]):
                smallest = right
            if smallest != idx:
                self._swap(idx, smallest)
                idx = smallest
            else:
                break

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        kind = "min" if self._min_heap else "max"
        return f"BinaryHeap({kind}, {self._data})"
