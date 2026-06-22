#!/usr/bin/env python3
"""Binary Heap with decrease-key for priority queues."""
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.REMOVED = object()
        self.counter = 0

    def push(self, item, priority):
        if item in self.entry_finder: self.remove(item)
        entry = [priority, self.counter, item]
        self.counter += 1
        self.entry_finder[item] = entry
        heapq.heappush(self.heap, entry)

    def remove(self, item):
        entry = self.entry_finder.pop(item)
        entry[-1] = self.REMOVED

    def pop(self):
        while self.heap:
            prio, cnt, item = heapq.heappop(self.heap)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return item, prio
        raise KeyError("empty")

    def decrease_key(self, item, new_prio): self.push(item, new_prio)
    def __len__(self): return len(self.entry_finder)

if __name__ == "__main__":
    h = MinHeap()
    for task, p in [("code",3),("fix_bug",1),("deploy",5),("review",2),("test",4)]:
        h.push(task, p)
    h.decrease_key("deploy", 0)
    print("Min-Heap (deploy priority decreased to 0):")
    while h:
        t, p = h.pop()
        print(f"  {p}: {t}")\n