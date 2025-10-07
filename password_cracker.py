import hashlib

def crack_sha1_hash(hash, use_salts = False):

    salts = []
    if use_salts:
        with open("known-salts.txt") as salt_file:
            salts = salt_file.read()
            salts = salts.split("\n")

    with open("top-10000-passwords.txt", mode="r") as password_file:
        # get all passwords to check
        passwords = password_file.readlines()
        passwords = tuple(p.strip() for p in passwords)

        crack = hashlib.sha1()
        crack.update(hash.encode("utf-8"))
        cracked = crack.hexdigest()

        for password in passwords:
            if not use_salts:
                password_crack = hashlib.sha1()
                password_crack.update(password.encode("utf-8"))
                cracked_password_hash = password_crack.hexdigest()
                if cracked_password_hash == cracked:
                    return password

            else:
                for salt in salts:
                    pass
                    crack_salt = hashlib.sha1()
                    crack_salt.update(str(salt + hash + salt).encode("utf-8"))
                    cracked = crack_salt.hexdigest()
