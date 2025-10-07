import hashlib

def crack_sha1_hash(hash, use_salts = False):

    salts = []
    if use_salts:
        with open("known-salts.txt") as salt_file:
            salts = salt_file.read()
            salts = salts.split("\n")
