from random import randint
import urllib.request, json, requests

def main():
   user_res = input("Enter s or S to start the Game =>")

   while user_res != "s" and user_res != "S":
       user_res = input("Wrong Input try again => ")
   start_game()

def end_game():
    print("Thanks for playing")

def showList(isWin, score):
    user_res = input("Press b to see Score Board => ")
    while user_res != "b":
        user_res = input("Unknown Input, try again => ")
    else:
        url = "http://localhost:3000/scores"
        with urllib.request.urlopen(url) as url:
            data = json.load(url)
            data = data[::-1]
            print(data)
            for i in data:
                print(f"|{i['username']}: {i['score']}|")

    if isWin == True:
        user_score_res = input(f"Press y if you want to add your score or press q to end the game, {score} =>")
        if user_score_res == "q":
            end_game()
        elif user_score_res == "y":
            username = input("Enter your username => ")
            url = "http://localhost:3000/scores"
            r = requests.post(url, json={
                "username":username,
                "score":score
            })
            with urllib.request.urlopen(url) as url:
                data = json.load(url)
                data = data[::-1]
                for i in data:
                    print(f"|{i['username']}: {i['score']}|")



def start_game():
    print("Welcome to the number guessing game, you should guess number between 1 and 10")
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


