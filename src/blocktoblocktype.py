from blocktype import BlockType

def block_to_block_type(markdown_block):
    if markdown_block is None or markdown_block == "":
        raise ValueError("Error: Empty markdown block")
    if is_heading(markdown_block):
        return BlockType.HEADING
    elif is_code(markdown_block):
        return BlockType.CODE
    elif is_quote(markdown_block):
        return BlockType.QUOTE
    elif is_unordered_list(markdown_block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(markdown_block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def is_heading(markdown_block):
    heading_check = markdown_block[:8] # "###### T"
    index = 0
    while heading_check[index] == "#":
        index += 1
        if index > len(heading_check) - 1:
            return False
    if index == 0 or index >= 7:
        return False
    if heading_check[index] != ' ':
        return False
    index += 1
    if heading_check[index] == ' ':
        return False
    return True

def is_code(markdown_block):
    code_check_start = markdown_block[:4]
    if code_check_start != "```\n":
        return False
    code_check_end = markdown_block[-3:]
    if code_check_end != "```":
        return False
    return True

def is_quote(markdown_block):
    quote_check = markdown_block.split('\n')
    for quote in quote_check:
        if quote == "" or len(quote) < 2:
            return False
        if quote[0] != '>':
            return False
        if len(quote) > 2:
            if quote[1] == ' ' and quote[2] == ' ':
                return False
    return True
        
def is_unordered_list(markdown_block):
    unordered_check = markdown_block.split('\n')
    for line in unordered_check:
        if line == "" or len(line) < 2:
            return False
        if line[0] != '-':
            return False
        if line[1] != ' ':
            return False
    return True

def is_ordered_list(markdown_block):
    ordered_check = markdown_block.split('\n')
    index = 0
    for line in ordered_check:
        if line == "" or len(line) < 3:
            return False
        index += 1
        if line[0] != str(index):
            return False
        if line[1] != '.':
            return False
        if line[2] != ' ':
            return False
    return True