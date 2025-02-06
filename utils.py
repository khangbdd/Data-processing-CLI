def compose(nextFunc, currentFunc):
    def fn(data):
        return nextFunc(currentFunc(data))
    return fn

def transpose(lst): return list(map(list, zip(*lst)))