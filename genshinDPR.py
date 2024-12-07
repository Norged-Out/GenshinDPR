import sys

def mavuika():
    print("mavvvvv")

# Main function to handle dynamic function calling
def main():
    user_input = input("Enter the function name to call (e.g., 'mavuika'): ").strip()

    # Dynamically call the function using getattr
    func = getattr(sys.modules[__name__], user_input, None)
    if callable(func):
        func()
    else:
        print(f"Function '{user_input}' does not exist or is not callable.")

if __name__ == "__main__":
    main()
