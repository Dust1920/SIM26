import os

path_base = os.getcwd()


def searcher(filename, path, **kwargs):
    file_type = kwargs.get('type',None)
    files = os.listdir(path)
    if file_type != None:
        filename = filename + '.' + file_type
    try:
        index = files.index(filename)
        path = files[index]
        return path
    except:
        for l in files:
            try:
                if l.index('.'):
                    continue
            except:
                if l == "__pycache__":
                path = '..' + searcher(filename, path)
        
        
