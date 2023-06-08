import random
import time

number = random.randint(0, 10001)
tries_count = 0
print("Print \"exit\" to end the game")
start_time = time.time()
while True:
    answer = input("Enter number:")
    if answer == "exit":
        break
    if not answer:
        continue 

    if not answer.isdigit():
        print("Enter normal number!")
        continue

    user_answer = int(answer)
    if user_answer > number:
        print("the hidden number is less")
        tries_count+=1
    elif user_answer < number:
        print("the hidden number is greater")
        tries_count+=1
    else:
        full_time = time.time() - start_time
        print("CONGRATULATIONS! Number of tries - {}".format(tries_count+1))
        print(f"Time:{full_time:.3f} seconds")
        break