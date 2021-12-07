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
        #else error


#def configurable_update():
    #if its already in the dictionary update it as you need if its not then return an error

