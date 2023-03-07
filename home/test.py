x = ['a', 'b', 'c', 'd', 'e', 'h']
z = {'1':'v','2':'y','3':'z', '4':'r'}
def check(*args, **kwargs): 
    for i in x:
        if i in z.values():
            return True
        return False
            
print(check(x,z))