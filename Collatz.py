import time,sys

def collatz (num):
    while num != 1:
        if num % 2:
            num = int(num * 3 + 1)
        else:
            num = int(num / 2)
        print(num)
        time.sleep(0.1)

def main():
    print("COLLATZ SEQUENCE")
    print("Input an integer to start the sequence")
    try:
        num = int(input())
    except ValueError:
        print("That's not an integer!")
        main()
    
    collatz(num)

if __name__ == "__main__":
    main()