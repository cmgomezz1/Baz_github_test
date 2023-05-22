my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["a"]
except KeyError:
    print("That key does not exist")
else:
    print("Everithing is working perfect!!")

my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["hola"]
except KeyError:
    print("That key does not exist")
else:
    print("Everithing is working perfect!!")