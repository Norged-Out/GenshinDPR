import sys

def mavuika():
    print("Mavuika tests")
    file = open('tests/mavuika.txt', 'r')
    data = file.readlines()
    headers = data[0].strip().split()
    builds = data[1:]
    print("{:<20} {:<20} {:<20} {:<20}".format(headers[0], headers[1], headers[2], headers[3]))
    '''for build in builds:
        build = build.strip().split()
        print(build)
        bName = build[0]
        rawDPR = float(build[1]) * 8 + float(build[2]) + float(build[3])
        avgDPR = float(build[1]) * 4 + float(build[4]) * 4 + float(build[2]) + float(build[3])
        bestDPR = float(build[1]) * 4 + float(build[4]) * 4 + float(build[5]) + float(build[6])
        print(f"{bName}: {rawDPR} {avgDPR} {bestDPR} \n")'''
        

    file.close()


# Main function to handle dynamic function calling
def main():
    user_input = input("Enter the character to call: ").strip()

    # Dynamically call the function using getattr
    func = getattr(sys.modules[__name__], user_input, None)
    if callable(func):
        func()
    else:
        print(f"Function '{user_input}' does not exist or is not callable.")

if __name__ == "__main__":
    main()
