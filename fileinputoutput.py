#Here we discuss write opt for writing data into file...
#First we create list of some items, Then we write this list into files and we used w mode mean write mode
bucket = ["Apple","Bnana","Orange"]
with open("Learn-Python/writefile.txt","w") as temp_bucket:
    for fruit in bucket:
        print(fruit, file=temp_bucket)

#Here we have string, we append this data into existing file we used a mode mean append mode
my_String= ["I Am Sheraz Ahmad hailing from Mianwali."]
with open("Learn-Python/writefile.txt","a") as temp_string:
    for into in my_String:
        print(into, file=temp_string)

#Here we used readlines method for reading data from files and then save into another file.
#because in list form data into new files organized in lines by lines. if i used read func which read file or article 
# character wise data write into files at every new lines one by one character (More reasearch in this topic at next time)
with open("Learn-Python/textfile.txt","r") as temp_read:
     save_string =temp_read.readlines()
     
print(save_string)
with open("Learn-Python/writefile.txt","a") as temp_r_w:
    for intro in save_string:
        print(intro, file=temp_r_w)
    