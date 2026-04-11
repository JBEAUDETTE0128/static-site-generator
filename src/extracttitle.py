def extract_title(markdown):
    lines = markdown.split('\n')
    extraction = ""
    for line in lines:
        if line.startswith('# '):
            extraction = line
    if extraction is "":
        raise ValueError("Error: Header One Not Found")
    return extraction[2:].strip()