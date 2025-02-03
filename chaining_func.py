def compose(nextFunc, currentFunc):
    def fn(data):
        return nextFunc(currentFunc(data))
    return fn