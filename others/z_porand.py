import sys

def method(n):
    result = None
    stack = []
    
    for val in n:
        print(val)
        if val != "+" or val != "-" or val != "*":
            stack.append(val) 
            print(stack)
    
    return result

if __name__ == '__main__':
    print(method(sys.argv[1:]))