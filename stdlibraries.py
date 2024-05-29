#Here we discuss library & Modules .. some modules build in and some ..

print(dir())
for i in dir():
    print(i)

for j in (dir(__builtins__)):
    print(j)


from turtle import *
color("blue","pink")
begin_fill()
left(140)
forward(111.65)
for i in range(200):
    right(1)
    forward(1)
left(120)
for i in range(200):
    right(1)
    forward(1)

forward(111.65)
end_fill()
done()


