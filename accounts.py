#!/usr/bin/env python
# coding: utf-8

# In[28]:


account_number = input("Please enter a value: ") # Prompting user to enter account number


# In[29]:


num_leading_digits = len(account_number)-4 # Creating a variable to calculate number of leading digits before the last 4 digits


# In[30]:


print(num_leading_digits) # printing the number of leading digits for validation


# In[33]:


four_digits = account_number[-4:] # Creating variable to identify 4 ending digits of account number


# In[34]:


print(four_digits) # Printing the last four digits for validation


# In[35]:


lead_x = num_leading_digits * "X" # Creating variable to mask the number of leading digits with 'X'


# In[36]:


print(lead_x) # Printing the number of X's for validation


# In[37]:


encrypted_acc_num = lead_x + four_digits # creating the encrypted account number by adding the lead_x and four_digits


# In[38]:


print(encrypted_acc_num) # Printing the calculated variable for validation


# In[ ]:




