text_dict={'codingal':2,'is':2,'best':2,'for':2,'codingal':1}
print("The original dictionary:"+str(text_dict))
k=2
res=0
for key in text_dict:
    if text_dict[key]==k:
        res=res+1
print("Frequency of k is :"+str(res))