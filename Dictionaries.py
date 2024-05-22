#Unorderd set of key value pair.
#key alwas immutable 
#best example English or any dictionary when we know about words but dont know about defination or meaning we find value
#dictionary will be in curly braces list in square braces.

dic_a= {"f_name" :"Sheraz" , "last_name":"Ahmad" , "Religion": "Islam"} 
print(dic_a)
print(dic_a["last_name"])
print(dic_a.get("Religion"))

#Note :: at left side we use string or tuple. mean key will always  immutable (not changed)

dic_b = {
         "vechile":"bike",
         "model": "125",
         "color":("Black","Red"),
         "speed":[40,60,80,100],
         "tyre":{"old":"blast", "new":"No blast"}
         }

print(dic_b["color"][1])
print(dic_b["speed"][1])
print(dic_b["tyre"]["new"])

dic_c ={
         "vechile":"car",
         "model": "sazuki",
         "color":("Black","Red"),
         "speed":[40,60,80,100,120,140,160,180],
         "tyre":{"old":"blast", "new":"No blast"}
         }
print(dic_c.items())
p,q,r,s,t =dic_c.items()
print(p)
print(q)
print(r)
print(s)
print(t)

print(dic_c.keys())
a,b,c,d,e = dic_c.keys()
print(a)
print(b)
print(c)
print(d)
print(e)
print(dic_c.values())
