from function import cacher

def handle(req):
    """handle a request to the function
    Args:
        req (str): layer_name
    """
    try:
        layer_data = cacher.get_layer_data(req)
    except Exception as e:
        # TODO: Print error to stderr
        length = len(layer_data)
        return length

