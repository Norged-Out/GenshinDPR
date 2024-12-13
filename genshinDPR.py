"""
Author: Pri
Description: A simple script to calculate the 
             damage per rotation (DPR) of a 
             character in Genshin Impact.

so far only made it for Mavuika, prolly will update it later

maybe
"""
import sys

def rank_DPR(numbers):
    """Takes a list of numbers and returns their rankings from highest to lowest."""
    ranked = sorted(numbers, reverse=True)
    rankings = [ranked.index(num) + 1 for num in numbers]
    return rankings

def mavuika():
    print("Mavuika tests")
    file = open('tests/mavuika.txt', 'r')
    data = file.readlines()
    headers = data[0].strip().split()
    
    
    builds = []
    rawDPRS = []
    avgDPRS = []
    idealDPRS = []
    for build in data[1:]:
        build = build.strip().split()
        bName = build[0]
        rawDPR = int(build[1]) * 8 + int(build[2]) + int(build[3])
        avgDPR = int(build[1]) * 4 + int(build[4]) * 4 + int(build[2]) + int(build[3])
        idealDPR = int(build[1]) * 4 + int(build[4]) * 4 + int(build[5]) + int(build[6])
        builds.append(bName)
        rawDPRS.append(rawDPR)
        avgDPRS.append(avgDPR)
        idealDPRS.append(idealDPR)
        # print("{:10} {:<15} {:<15} {:<15}\n".format(bName, rawDPR, avgDPR, idealDPR))

    rawRankings = rank_DPR(rawDPRS)
    avgRankings = rank_DPR(avgDPRS)
    idealRankings = rank_DPR(idealDPRS)

    print("{:10} {:<15} {:<15} {:<15} {:<15} {:<10}\n".format(headers[0], "Raw DPR", "Average DPR", "Ideal DPR", "Rankings", "Score"))
    for i in range(len(builds)):
        a = rawRankings[i]
        b = avgRankings[i]
        c = idealRankings[i]
        final_score = (a + b + c) / 3
        print("{:10} {:<15} {:<15} {:<15} {:<4} {:<4} {:<5} {:<10.2f}\n".format(builds[i], rawDPRS[i], avgDPRS[i], idealDPRS[i], a, b, c, final_score))

    file.close()


# Main function to handle dynamic function calling
def main():
    user_input = 'mavuika' #input("Enter the character to call: ").strip()

    # Dynamically call the function using getattr
    func = getattr(sys.modules[__name__], user_input, None)
    if callable(func):
        func()
    else:
        print(f"Function '{user_input}' does not exist or is not callable.")

if __name__ == "__main__":
    main()
