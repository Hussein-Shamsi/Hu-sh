import itertools
import time
import string

def decrypt_with_partial_key(cipher_text, used_letters, permutation):
    mapping = dict(zip(used_letters, permutation))
    return ''.join(mapping[char] for char in cipher_text)

cipher_text = input("Enter the cipher text (letters only): ").upper()
cipher_text = ''.join([char for char in cipher_text if char.isalpha()])
used_letters = sorted(set(cipher_text))

attempt_count = 0
start_time = time.time()

print("First 5 decryption attempts:")
for permutation in itertools.permutations(string.ascii_uppercase, len(used_letters)):
    decrypted_result = decrypt_with_partial_key(cipher_text, used_letters, permutation)
    print(decrypted_result)
    attempt_count += 1
    if attempt_count == 5:
        break

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Attempts: {attempt_count}")
print("Elapsed time: %.2f seconds" % elapsed_time)
