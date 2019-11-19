from function import cacher

def handle(req):
    """handle a request to the function
    Args:
        req (str): layer_name
    """

    layer_data = cacher.get_layer_data(req)
    length = len(layer_data)
    return length