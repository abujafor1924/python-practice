def main():
    n = int(input("Enter the value of n: "))

    total_sum = 0

    for i in range(1, n + 1):
        total_sum += i ** i

    print(f"The sum of the series {n}^{n} is: {total_sum}")

if __name__ == "__main__":
    main()
