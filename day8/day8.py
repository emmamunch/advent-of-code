import numpy as np

class Program:
    def __init__(self):
        self.accumulator = 0
        self.pc = 0
        self.prev_pc = -1

    def exec_inst(self, inst):
        self.prev_pc = self.pc
        if inst[0] == 'jmp':
            if '+' in inst[1]:
                self.pc += int(inst[1][1:])
            else:
                self.pc += int(inst[1])
            return
        elif inst[0] == 'acc':
            if '+' in inst[1]:
                self.accumulator += int(inst[1][1:])
            else:
                self.accumulator += int(inst[1])
        self.pc += 1


def day8():
    with open('day8input.txt', 'r') as f:
        content = f.read()

    content = content.split('\n')
    executed = {}

    p = Program()

    while p.pc not in executed:
        inst = content[p.pc].split(' ')
        executed[p.pc] = 1
        p.exec_inst(inst)
    print('part 1', p.accumulator)
    start = p.pc

    # find all the possible jumps in repeating section so can interchange swapping them
    jumps = []
    while executed[p.pc] < 2:
        inst = content[p.pc].split(' ')
        executed[p.pc] += 1
        if inst[0] == 'jmp':
            jumps.append(p.pc)
        p.exec_inst(inst)

    # have to reset accumulator to the non-repeat section
    p2 = Program()   
    while p2.pc != start:
        inst = content[p2.pc].split(' ')
        p2.exec_inst(inst)
    acc_start = p2.accumulator

    # swap out one jump at a time, starting from state before infinite loop starts
    for j in jumps:
        executed = {}
        stopped = False
        while p2.pc != len(content):
            if p2.pc not in executed:
                executed[p2.pc] = 1
            else:
                stopped = True
                break
            if p2.pc == j:
                inst = content[j].replace('jmp', 'nop').split(' ')
            else:
                inst = content[p2.pc].split(' ')
            p2.exec_inst(inst)

        if not stopped:
            return p2.accumulator
        else:
            p2.accumulator = acc_start
            p2.pc = start
    return -1


print('part 2', day8())


