import sys
inputs = sys.stdin.readlines()

vars = {}
vals = {}

def define(arr):
    var, val = arr
    vars[var] = int(val)
    vals[int(val)] = var
    # print(vars)
    # print(vals)

def calculate(arr):
    query_val = 0
    cmds = ['+'] + arr
    for i in range(0, len(arr), 2):
        cmd = cmds[i]
        var = cmds[i+1]
        if var not in vars:
            display(arr, 'unknown')
            return
        val = int(vars.get(var))
        if cmd == '+':
            query_val += val
        else:
            query_val -= val
    if query_val not in vals:
        display(arr, 'unknown')
        return
    ret_str = vals.get(query_val)
    display(arr, ret_str)

def display(arr, ret):
    out = ''
    for e in arr:
        out += e + ' '
    out += ret
    print(out)

def clear():
    vars = {}
    vals = {}

for input in inputs:
    line = input.split()
    command = line[0]
    if command == 'def':
        define(line[1:])
    elif command == 'calc':
        calculate(line[1:])
    else:
        clear()