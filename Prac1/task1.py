class MainClass:
    
    def __init__(self):
        self.username = input()
        self.print_hello()
    
    def print_hello(self):
        print(f"Hello, {self.username}")

if __name__ == '__main__':
    MainClass()