import sys
def count_terminal_stations():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    if N== 0:
        print(0)
        return
    stations=[int(x) for x in input_data[1:n+1]
    terminal_count=0
    for i in range(N):
        left_child_idx=2+i+1

        if left_child_idx >=N:
            terminal_count+=1
    print(terminal_count)
if __name__ == "__main__":
    count_terminal_statement()