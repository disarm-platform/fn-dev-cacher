# Assume for toy use, req should be one of 'a', 'b' or 'c'
def get_layer_data(req):
    # Return immediately if req is empty, or a number or an object, etc.
    if req not in ['a', 'b', 'c']:
        raise Exception("Invalid req supplied: {0}".format(req))

    # Convert `req` into a filename / path
    filepath = make_filepath(req)
    url = make_url(filepath)

    temp_path = 'tmp1234'
    local_path = temp_path + cached_path

    # Check bucket if path exists
    if bucket.does_path_exist(cached_path):
        bucket.get_file(cached_path, local_path)
    else:
        # Construct URL
        # Download file
        url = "http://example.com/" + path
        
        # Check if successfully downloaded
        download_file(url, local_path)
        
        # Store in cache, check if successfully store
        bucket.store_file(local_path, cached_path)

    # TODO: In the R version we want to 
    return os.read_file(local_path)

# 1. Construct URLs and filepaths from req params
def make_filepath(req):
    filepath = ''
    return filepath

def make_url(filepath):
    url = ''
    return url

# 2. Interact with cache - get and store files
# TODO: Working with zips?
def check_exists(filepath):
    return False

def get_files(filepath):
    files = ['']
    return files

def put_file(filepath):
    return False

# 3. Handle downloading (and then cache-storing)
def download_file(filepath):
    return False

# 4. Extract data from files, depending on req params, and return
def process_file(filepath):
    # unzip
    # read file content
    content = ''
    return content
