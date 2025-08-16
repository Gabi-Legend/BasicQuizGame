print("Welcome to CAPITALS QUIZ!")

playOrNot = input("Do you want to play?:").lower()

def play():
    count = 0
    romania = input("What is the capital of Romania? : ")

    romania = romania.lower()
    if romania == "bucharest" or romania == "bucuresti":
        print("Congrats, you answered correctly!")
        count+=1
    else:
        print("Wrong answer, the capital of Romania is Bucharest")

    france = input("What is the capital of France? : ")

    france = france.lower()
    if france == "paris":
        print("Congrats, you answered correctly!")
        count+=1
    else:
        print("Wrong answer, the capital of France is Paris")

    hungary = input("What is the capital of Hungary? : ")

    hungary = hungary.lower()
    if hungary == "budapest" or hungary == "budapesta":
        print("Congrats, you answered correctly!")
        count+=1
    else:
        print("Wrong answer, the capital of Hungary is Budapest")

    southKorea = input("What is the capital of South Korea? : ")

    southKorea = southKorea.lower()

    if southKorea == "seul" or southKorea=="seoul":
        print("Correct!")
        count+=1
    else:
        print("Wrong!")

    print(f"You had {count} correct answers!")

def quit():
    print("Maybe next time!")

if playOrNot == "yes" or playOrNot == "da":
    play()
else:
    quit()