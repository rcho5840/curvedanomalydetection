import splitfolders

def split(input, output):
    splitfolders.ratio(input, output = output, seed = 1337, ratio = (.7, .2, .1), group_prefix = None)