set = [str(i) if i % 3 != 0 and i % 5 != 0 else 'fizzBuzz' if i % 15 == 0 else 'fizz' if i % 3 == 0 else 'buzz' for i in range(1,101)]
print(set)