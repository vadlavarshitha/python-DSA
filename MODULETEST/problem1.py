import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    n = int(input_data[0])
    queue = []
    MAX_SIZE = 5

    for i in range(1, n + 1):
        command = input_data[i].strip().split()
        if not command:
            continue
            
        cmd_type = command[0]

        if cmd_type == "ARRIVE":
            x = command[1]
            if len(queue) >= MAX_SIZE:
                print("Queue Full")
            else:
                queue.append(x)

        elif cmd_type == "SERVE":
            if not queue:
                print("No Customers")
            else:
                queue.pop(0)

        elif cmd_type == "FRONT":
            if not queue:
                print("No Customers")
            else:
                print(queue[0])

        elif cmd_type == "ISEMPTY":
            print(len(queue) == 0)

if __name__ == '__main__':
    solve()