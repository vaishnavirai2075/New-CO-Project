instructions_dict = {
    "add": {"type": "R", "opcode": "0110011", "funct3": "000", "funct7": "0000000"},  
    "sub": {"type": "R", "opcode": "0110011", "funct3": "000", "funct7": "0100000"}, #we have made a nested dictionary for each operation specifying its type n everything
    "sll": {"type": "R", "opcode": "0110011", "funct3": "001", "funct7": "0000000"},
    "slt": {"type": "R", "opcode": "0110011", "funct3": "010", "funct7": "0000000"},
    "sltu": {"type": "R", "opcode": "0110011", "funct3": "011", "funct7": "0000000"},
    "xor": {"type": "R", "opcode": "0110011", "funct3": "100", "funct7": "0000000"},
    "srl": {"type": "R", "opcode": "0110011", "funct3": "101", "funct7": "0000000"},
    "or": {"type": "R", "opcode": "0110011", "funct3": "110", "funct7": "0000000"},
    "and": {"type": "R", "opcode": "0110011", "funct3": "111", "funct7": "0000000"},
    "lw": {"type": "I", "opcode": "0000011", "funct3": "010"},
    "addi": {"type": "I", "opcode": "0010011", "funct3": "000"},
    "sltiu": {"type": "I", "opcode": "0010011", "funct3": "011"},
    "jalr": {"type": "I", "opcode": "1100111", "funct3": "000"},
    "sw": {"type": "S", "opcode": "0100011", "funct3": "010"},
    "beq": {"type": "B", "opcode": "1100011", "funct3": "000"},
    "bne": {"type": "B", "opcode": "1100011", "funct3": "001"},
    "blt": {"type": "B", "opcode": "1100011", "funct3": "100"},
    "bge": {"type": "B", "opcode": "1100011", "funct3": "101"},
    "bltu": {"type": "B", "opcode": "1100011", "funct3": "110"},
    "bgeu": {"type": "B", "opcode": "1100011", "funct3": "111"},
    "lui": {"type": "U", "opcode": "0110111"},
    "auipc": {"type": "U", "opcode": "0010111"},
    "jal": {"type": "J", "opcode": "1101111"}
}

#making registers dctionary

registers_dict = {
    "zero": "00000", "ra": "00001", "sp": "00010", "gp": "00011", "tp": "00100",      
    "t0": "00101", "t1": "00110", "t2": "00111", "s0": "01000", "fp": "01000",
    "s1": "01001", "a0": "01010", "a1": "01011", "a2": "01100", "a3": "01101",
    "a4": "01110", "a5": "01111", "a6": "10000", "a7": "10001", "s2": "10010",
    "s3": "10011", "s4": "10100", "s5": "10101", "s6": "10110", "s7": "10111",
    "s8": "11000", "s9": "11001", "s10": "11010", "s11": "11011", "t3": "11100",
    "t4": "11101", "t5": "11110", "t6": "11111"
}

#Binary conversion given by Naveen

def binary_convert(decimal, num_bits):  
    if decimal >= 0:
        binary = bin(decimal)[2:]     #used inbuilt function and removed the first twocharacters
        return binary.zfill(num_bits)
    else:
        binary = bin(decimal & int("1" * num_bits, 2))[2:]    #this is for negative numbers, we represent them using two's complement
        return binary

#making list of each instrction and identifying its type

def assemble(instruction, labels, current_address):
    parts = instruction.replace(",", " ").replace("(", " ").replace(")", "").split()  # first we make a list of the instruction
    
    if parts[0] == 'lw':
        parts[2], parts[3] = parts[3], parts[2]  # this is done to smoothly handle lw operation as we switch in it
    
    instr_type = instructions_dict[parts[0]]["type"] #now we make a variable to determine instruction type
    
    if instr_type == "R":
        return assemble_rtype(parts)
    elif instr_type == "I":
        return assemble_itype(parts, labels, current_address)
    elif instr_type == "S":
        return assemble_stype(parts)
    elif instr_type == "B":
        return assemble_btype(parts, labels, current_address)
    elif instr_type == "U":
        return assemble_utype(parts)
    elif instr_type == "J":
        return assemble_jtype(parts, labels, current_address)
    else:
        return "ERROR"

def assemble_rtype(parts):                              #we map all registers to their corresponding binary code and join it up and return it
    funct3 = instructions_dict[parts[0]]["funct3"]
    funct7 = instructions_dict[parts[0]]["funct7"]
    rd = registers_dict[parts[1]]
    rs1 = registers_dict[parts[2]]
    rs2 = registers_dict[parts[3]]
    opcode = instructions_dict[parts[0]]["opcode"]
    return funct7 + rs2 + rs1 + funct3 + rd + opcode

def assemble_itype(parts, labels, current_address):   #here we need to do binary conversion to get immediate 
    funct3 = instructions_dict[parts[0]]["funct3"]
    rd = registers_dict[parts[1]]                             
    rs1 = registers_dict[parts[2]]
    if parts[3] in labels:                                              #we check for labels here 
        imm = binary_convert(labels[parts[3]] - current_address, 12)
    else:
        imm = binary_convert(int(parts[3]), 12)
    opcode = instructions_dict[parts[0]]["opcode"]
    return imm + rs1 + funct3 + rd + opcode
