import random
def hash_generator(message):
    random.seed(message) 
    hash_value = random.randint(0, 2**16-1)
    return hash_value

msg=input("Enter the message:")
hash_value=hash_generator(msg)

print("Original Message:", msg) 
print("Hash value:", hash_value)

received_msg=input("Enter the received message: ")
received_hash=hash_generator(received_msg) 

print("Received Message:", received_msg)
print("Received Hash value:", received_hash)

if received_hash == hash_value: 
    print("The message has not been modified.")
else:
    print("The message has been modified.")
