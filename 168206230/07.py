list = ["A", "B", "C", "D"]
for i in range(len(list)):    
    if (list[i] !="A") + (list[i] =="D") + (list[i] =="B") + (list[i] !="D") == 1:	           
        print("小偷是"  + list[i])
