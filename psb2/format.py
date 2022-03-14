import itertools

def objects2lines(objects):
    lines = []
    for object in objects:
        if isinstance(object, list):
            lines.append(str(len(object)))
            lines.append(' '.join(map(str, object)))
        else:
            lines.append(str(object))
    return lines

def disnumerate_prefix(data, prefix):
    lines = []
    for line_number in itertools.count(start=1):
        try:
            lines.append(data[f'{prefix}{line_number}'])
        except KeyError:
            break
    return lines

def format_test_case(test_case, format):
    """
    Represents a test case in one of 3 formats: 'psb2', 'lists' or 'competitive'

    'psb2' format is a dictionary with keys 'input{i}' and 'output{i}'
        indicating ith input and output, respectively.
        Ex: {'input1': 1, 'input2': 2, 'output1': 'output'}
    'lists' format is a list of tuple of the form (input, output)
        where input and output are lists of objects.
        Ex: [(1, 2), ('output')]
    'competitive' format is the defacto standard format in competitive programming.
        It has the same structure as 'lists', but all inputs and outputs are strings
        corresponding to input and output lines
        Besides, every array/list input/output is represented with 2 lines:
        array length and array elements
    """

    if format == 'psb2':
        return test_case
    else:
        input_objs, output_objs = (disnumerate_prefix(test_case, prefix) 
                                   for prefix in ('input', 'output'))

        if format == 'lists':
            return (input_objs, output_objs)
        elif format == 'competitive':
            return (objects2lines(input_objs), objects2lines(output_objs))

    raise ValueError(f'Unknown format: {format}')