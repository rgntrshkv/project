import random

number = random.randint(0, 10)
cnt_tries = 0
while True:
    answer = input("Enter number:")
    if answer == "exit":
	break
    if not answer:
	continue
    if not answer.isdigit():
	print("Enter normal number!")
	continue
    cnt_tries += 1
    uanswer = int(answer)
    if rand < uanswer:
	print("Key is less")
	continue
    elif rand > uanswer:
	print("Key is greater")
	continue
    else:
	print("Win!")
	print("Number of tries: "+str(cnt_tries))
	break