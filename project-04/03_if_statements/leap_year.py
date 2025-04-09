def main():
    year = int(input("please enter year:"))
    if year % 4 == 0:
      if year % 100 != 0 or year % 400 == 0:
        print (f"this year is leap year")
      else:
          print (f"this year is not leap year")
    else:
       print (f"this year is not leap year")

if __name__ == "__main__":
   main()
      