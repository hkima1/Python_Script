def rot_cipher():
    bezos_cc_secret = input("Donner le texte a dechiffrer")
    rotate = int(input("Donner le nombre de rotation"))
    # Reference alphabet
    alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
                "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in bezos_cc_secret:
        index = alphabet.find(c)
        original_index = (index + rotate) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)

rot_cipher()