from multiprocessing import log_to_stderr
import numbers
import random
import random
#numbers=[1,2,3,4,5,6,7,8,9]
numbers=range(1,46)
lotto = random.sample(numbers,6)
print(lotto)