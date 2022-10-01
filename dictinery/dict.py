d = {'simple_key':'hello'}
d1 = {'k1':{'k2':'hello'}}
d2 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print(d3['k1'][2]['k2'][1]['tough'][2][0])
def hello():
    print('hello')

d1={'hello':hello(),'ashis':'banerjee'}

print(d1['hello'])

