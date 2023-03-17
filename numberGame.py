from random import randint

list = {'Maxim': 200, 'Chett': 200, 'Alina': 300}
def main():
   user_res = input("Enter s or S to start the Game =>")

   while user_res != "s" and user_res != "S":
       user_res = input("Wrond Input try again => ")
   start_game()

def end_game():
    print("Thanks for palying")

def showList(isWin, score):
    user_res = input("Press b to see Score Board => ")
    while user_res != "b":
        user_res = input("Unkown Input, try again => ")
    else:
        for i in list:
            print(f"{i}: {list[i]}")

    if isWin == True:
        user_score_res = input(f"Press y if you want to add your score or press q to end the game, {score} =>")
        if user_score_res == "q":
            end_game()
        elif user_score_res == "y":
            username = input("Enter your username => ")
            list[username] = score
            for i in list:
                print(f"{i}: {list[i]}")



def start_game():
    print("Welcome to the number guessing game, you sohuld guess number between 1 and 10")
    isWin = False
    default_score = 100
    attempts = 3
    rand_num = randint(1, 10)
    print(rand_num)
    user_num = int(input("Enter your number => "))
    while int(user_num) != rand_num:
        if user_num > rand_num:
            print("Lower")
        elif user_num < rand_num:
            print("Higher")

        if attempts == 1:
            print("You are out of attempts, Loser")
            showList(isWin, default_score)
            break
        attempts -= 1
        print(f"Wrong you have {attempts} left")
        user_num = int(input("Enter your number => "))
    else:
        print("You Win")
        print(f"Score: {default_score * attempts}")
        user_score = default_score * attempts
        isWin = True
        showList(isWin, user_score)
main()


