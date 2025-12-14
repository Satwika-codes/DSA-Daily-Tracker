class MyHashMap(object):
    # Approach:
    # - Implement HashMap using Separate Chaining to handle collisions.
    # - Use a fixed-size array of buckets, where each bucket is a list.
    # - Each key is mapped to a bucket using modulo hashing (key % size).
    # - Each bucket stores [key, value] pairs.
    #
    # Operations:
    # - put: Update value if key exists, else insert new key-value pair.
    # - get: Search the bucket and return value if found, else -1.
    # - remove: Locate the key in its bucket and delete it if present.
    #
    # Time Complexity:
    # - Average: O(1) for put, get, remove
    # - Worst-case: O(n) if many keys collide into one bucket

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        index = key % self.size
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[index].append([key, value])

    def get(self, key):
        index = key % self.size
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        index = key % self.size
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                self.buckets[index].pop(i)
                return
