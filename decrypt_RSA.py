from Crypto.Util.number import inverse, long_to_bytes

c = int(input("Give me the decrypted message"))
n = int(input("Give me the factoriel n"))
e = int(input("Give me the coefficient e"))
p = int(input("Give me the first primary of the factoriel"))
q = int(input("Give me the second primary of the factoriel"))

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c,d,n)

print(long_to_bytes(m))