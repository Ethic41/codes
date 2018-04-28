import re

def validate(filename):
    file_name = re.sub("\W", "_", filename)
    return file_name

if __name__ == '__main__':
    validate(filename)
