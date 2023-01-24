#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Created by: DeAndre Thomas
# IST652: Lab 1 
# Data Used: NBAfile.py
# Date Created: April 21, 2022


# In[ ]:


# Instructions
# For the NBAfile.py program, for each line, create a 
# string using string formatting that puts the team, attendance, 
# and ticket prices into a formatted string. Each line should look something like:
#‘The attendance at Atlanta was 13993 and the ticket price was $20.06’
# Your program should then print these strings instead of the lines. 


# In[33]:


nbafile = open('NBA-Attendance-1989.txt', 'r')


# In[34]:


nbalist=[]
for line in nbafile:
    team, attendance, price = line.split()
    print('The attendance at %s was %s and the ticket price was $%s'%(team, attendance, price))

