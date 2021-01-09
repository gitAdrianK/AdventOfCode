import threading

def solve_day_16(input):
    f = open(input, "r")
    input = [int(c) for c in list(f.readline().replace("\n", ""))]
    input *= 10_000     # Disable for p1 result
    length = len(input)
    half = length//2
    third = length//3
    halfs_done = False
    thirds_done = False
    output = [0]*length
    for n in range(100):
        threads = []
        print("Cycle ", n+1, "... ", end="", sep="")
        output[-1] = input[-1]
        for i in range(length-2, -1, -1):
            if i >= half:
                output[i] = (input[i]+output[i+1]) % 10
            elif i >= third:
                if not halfs_done:
                    print("Half done... ", end="")
                    halfs_done = True
                try:
                    output[i] = input[i]+output[i+1]-input[i+i+1]-input[i+i+2]
                except IndexError:
                    output[i] = input[i]+output[i+1]-input[i+i+1]
                output[i] = output[i] % 10
            else:
                if not thirds_done:
                    print("Two thirds done... ", end="")
                    thirds_done = True
                thread = threading.Thread(target=thread_func, args=(i, input, output, length))
                threads.append(thread)
        for thread in threads:
            thread.start()
            thread.join()
        input = output
        output = [0]*length
        halfs_done = False
        thirds_done = False
        print("done.")
    p1 = "".join(str(nr) for nr in input[:8])
    p2 = "".join(str(nr) for nr in input[int(p1):int(p1)+8])
    return (p1, p2)


def thread_func(i, input, output, length):
    new = 0
    pos = i
    should_add = True
    while pos < length:
        if should_add:
            new += sum(input[pos:pos+i+1])
        else:
            new -= sum(input[pos:pos+i+1])
        should_add = not should_add
        pos += 2*(i+1)
    output[i] = abs(new) % 10


# print(solve_day_16("test_input_0.txt"))
# print(solve_day_16("test_input_1.txt"))
# print(solve_day_16("test_input_2.txt"))
print(solve_day_16("input.txt"))
