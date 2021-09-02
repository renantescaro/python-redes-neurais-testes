import numpy as np                                                 

x = np.random.normal(size=[1, 5])

# first approach                           
leaky_way1 = np.where(x > 0, x, x * 0.01)                          

# second approach                                                                   
y1 = ((x > 0) * x)                                                 
y2 = ((x <= 0) * x * 0.01)                                         
leaky_way2 = y1 + y2

print(leaky_way1)
print(leaky_way2)