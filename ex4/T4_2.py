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
        if not self._data:
            self._handle_error(raise_error, error_msg, default)
        else:
            key = self.keys()[-1]
            value = self.values()[-1]
            self.__delitem__(key)
            return value

    def get_item(self, key, raise_error=None, error_msg=None, default=None):
        try:
            return self._data[key]
        except KeyError:
            self._handle_error(raise_error, error_msg, default)

    def _handle_error(self, raise_error, error_msg, default):
        if raise_error:
            if error_msg:
                raise KeyError(f"KeyError: '{error_msg}'")
            else:
                raise KeyError("KeyError: 'error_msg'")
        else:
            if default is not None:
                return default
            else:
                if error_msg:
                    print(error_msg)
                else:
                    print("Error: No default value/message specified.")


# Example usage:
d = RoseDictionary()
d["key1"] = "value1"
d["key2"] = "value2"

print(d["key1"])
print(d.get_item("key1"))
print(d.get_item("key3", default="Default Value"))
d.get_item("key3")
print(d.pop_item())
print(d.get_item("key1", error_msg="error message"))
print(d.get_item("key2", error_msg="error message2"))
d.pop_item()
d.get_item("key3", default="Default Value", raise_error=True, error_msg="Hi")
