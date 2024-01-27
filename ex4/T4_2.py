class RoseDictionary:
    def __init__(self, initial_data=None):
        self._data = initial_data or {}
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __setitem__(self, key, value):
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def keys(self):
        return list(self._data.keys())
    
    def values(self):
        return list(self._data.values())
    
    def items(self):
        return list(self._data.items())
    
    def pop_item(self, raise_error=None, error_msg=None, default=None):
        x = len(self.keys()) - 1
        if x == -1:
            if raise_error == True:
                if error_msg != None:
                    print('KeyError: \'{}\''.format(error_msg))
                elif error_msg == None:
                    print('KeyError: \'error_msg\'')
            else:
                if default != None:
                    return default
                else:
                    if error_msg != None:
                        print(error_msg)
                    else:
                       print('Dictionary was empty and no default value/message was specified.')
        else:
            b = self.keys()[x]
            a = self.values()[x]
            self.__delitem__(b)
            return a
    
    def get_item(self, key, raise_error= None, error_msg= None, default= None):
        try:
            return self._data[key]
        except KeyError:
            if raise_error == True:
                if error_msg != None:
                    print('KeyError: \'{}\''.format(error_msg))
                elif error_msg == None:
                    print('KeyError: \'error_msg\'')
            else:
                if default != None:
                    return default
                else:
                    if error_msg != None:
                        print(error_msg)
                    else:
                       print('Value was not found and no default value/message was specified.')

    
        
    
d = RoseDictionary()
d["key1"] = "value1"
d["key2"] = "value2"
print(d["key1"])
print(d.get_item("key1"))
print(d.get_item("key3", default = "Default Value"))
d.get_item("key3")
print(d.pop_item())
print(d.get_item("key1", error_msg = "error message"))
print(d.get_item("key2", error_msg = "error message2"))
d.pop_item()
d.get_item("key3", default = "Default Value", raise_error = True, error_msg = "Hi")


