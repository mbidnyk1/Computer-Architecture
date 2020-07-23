"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [] * 256
        self.pc = 0
        self.register =  [] * 8
    def ram_read(self, address):
        if self.ram[address] == 0b00000001 or self.ram[address] == 0x01:
            break
        if self.ram[address] == 0b10000010:
            
    def ram_write(self):
        address = 0
        if len(sys.argv) != 2:
            print("usage: cpu.py filename")
            sys.exit(1)
        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    try:
                        line = line.split("#",1)[0]
                        line = int(line, 2)  # int() is base 10 by default
                        self.ram[address] = line
                        address += 1
                    except ValueError:
                        pass
        except FileNotFoundError:
            print(f"Couldn't find file {sys.argv[1]}")
            sys.exit(1)
    
    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = """
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        """

        if len(sys.argv) != 2:
            print("usage: comp.py filename")
            sys.exit(1)
        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    try:
                        line = line.split("#",1)[0]
                        line = int(line, 10)  # int() is base 10 by default
                        memory[address] = line
                        address += 1
                    except ValueError:
                        pass
        except FileNotFoundError:
            print(f"Couldn't find file {sys.argv[1]}")
            sys.exit(1)
        
        for instruction in program:
            self.ram[address] = instruction
            address += 1

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
        # running = True
        # LDI = 10000010 00000rrr iiiiiiii 82 0r ii
        # while running:
        #     if self.ram[pc] == 10000010:

    
        # if 
        # 10000010 # LDI R0,8
        # 00000000
        # 00001000
        # 01000111 # PRN R0
        # 00000000
        # 00000001 # HLT
        # pce = 0
        
        
            

