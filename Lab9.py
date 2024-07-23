def encode(password):
    nums = []
    for i in password:
        num = int(i) + 3
        nums.append(str(num))
    new_pass = ''.join(nums)
    return new_pass

def decode(password):
    decoded = ''
    for i in range(len(password)):
        n2 = int(password[i])
        nn2 = (n2 - 3) % 10
        decoded += str(nn2)
    return decoded


def main():
    active = 'ON'
    while active == 'ON':
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))
        if option == 1:
            og_pass = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif option == 2:
            encoded = encode(og_pass)
            print("The encoded password is {}, and the original password is {}".format(encoded, og_pass))
        elif option == 3:
            active = 'OFF'

main()