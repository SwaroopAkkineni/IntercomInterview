import json

def main():
    with open('customers.txt') as file:
        line = file.readline()
        while line:
            print(line)
            line = file.readline()

if __name__ == "__main__": main()
