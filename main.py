import hashlib

wlist = input("wordlist: ")
hash2crack = input("hash: ")

rainbow = open(wlist, "r").readlines()
# print(wlistlines)


for i in range(0, len(rainbow)):
    hash2comp = hashlib.md5(rainbow[i].replace("\n", "").encode()).hexdigest()

    if hash2crack == hash2comp:
        print("password cracked: " + rainbow[i].replace("\n", " "))
        exit()

print("Wasn't able to crack the hash password")
