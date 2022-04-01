def is_assertion(line):
    return line.startswith('assert')


def is_sleep(line):
    return line.startswith('sleep')


def starts_try_block(line):
    return 'try:' in line


def starts_except_block(line):
    return 'except:' in line


def get_assertion_method(line, all_lines):
    asserted_entity = line[line.find(' '):line.find('==')].strip()
    if '(' not in asserted_entity:  # variable tested
        for line in all_lines:
            if line.startswith(f'{asserted_entity} ='):
                return line[line.find(' ') + 2:line.find('(')]
    else:
        return line[line.find(' '):line.find('(')]  # From first space after assert until the function call


def get_try_except_block(index_of_try_line, all_lines):
    try_except_block_content = []
    for line in all_lines[index_of_try_line:]:
        try_except_block_content.append(line)
        if starts_except_block(line):
            break
    return try_except_block_content
