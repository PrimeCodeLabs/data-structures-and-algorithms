import timeit
from solution import LRUCache, LRUCacheInefficient

n = 10000  # change as necessary

# Testing Efficient Implementation
cache = LRUCache(n)

start_time = timeit.default_timer()
for i in range(n):
    cache.put(i, i)
end_time = timeit.default_timer()
print(f"Efficient Method Insertion took {end_time - start_time} seconds.")

start_time = timeit.default_timer()
for i in range(n):
    cache.get(i)
end_time = timeit.default_timer()
print(f"Efficient Method Retrieval took {end_time - start_time} seconds.")

# Testing Inefficient Implementation
cache = LRUCacheInefficient(n)

start_time = timeit.default_timer()
for i in range(n):
    cache.put(i, i)
end_time = timeit.default_timer()
print(f"Inefficient Method Insertion took {end_time - start_time} seconds.")

start_time = timeit.default_timer()
for i in range(n):
    cache.get(i)
end_time = timeit.default_timer()
print(f"Inefficient Method Retrieval took {end_time - start_time} seconds.")
