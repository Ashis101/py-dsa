
# def hello(*args):
#     for i in args:
#         print(list[i])

def hello(**kwargs):
    f=kwargs['fruits']
    print(f'fav fruits is{f} and i have a ')


hello(fruits="apple",pet='dog')

