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

