from hashlib import sha256

def login(email, stored_logins , pasword_to_check):
    if stored_logins[email] == hash_pasword(pasword_to_check):
        return True
    return False

def hash_pasword(pasword):
    return sha256(pasword.encode()).hexdigest()

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    print(login("example@gmail.com" , stored_logins ,  "words"))
    print(login("example@gmail.com" , stored_logins , "pasword"))

    print(login("code_in_placer@cip.org" , stored_logins ,"12222"))
    print(login("code_in_placer@cip.org" , stored_logins , "1222"))

    print(login("student@stanford.edu" , stored_logins , "pasword"))
    print(login("student@stanford.edu" , stored_logins , "14456"))

main()