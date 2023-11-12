import hashlib
username_trial=input("Give me the data to hash").encode()
ind1=int(input("Give me the first index of the partition"))
ind2=int(input("Give me the second index of the partition"))
print(hashlib.sha256(username_trial).hexdigest()[ind1:ind2])
