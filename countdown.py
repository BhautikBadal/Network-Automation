import time

print("Starting countdown...")
for i in range(20, 0, -1):
    print(i)
    time.sleep(1)   # Delay for 1 second
print("Stage Completed!!!")
