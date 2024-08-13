data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]



def data_structure_sum(*args):
    total_sum = 0
    for arg in args:
       if isinstance(arg, (int, float)):
           total_sum += arg
       elif isinstance(arg, str):
           total_sum += len(arg)
       elif isinstance(arg, (list, tuple, set)):
           total_sum += data_structure_sum(*arg)
       elif isinstance(arg, dict):
           total_sum += data_structure_sum(*arg.items())
       elif arg in none:
           pass
    return total_sum
print(data_structure_sum(data_structure))