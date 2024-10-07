
__all__ = ["dict_items", "dict_keys", "dict_values"]

_d = {}
dict_items = type(_d.items())
dict_keys = type(_d.keys())
dict_values = type(_d.values())

