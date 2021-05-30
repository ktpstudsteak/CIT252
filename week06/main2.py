import requests

def print_nested_dict(dict_obj, indent = 0):
    ''' Pretty Print nested dictionary with given indent level  
    '''
    # Iterate over all key-value pairs of dictionary
    for key, value in dict_obj.items():
        # If value is dict type, then print nested dict 
        if isinstance(value, dict):
            print(' ' * indent, key, ':', '{')
            print_nested_dict(value, indent + 4)
            print(' ' * indent, '}')
        else:
            print(' ' * indent, key, ':', value)
def display_dict(dict_obj):
    ''' Pretty print nested dictionary
    '''
    print('{')
    print_nested_dict(dict_obj, 4)
    print('}')

def earthquake_daily_summary():
    """
    This function will read JSON (Javascrip Object Notation) data from the 
    United States Geological Service (USGS) consisting of earthquake data.
    The data will include all earthquakes in the current day.
    
    JSON data is organized into a dictionary.  After reading the data using
    the 'requests' library, this function will print out a list of all
    earthquake locations ('place' attribute) and magnitudes ('mag' attribute).
    Additional information about the format of the JSON data can be found 
    at this website:  

    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
        
    To install the requests library, run:
       If using virtual environment: pip install requests
       If using Windows: py -m pip install requests
       If using Mac: pip3 install requests
    """    
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    data = req.json() # The .json() function will convert the json data from the server to a dictionary

    feat_list : list = data['features']
    prop : list = [pro['properties'] for pro in feat_list]
    places : list = [plc['place'] for plc in prop]
    mag : list = [ma['mag'] for ma in prop]
    
    asdf = lambda list1, list2 : (str.format('Location: {} : Magnitude: {}', list1, list2))
    map_asdf = list(map(asdf, places, mag))

    [print(re) for re in map_asdf]
     
    
        

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 5 TESTS ===========")
earthquake_daily_summary()