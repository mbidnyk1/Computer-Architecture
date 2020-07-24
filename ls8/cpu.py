"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.pc = 0
        self.reg = [0] * 8
        self.reg[7]= 0xf4
        self.running = False
        self.flag = 0b00000000
        
    
    def ram_read(self,pc):
        return self.ram[pc]
    
    def ram_write(self,command):
        self.ram[self.pc] = command
    
    def load(self):
        """Load a program into memory."""
        if len(sys.argv) != 2:
            print("usage: ls8.py filename")
            sys.exit(1)
        try:
            with open(f'examples/' + sys.argv[1]) as f:
                for line in f:
                    try:
                        line = line.split("#",1)[0]
                        line = int(line, 2)  # int() is base 10 by default
                        # print(repr(line))
                        # print(self.pc)
                        self.ram_write(line)
                        self.pc += 1
                    except ValueError:
                        pass
        except FileNotFoundError:
            print(f"Couldn't find file {sys.argv[1]}")
            sys.exit(1)
        

        # For now, we've just hardcoded a program:

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        self.running = True
        self.pc = 0
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        MUL = 0b10100010
        PUSH = 0b01000101
        POP = 0b01000110
        CMP = 0b10100111
        JMP = 0b01010100
        JNE = 0b01010110
        JEQ = 0b01010101
        #FL bits: 00000LGE
        # print(self.ram)
        # print(self.reg)
        while self.running:
            if self.ram[self.pc] == HLT:
                self.running = False
                break
            elif self.ram[self.pc] == LDI:
                num = self.ram[self.pc + 2]
                # print(num)
                reg_id =self.ram[self.pc + 1]
                self.reg[reg_id] = num
                self.pc += 3
            elif self.ram[self.pc] == PRN:
                reg_id = self.ram[self.pc + 1]
                num = self.reg[reg_id]
                print(num)
                self.pc += 2
            elif self.ram[self.pc] == MUL:
                reg_id = self.ram[self.pc + 1]
                reg_id2 = self.ram[self.pc + 2]
                self.reg[reg_id] = self.reg[reg_id] * self.reg[reg_id2]
                self.pc += 3
            
            elif self.ram[self.pc] == PUSH:
                # print(self.reg[7])
                self.reg[7] -= 1
                reg_id = self.ram[self.pc + 1]
                value = self.reg[reg_id] 
                address_to_push = self.reg[7]
                self.ram[address_to_push] = value 
                # print(self.ram[address_to_push])
                self.pc += 2
                
            elif self.ram[self.pc] == POP:
                address_to_pop = self.reg[7]
                print(address_to_push)
                self.ram[address_to_pop] = value
                reg_id = self.ram[self.pc + 1]
                self.reg[reg_id] = value
                # print(self.reg[7])
                self.reg[7] += 1
                self.pc += 2
            
            elif self.ram[self.pc] == CMP:
                reg_id1 = self.ram[self.pc + 1]
                reg_id2 = self.ram[self.pc + 2]
                if self.reg[reg_id1] == self.reg[reg_id2]:
                    #If they are equal, set the Equal E flag to 1, otherwise set it to 0.
                    self.flag = self.flag | 0b00000001 
                elif self.reg[reg_id1] < self.reg[reg_id2]:
                    #If registerA is less than registerB, set the Less-than L flag to 1, otherwise set it to 0.
                    self.flag = self.flag | 0b00000100
                    # print(self.reg[reg_id1])  
                    # print(self.reg[reg_id2])
                    # print(bin(self.flag)) 
                elif self.reg[reg_id1] > self.reg[reg_id2]:
                    #If registerA is greater than registerB, set the Greater-than G flag to 1, otherwise set it to 0.
                    self.flag = self.flag | 0b0000010
                self.pc += 3

            elif self.ram[self.pc] == JMP:
                reg_id = self.ram[self.pc + 1]
                self.pc = self.reg[reg_id]
                # self.pc += 2

            elif self.ram[self.pc] == JNE:
                if self.flag & 0b00000001 == 0b00000000:
                    reg_id = self.ram[self.pc + 1]
                    self.pc = self.reg[reg_id]
                else:
                    self.pc += 2

            elif self.ram[self.pc] == JEQ:
                if self.flag & 0b00000001 == 0b00000001:
                    reg_id = self.ram[self.pc + 1]
                    self.pc = self.reg[reg_id]
                else:
                    self.pc += 2



            

