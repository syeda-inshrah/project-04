import random

DONE_LIKELIHOOD = 0.3

def choatic_counting():
    for i in range (10):
        curr_num = i + 10
        if done():
            return
        print(curr_num)

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False
def main():
    print("I am going to count until 10 or until I feel like stopping, whichever comes first.")
    choatic_counting()
    print("i am done")

main()