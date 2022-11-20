# 7. Conversia unui string de forma "1.234.567,89 Lei" la un float de forma 1234567.89.
def str_to_float(v):
    return float(v.replace('.', '').replace(',', '.').replace('Lei', ''))

def str_to_float_2(v):
    var = v.replace('.', '').replace(',', '.').replace('Lei', '')
    if var.isnumeric():
        return float(var)
    else:
        return False

#
#
print(str_to_float_2("1.234.567,89 Lei"))
