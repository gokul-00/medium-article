import time
passwd = "t1e2"
userInput = input()  # user input : t1e2
t = time.time()
print(userInput == passwd)  # True
print(f'{(time.time() - t)*1000} ms')  # 0.04291534423828125ms
