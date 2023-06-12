import timeit
from solution import full_justify_efficient, full_justify_inefficient

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

start_time = timeit.default_timer()
full_justify_efficient(words, maxWidth)
end_time = timeit.default_timer()
print(f"Efficient Method took {end_time - start_time} seconds.")

start_time = timeit.default_timer()
full_justify_inefficient(words, maxWidth)
end_time = timeit.default_timer()
print(f"Inefficient Method took {end_time - start_time} seconds.")
