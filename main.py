import random

def main():
    h_t = ["h", "t"]

    w = input("choose heads or tails >>>  ").lower().strip()

    choice = random.choice(h_t)

    if choice == "t":
        if w == "tails":
            print("you won it was tails")
        else:
            print("you lost it was tails")
    if choice == "h":
        if w == "heads":
            print("you won it was heads")
        else:
            print("you lost it was heads")
    main()
while True:
    main()


