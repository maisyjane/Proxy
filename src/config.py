# list of associative arrays
dictionary = {"charcount": "http://charcount.editor.qpc.hal.davecutting.uk|text",
              "wordcount": "http://wordcount.editor.qpc.hal.davecutting.uk|text",
              "vowelcount": "http://vowelcount.40225143.qpc.hal.davecutting.uk|x",
              "andcount": "http://instancesofand.40225143.qpc.hal.davecutting.uk|x",
              "avgwordlength": "http://averagewordlength.40225143.qpc.hal.davecutting.uk|",
              "commacount": "http://commacount.40225143.qpc.hal.davecutting.uk|x"}


def get_url(function_name):
    found = False
    for key in dictionary.keys():
        if key == function_name:
            found = True
            function = dictionary[key].split('|')
            return function[0]
    if not found:
        return "error"


def get_argument(function_name):
    for key in dictionary.keys():
        if key == function_name:
            arg = dictionary[key].split('|')
            return arg[1]


def configurable_update(function, data):
    found = False
    for key in dictionary.keys():
        if key == function:
            found = True
            dictionary[function] = data
    if not found:
        dictionary[function] = data


