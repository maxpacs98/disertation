from constants import CAST_KEYWORDS


def is_assertion(line):
    return 'assert' in line


def is_sleep(line):
    return line.startswith('sleep') or line.startswith('await asyncio.sleep')


def is_print(line):
    return line.startswith('print')


def is_annotation(line, annotation_name):
    return line.startswith(annotation_name)


def starts_try_block(line):
    return 'try:' in line


def starts_except_block(line):
    return 'except:' in line


def get_assertion_method(line, all_lines):
    # TODO: refactor this maybe using recursion
    asserted_entity = line[line.find(' '):line.find('==')].strip()
    if '(' not in asserted_entity:  # variable tested
        if '.' in asserted_entity:
            asserted_entity = asserted_entity.split('.')[0]
        for line in all_lines:
            if line.startswith(f'{asserted_entity} ='):
                return line[line.find(' ') + 2:line.find('(')].strip()
    else:
        first_call = line[line.find(' '):line.find('(')]  # From first space after assert until the function call
        if first_call in CAST_KEYWORDS:
            if '(' not in asserted_entity:  # cast variable tested
                if '.' in asserted_entity:
                    asserted_entity = asserted_entity.split('.')[0]
                for line in all_lines:
                    if line.startswith(f'{asserted_entity} ='):
                        return line[line.find(' ') + 2:line.find('(')].strip()
            return line[line.find('('):line.rfind(')')]  # cast method tested


def get_try_except_block(index_of_try_line, all_lines):
    try_except_block_content = []
    for line in all_lines[index_of_try_line:]:
        try_except_block_content.append(line)
        if starts_except_block(line):
            break
    return try_except_block_content


def contains_numeric_literals(assert_line):
    assertion_elements = assert_line.split('==')
    for el in assertion_elements:
        el = el.strip()
        try:
            int(el)
            float(el)
            return True
        except ValueError:
            pass
    return False
