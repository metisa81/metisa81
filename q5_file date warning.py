try :
    f= open("test text.txt","r")
    f.close()
except :
    f= open("test text.txt","a")
    f.write("")
    f.close()
# file date warning
import datetime
from datetime import date

while True :
    put = input("1)see work list\n2)add\n3)edit\n4)All delete\n5)Marking a line\n6)Delete a line mark\n7)delete a line\n8)exit\nselect please :")
    # s  is for see file 
    
    if put == "1" :
        numberline = 0
        f= open("test text.txt","r")
        for line in f :
            numberline +=1
        f.close()
        tek =0   
        f= open("test text.txt","r")
        for line in f :
           import datetime
           t1 = datetime.datetime.now()
           from datetime import datetime, date
           from datetime import datetime
           line_string = str(line)
           title1 = line_string.find(":")
           title2 = line_string.find("|")
           time1 = line_string.find("=")
           time2 = line_string.find("!")
        
           title = ""
           year1 = ""
           for i in range(len(line_string)) :
               if title1 < i < title2 :
                   title = title + line_string[i]
           for n in range(len(line_string)):
                if time1 <n < time2 :
                    year1 = year1 + line_string[n]
            
           t2 = datetime.strptime(year1 , "%Y-%m-%d %H:%M:%S")
           dt = t2 -t1
           
           f= open("test text.txt","r")
           lis = f.readlines()
           asd = line_string[0]
           
           
           add_setare = ""
           if line_string[0]== "*":
               add_setare = add_setare + "* "
     

           
           f= open("test text.txt","r")
           lis = f.readlines()
           lis[tek]= add_setare+str(tek+1) +")" +"title:{}| date={}! | remaining time:{}\n".format(title,str(t2),str(dt))
           f = open("test text.txt","w")
           f.writelines(lis)
           f.close()
           
           tek +=1
           if tek == numberline :
               break
           
           
           
        f.close()
        
        f= open("test text.txt","r")
        for line in f :
            print(line) 
        
        
         


    # a  is for add 
    if  put == "2" :
        #input text title
        title = input("enter your text title:")
        # input time and dt
        import datetime
        t1 = datetime.datetime.now()
        from datetime import datetime, date
        from datetime import datetime
        year1 = str(input("enter date(example:2022/3/4 14:30):"))
        t2 = datetime.strptime(year1 , "%Y/%m/%d %H:%M")
        dt = t2 -t1
        # add to file
        f= open("test text.txt","a")
        f.write("title:{}| date={}! | remaining time:{}\n".format(title,str(t2),str(dt)))
        f.close()

    #  selecting
    if put == "5" :
        # input line namber
        linenumber = int(input("Whach line do you want to tik:"))
        

        # edit title
        f= open("test text.txt","r")
        lis = f.readlines()
        sre =lis[linenumber-1]
        lis[linenumber-1]= "* " + sre
        f = open("test text.txt","w")
        f.writelines(lis)
        f.close()



    # 3  is for editing
    if put == "3" :
        # input titel and line namber
        linenumber = int(input("Whach line do you want to edit:"))
        title = input("enter your text title:")

        # input time and dt
        import datetime
        t1 = datetime.datetime.now()
        from datetime import datetime, date
        from datetime import datetime
        year1 = str(input("enter date(example:2022/3/4 14:30):"))
        t2 = datetime.strptime(year1 , "%Y/%m/%d %H:%M")
        dt = t2 -t1

        # edit title
        f= open("test text.txt","r")
        lis = f.readlines()
        lis[linenumber-1]= "title:{}| date={}! | remaining time:{}\n".format(title,str(t2),str(dt))
        f = open("test text.txt","w")
        f.writelines(lis)
        f.close()

        

    #all deleting
    if  put == "4" :
        title = ""
        f= open("test text.txt","w")
        f.write(title)
        f.close()

    #delete a line   
    if put == "7" :
        linenumber = int(input("Whach line do you want to delete:"))
        linenumber2 = linenumber -1
        f= open("test text.txt","r")
        lis = f.readlines()
        lis[linenumber2]= " "
        f = open("test text.txt","w")
        f.writelines(lis)
        f.close()

    #delete  line   mark
    if put == "6" :
        linenumber = int(input("Whach line do you want to delete mark:"))
        linenumber2 = linenumber -1
        f= open("test text.txt","r")
        lis = f.readlines()
        
        line2_string = lis[linenumber2]
        list_string = list(line2_string)
        list_string[0]= ""
        line_string3 = "".join(list_string)
        lis[linenumber2]= str(line_string3)
        f = open("test text.txt","w")
        f.writelines(lis)
        f.close()

        
        
        f = open("test text.txt","w")
        f.writelines(lis)
        f.close()


    #breaking bad
    if put == "8" :
        break
