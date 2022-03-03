def is_assertion(line):
    return line.startswith('assert')


def get_assertion_method(line, all_lines):  # TODO: Check for variable which stores a method result
    asserted_entity = line[line.find(' '):line.find('==')].strip()
    if '(' not in asserted_entity:  # variable tested
        for line in all_lines:
            if line.startswith(f'{asserted_entity} ='):
                return line[line.find(' ') + 2:line.find('(')]
    else:
        return line[line.find(' '):line.find('(')]  # From first space after assert until the function call
