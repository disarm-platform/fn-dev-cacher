def get_layer_data(req):
    return req
    # Convert `req` into a filename / path
    cached_path = req + ".zip" # TODO: Do this more cross-OS reliably

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
# 2. Interact with cache - get and store files
# 3. Handle downloading (and then cache-storing)
# 4. Extract data from files, depending on req params, and return
