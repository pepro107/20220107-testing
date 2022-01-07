
# coding: utf-8

# In[11]:


def Question1(nums,target):
    # easist way is use two for loop
    v1 = -1
    v2 = -1
  
    for i in range(len(nums)):
        v1 = nums[i]
        for j in range(i+1,len(nums)):
            
            v2 = nums[j]
            if (v1+v2) == target:
                return [i,j]
            
    return None


# In[12]:


nums = [2,7,11,15]
target = 9
Question1(nums,target)


# In[13]:


nums = [3,2,4]
target = 6

Question1(nums,target)


# In[15]:


nums = [3,3]
target = 6
Question1(nums,target)


# In[17]:


# i = 1
# 
romanDC = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
    'IV':4,
    'IX':9,
    'XL':40,
    'XC':90,
    'CD':400,
    'CM':900
}

        
        
        


# In[33]:


def Question2(s):
    num = 0
    lengthStr = len(s)
    index = 0
    while(index<lengthStr):
        s1 = s[index]
        s2 = s[index:index+2]
        
        #print((s2))
        if romanDC.get(s2):
            num += romanDC.get(s2)
            index += 1 
        else:
            num += romanDC.get(s1)
        index +=1
    
    
        
    return num


# In[34]:


s = "III"
Question2(s)


# In[35]:


s = "IX"
Question2(s)


# In[36]:


s = "LVIII"
Question2(s)


# In[37]:


s = "MCMXCIV"
Question2(s)


# In[39]:


def Question7(num):
    if num%4 == 0:
        return True
    if num == 1:
        return True
    return False
 


# In[40]:


n = 16
Question7(n)


# In[42]:


n = 5
Question7(n)


# In[43]:


n = 1
Question7(n)

