PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    userage = int(input("Enter your age"))
    if userage >= PETURKSBOUIPO_AGE:
        print(f"you can vote in  PETURKSBOUIPO . where age of vote is  {PETURKSBOUIPO_AGE}")
    else:
        print(f"you can't vote in  PETURKSBOUIPO . where age of vote is  {PETURKSBOUIPO_AGE}")
    
    if userage >= STANLAU_AGE:
        print(f"you can vote in  STANLAU . where age of vote is  {STANLAU_AGE}")
    else:
        print(f"you can't vote in  STANLAU . where age of vote is  {STANLAU_AGE}")
    
    if userage >= MAYENGUA_AGE:
        print(f"you can vote in  MAYENGUA . where age of vote is  {MAYENGUA_AGE}")
    else:
        print(f"you can't vote in  MAYENGUA . where age of vote is  {MAYENGUA_AGE}")
    

if __name__ == "__main__":
    main()