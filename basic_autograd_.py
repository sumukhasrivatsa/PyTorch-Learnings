# -*- coding: utf-8 -*-
"""basic autograd .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1djBM7MCSvIZLWwbynI7flVPE2ZDLSyhK
"""

import torch

"""## ***what exactly is requires_grad=True doing??***

it basically tells that whatever new variables or operations are done using any of that tensor values or that tensor itself 
### we need to maintain a COMPUTATION GRAPH for it 
---

so when i say 

`x=torch.tensor(2.,requires_grad=true)`

and then 

`y=x**2+1`

it will make a data structure such that it remembers how we got y from x

"""

x=torch.randn(3,requires_grad=True)

print(x)

y=x**2+1

print(y)

z=y**x-x*y

print(z)

#y.backward() wont work as we need only a single valued scalar for it to work

y=torch.mean(y)

#we got singular value

y.backward()
autograd.grad(retain_graph=True)
#now we have the gradient of the input X 
#we always get the gradients only of the output with respect to the input 

#dy/dx

print(y)

# we get error if we do this twice

#now we can calculate grad 

print(x.grad)


#calculating the gradient of z wrt x
z=torch.mean(z)
z.backward()
print(x.grad)

#again this wont work cuz we are not

## we can stop the gradient tracingusing 
"""
1) required_grad=false
2) x.deatch()
3) with torch.no_grad():
      operations 

"""

"""## **MODEL BUILDING**

Saved intermediate values of the graph are freed when you call .backward() or autograd.grad(). Specify retain_graph=True if you need to backward through the graph a second time or if you need to access saved tensors after calling backward.
"""

weights=torch.ones(5,requires_grad=True)

input=torch.ones(5,requires_grad=False)
input2=torch.ones(5,requires_grad=True)

epoch=4

for i in range(4):
  output=(weights*input).sum()
  output.backward()
  print(input.grad)
  print(weights.grad)

for i in range(4):
  output=(weights*input2).sum()
  output.backward()
  print(input2)
  print(input2.grad)
  print(weights.grad)


  
#we can see that the gradients are adding to the old gradients

##to prevent this we need to make the gradidents reset everytime or every epoch

weights=torch.ones(5,requires_grad=True)

input=torch.ones(5,requires_grad=False)

epoch=4

for i in range(4):
  output=(weights*input).sum()
  output.backward()
  print(input.grad)
  print(weights.grad)

  weights.grad.zero_()
  """
  THIS IS VERY IMPORTANT
  """

###SIMPLE EXAMPLE TO DEMONSTATE HOW IT WORKS

weights=torch.tensor(1.,requires_grad=True)
input=torch.tensor(2.)

#forward pass
y=(weights*input)
y.backward()

print(weights.grad)

