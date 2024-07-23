def encode(password):
    nums = []
    for i in password:
        num = int(i) + 3
        nums.append(str(num))
    new_pass =
    print(nums)

def decode(password):
    decoded = ''
    for i in range(len(password)):
        n2 = int(password[i])
        nn2 = (n2 - 3) % 10
        decoded += str(nn2)
    return decoded


def main():
    encode('12345555')

main()