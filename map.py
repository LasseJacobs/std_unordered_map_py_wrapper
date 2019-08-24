from ctypes import *
lib = cdll.LoadLibrary('./libmap.so')

class c_result(Structure):
    _fields_ = [('value', c_char_p), ('found', c_bool)]

###################
# __init__(self):
lib.new_map.restype = c_void_p;


###################
# empty(self):
lib.m_empty.argtypes = [c_void_p]
        
# size(self):
lib.m_size.argtypes = [c_void_p]
lib.m_size.restype = c_ulong
        
# max_size(self):
lib.m_max_size.argtypes = [c_void_p]
lib.m_max_size.restype = c_ulong


##################
# clear(self):
lib.m_clear.argtypes = [c_void_p]

# set(self, key, value):
lib.m_set.argtypes = [c_void_p, c_char_p, c_char_p]

# erase(self, key):
lib.m_erase.argtypes = [c_void_p, c_char_p]

# swap(self, other_map):
lib.m_swap.argtypes = [c_void_p, c_void_p]


##################
# get(self, key):
lib.m_get.argtypes = [c_void_p, c_char_p]
lib.m_get.restype = c_char_p

# count(self, key):
lib.m_count.argtypes = [c_void_p, c_char_p]
lib.m_count.restype = c_ulong

# find(self, key):
lib.m_find.argtypes = [c_void_p, c_char_p]
lib.m_find.restype = c_result


################
# bucket_count(self):
lib.m_bucket_count.argtypes = [c_void_p]
lib.m_bucket_count.restype = c_ulong
        
# max_bucket_count(self):
lib.m_max_bucket_count.argtypes = [c_void_p]
lib.m_max_bucket_count.restype = c_ulong
        
# bucket_size(self, n):
lib.m_bucket_size.argtypes = [c_void_p, c_ulong]
lib.m_bucket_size.restype = c_ulong
        
# bucket(self, key):
lib.m_bucket.argtypes = [c_void_p, c_char_p]
lib.m_bucket.restype = c_ulong


###############
# load_factor(self):
lib.m_load_factor.argtypes = [c_void_p]
lib.m_load_factor.restype = c_float
        
# max_load_factor(self):
lib.m_get_max_load_factor.argtypes = [c_void_p]
lib.m_get_max_load_factor.restype = c_float
        
# max_load_factor(self, ml):
lib.m_set_max_load_factor.argtypes = [c_void_p, c_float]
        
# rehash(self, count):
lib.m_rehash.argtypes = [c_void_p, c_ulong]

# reserve(self, count):
lib.m_reserve.argtypes = [c_void_p, c_ulong]


###############
# __del__(self):
lib.delete_map.argtypes = [c_void_p]



class std_result(object):
    def __init__(self, value, found):
        self.value = value
        self.found = found 


class std_map(object):
    def __init__(self):
        self.obj = lib.new_map()
    
        
    ## Capacity
    
    def empty(self):
        return lib.m_empty(self.obj)
        
    def size(self):
        return lib.m_size(self.obj)
        
    def max_size(self):
        return lib.m_max_size(self.obj)
        
        
    ## Modifiers
        
    def clear(self):
        lib.m_clear(self.obj)
        
    def set(self, key, value):
        b_key = key.encode('utf-8')
        b_value = value.encode('utf-8')
        lib.m_set(self.obj, b_key, b_value) 
        
    def erase(self, key):
        b_key = key.encode('utf-8')
        lib.m_erase(self.obj, b_key)
        
    def swap(self, other_map):
        lib.m_swap(self.obj, other_map.obj)

    
    ## Lookup        
        
    def get(self, key):              
        b_key = key.encode('utf-8')
        value = lib.m_get(self.obj, b_key)
        
        return value.decode() if value else None 
       
    def count(self, key):
        b_key = key.encode('utf-8')
        return lib.m_count(self.obj, b_key)
        
    def find(self, key):
        b_key = key.encode('utf-8')
        pw_result = lib.m_find(self.obj, b_key)
        
        value = pw_result.value.decode() if pw_result.found else None
        return std_result(value , pw_result.found)
        
        
    ## Bucket Interface
    
    def bucket_count(self):
        return lib.m_bucket_count(self.obj)
        
    def max_bucket_count(self):
        return lib.m_max_bucket_count(self.obj)
        
    def bucket_size(self, n):
        return lib.m_bucket_size(self.obj, n)
        
    def bucket(self, key):
        b_key = key.encode('utf-8')
        return lib.m_bucket(self.obj, b_key)
        
    
    ## Hash Policy
    
    def load_factor(self):
        return lib.m_load_factor(self.obj)
        
    def max_load_factor(self):
        return lib.m_get_max_load_factor(self.obj)
        
    def max_load_factor(self, ml):
        lib.m_set_max_load_factor(self.obj, ml)
        
    def rehash(self, count):
        lib.m_rehash(self.obj, count)
        
    def reserve(self, count):
        lib.m_reserve(self.obj, count)
        
       
    ## Destructor
    
    def __del__(self):
        lib.delete_map(self.obj)
