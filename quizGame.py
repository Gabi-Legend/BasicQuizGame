print("Welcome to CAPITALS QUIZ!")
count = 0
romania = input("What is the capital of Romania? : ")

romania = romania.lower()
if romania == "bucharest" or romania == "bucuresti":
    print("Congrats, you answered correctly!")
    count+=1
else:
    print("Wrong answer, the capital of Romania is Bucharest")

print(f"You had {count} correct answers!")