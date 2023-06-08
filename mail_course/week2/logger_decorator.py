import random as rnd

def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result =  func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write('Execute '+ str(func)+'\n')
                f.write(str(result))
            return result
        return wrapped
    return decorator

@logger('sum_log.txt')
def summator(num_lst):
    return sum(num_lst)

n_lst = [rnd.randint(0,100) for i in range(10)]

print(n_lst)
summator(n_lst)

with open('sum_log.txt', 'r') as f:
    print(f.read())

        
                