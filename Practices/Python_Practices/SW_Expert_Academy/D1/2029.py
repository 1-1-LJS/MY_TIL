def quotient_remainder(num1, num2):
    quotient = num1 // num2
    remainder = num1 % num2
    
    return f"{quotient} {remainder}"

if __name__ == "__main__":
    for idx in range(int(input())):
        num1, num2 = map(int, input().split())
        print(f"#{idx+1} {quotient_remainder(num1, num2)}")