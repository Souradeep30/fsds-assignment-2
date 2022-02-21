#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""Answer 1:

There are 2 values of Boolean Data Type

True & False
Syntax: True, False"""

a = True
b = False
print('a: ', a)
print('b: ', b)


# In[ ]:


Answer 2:
    
There different types of Boolean operators are:

AND OR NOT


# In[6]:


###Answer 3:
    
list_AND = [1 and 1, 1 and 0, 0 and 1, 0 and 0]
list_AND


# In[7]:


list_OR = [1 or 1, 1 or 0, 0 or 1, 0 or 0]
list_OR


# In[8]:


list_NOT = [not 1, not 0]
list_NOT


# In[ ]:


Answer 4:

1. (5 > 4) and (3 == 5)                   = False
2. not (5 > 4)                            = False
3. (5 > 4) or (3 == 5)                    = True
4. not ((5 > 4) or (3 == 5))              = False 
5. (True and True) and (True == False)    = False
6. (not False) or (not True)              = True  


# In[ ]:


Answer 5:

== : is equal to
get_ipython().system('= : is not equal to')
> : is greater than
>= : is greater than or equal to
< : is less than
<= : is less than or equal to


# In[ ]:


Answer 6:

'= ' : single equals to sign is used for the assignment operation.
' == ' : double equals to sign is used for the equal to condition check.
When we want to assign something (eg. a = 30) we use the assignment operator. whereas when we want to check some condition (eg. 30 == 25) we use the equal to condition check operator.   


# In[9]:


###Answer 7:

spam = 0

if spam == 10:  ## Block 1
    print('eggs')
    
if spam > 5:    ## Block 2
    print('bacon')
else:           ## Block 3
    print('ham')
    
print('spam')
print('spam')


# In[10]:


###Answer 8:

spam = 1

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
    
    


# In[ ]:


Answer 9:

Press Ctrl + C on the command line.
Restart the kernal


# In[ ]:


Answer 10:

Break: It is used to break the loop and exit from the loop
continue: It is used to skip the current iteration of the loop and continue with the next iteration.


# In[11]:


"""Answer 11:

There is no difference"""

for i in range(10):
    print(i, end = ' ')


# In[12]:


for i in range(0, 10):
    print(i, end = ' ')


# In[13]:


for i in range(0, 10, 1):
    print(i, end = ' ')


# In[14]:


###Answer 12:
    
## Using for loop

for i in range(1, 11):
    print(i, end = ' ')


# In[15]:


## Using while loop

i = 1
while i < 11:
    print(i, end = ' ')
    i =i+1
    


# In[ ]:


Answer 13:

import spam
spam.bacon()

