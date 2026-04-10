def markdown_to_blocks(markdown):
    if markdown is None or markdown == "":
        return []
    if not isinstance(markdown, str):
        raise TypeError("Error: Markdown input must be a string.")
    document = markdown.strip('\n ')
    if document == "":
        return []
    block_strings = []
    while True:
        block = document.split("\n\n", 1)
        if len(block) == 1:
            block = block[0].strip()
            block_strings.append(block)
            return block_strings
        document = block[1].strip('\n ')
        block = block[0].strip()
        block_strings.append(block)