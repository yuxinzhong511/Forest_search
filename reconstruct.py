from fetch_data import *
    
def recon():
    cache_file = open(os.path.join(PATH, FORESTS_DATA) , 'r')
    cache_file_contents = cache_file.read()
    forests_dict = json.loads(cache_file_contents)
    cache_file.close()
    return forests_dict