# def count_up_to(n):
#   count = 1
#   while count <= n:
#     yield count
#     count += 1

# for num in count_up_to(5):
#   print(num)

# def large_sequence(n):
#   for i in range(n):
#     yield i

# # This doesn't create a million numbers in memory
# gen = large_sequence(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def simple_generator():
#     yield "Hello"
#     yield "World"
#     yield "!"

# gen=simple_generator()
# print(next(gen)) #Output: Hello
# print(next(gen)) #Output: World
# print(next(gen)) #Output: !

# sum of squares of first 10 numbers using generator expression
# total = sum(x*x for x in range(10))
# print(total) 

# Generate 100 Finbonacci numbers using a generator function

# def fibonacci():
#     a, b= 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# gen=fibonacci()
# for _ in range(100):
#     print(next(gen))


# def genrate():
#     while True:
#         received=yield
#         print(f"Received: {received}")
# gen=genrate()
# next(gen) # Start the generator
# gen.send("Hello") #Output: Received: Hello
# gen.send("World") #Output: Received: World


def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
print(next(gen))
gen.close()