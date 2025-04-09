import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
   random_numbers = []
   for i in range(N_NUMBERS):
         num = random.randint(MIN_VALUE , MAX_VALUE)
         random_numbers.append(num)
         print("Random number", num)

if __name__ == "__main__":
        main()