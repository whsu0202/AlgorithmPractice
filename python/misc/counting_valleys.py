import re
import sys

# https://www.hackerrank.com/challenges/counting-valleys/problem
def countingValleys(steps, path):
    location=1
    valley=0

    for x in path:
        print(x)
        if x=="U" and location==-1:
            location+=2
        elif x=="U" and location!=-1:
            location+=1
            print("PPP111")
        elif x=="D" and location==1:
            location-=2
            print("MMM222")
            valley+=1
        elif x=="D" and location!=1:
            location-=1
            print("MMMM111")

        print(location)
        print("---------")
            
    return valley

if __name__ == '__main__':

    
    result = countingValleys(12, "DDUUDDUDUUUD")
    print("==========")
    print(result)
