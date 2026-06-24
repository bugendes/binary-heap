"""Tests for BinaryHeap."""

import pytest
from binary_heap import BinaryHeap


class TestBinaryHeap:
    def test_min_heap(self):
        h = BinaryHeap()
        h.push(5); h.push(3); h.push(7); h.push(1)
        assert h.peek() == 1
        assert h.pop() == 1
        assert h.pop() == 3

    def test_max_heap(self):
        h = BinaryHeap(min_heap=False)
        h.push(5); h.push(3); h.push(7); h.push(1)
        assert h.peek() == 7
        assert h.pop() == 7
        assert h.pop() == 5

    def test_heap_sort(self):
        h = BinaryHeap()
        for x in [4, 2, 7, 1, 9, 3]:
            h.push(x)
        assert h.to_sorted() == [1, 2, 3, 4, 7, 9]

    def test_heapify(self):
        h = BinaryHeap()
        h.heapify([5, 3, 7, 1, 9])
        assert h.pop() == 1

    def test_pushpop(self):
        h = BinaryHeap()
        h.push(5); h.push(10)
        result = h.pushpop(3)
        assert result == 3  # 3 < 5, so 3 is returned directly

    def test_empty_errors(self):
        h = BinaryHeap()
        with pytest.raises(IndexError):
            h.pop()
        with pytest.raises(IndexError):
            h.peek()

    def test_custom_key(self):
        h = BinaryHeap(key=lambda x: x[1])
        h.push(("a", 3)); h.push(("b", 1)); h.push(("c", 2))
        assert h.pop() == ("b", 1)

    def test_size(self):
        h = BinaryHeap()
        assert h.size == 0
        h.push(1)
        assert h.size == 1
