import random


def main():
    # print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    last = 13
    rnd = random.randint(0, last)

    print(quotes[rnd])


rndx = random.randint(1, 5)

if __name__ == "__main__":
    for _ in range(rndx):
        main()
