returnedkwargs = {}
    for key, value in kwargs.items():
        if isinstance(value, bool)
            returnedkwargs[key] = not (value)
        elif isinstance(value, (int, float)):
            returnedkwargs[key] = value ** 2
        elif isinstance(value, str):
            returnedkwargs[key] = value[::-1]
        elif isinstance(value, list)
            returnedkwargs[key] = value[::-1]
        elif isinstance(value, tuple)
            returnedkwargs[key] = value[::-1]
        elif isinstance(value, dict)
            returnedkwargs[key] = {v: k for k, v in value.items()}
        else:
            returnedkwargs[key] = value
    
    return returnedkwargs
