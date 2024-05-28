#we will discuss keyword arguments (**kwargs).
#why we need kwargs? when we give unknown number of arguments then problem occue so the soluting of this prob args
#Then anonther problem occur.. if we want to control on our program we want next item first and first item next 
# then how is this possible. becuase through args value or data in tuple form and we unpack tuple through for loop
# so, we used key value form kwargs,

def studentName(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} and value is = {value}")
       


dic_a = {"Sis1":"Tahseen","bro1":"Waqas","myself":"Sheraz","sis2":"Nosheen","sis3":"Madiha"}
studentName(**dic_a)