'''Stores increasing(+1) numbers in filename'''
def get_var_value(filename):
    with open (filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val
    pass



#your_counter = get_var_value()
#print("This script has been run {} times.".format(your_counter))
