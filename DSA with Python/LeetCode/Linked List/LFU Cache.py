# PROBLEM NUMBER: 460
# https://leetcode.com/problems/lfu-cache/
# 460. LFU Cache
# DIFFICULTY: HARD

from collections import defaultdict, OrderedDict


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # Approach:
        # We need to design a cache that removes the Least Frequently Used (LFU) key.
        # If multiple keys have same frequency → remove Least Recently Used (LRU).
        #
        # To achieve O(1) operations, we use:
        #
        # Step 1: Two data structures:
        #         • keyMap → key → (value, freq)
        #         • freqMap → freq → OrderedDict(keys)
        #
        # Step 2: freqMap helps:
        #         • Track keys with same frequency
        #         • Maintain insertion order → helps LRU removal
        #
        # Step 3: Maintain minFreq:
        #         • Stores minimum frequency in cache
        #         • Used to quickly identify LFU keys

        self.capacity = capacity
        self.keyMap = {}  # key -> (value, freq)
        self.freqMap = defaultdict(OrderedDict)  # freq -> OrderedDict of keys
        self.minFreq = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Step 4: If key not present → return -1
        #
        # Step 5: If present:
        #         • Get value and frequency
        #         • Remove key from current freq list
        #         • Update minFreq if needed
        #         • Add key to next frequency list
        #         • Return value

        if key not in self.keyMap:
            return -1

        val, freq = self.keyMap[key]

        # remove from current frequency list
        del self.freqMap[freq][key]

        # update minFreq if needed
        if not self.freqMap[freq]:
            del self.freqMap[freq]
            if self.minFreq == freq:
                self.minFreq += 1

        # add to next frequency
        self.keyMap[key] = (val, freq + 1)
        self.freqMap[freq + 1][key] = None

        return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # Step 6: If capacity is 0 → do nothing
        #
        # Step 7: If key already exists:
        #         • Update value
        #         • Call get() to update frequency
        #
        # Step 8: If cache is full:
        #         • Remove LFU key
        #         • Use minFreq to find correct frequency list
        #         • Remove LRU key from that list (OrderedDict)
        #
        # Step 9: Insert new key:
        #         • Add with frequency = 1
        #         • Update minFreq = 1

        if self.capacity == 0:
            return

        # if key exists → update value + increase freq
        if key in self.keyMap:
            self.keyMap[key] = (value, self.keyMap[key][1])
            self.get(key)  # reuse get to update frequency
            return

        # if full → remove LFU key
        if len(self.keyMap) >= self.capacity:
            k, _ = self.freqMap[self.minFreq].popitem(last=False)
            del self.keyMap[k]

            if not self.freqMap[self.minFreq]:
                del self.freqMap[self.minFreq]

        # insert new key
        self.keyMap[key] = (value, 1)
        self.freqMap[1][key] = None
        self.minFreq = 1