import re

lib ="import requests"

#definition of the function to establish connection to server and retrieve its result from it for client
code_gen = "\n\ndef {}:\n\ts= \"{}\"{}\
\n\tr= requests.get(url= 'http://localhost:8080/hello/sayhello', params= {}\'{}\': s{})\
\n\tprint ('Status= ',r.status_code)\
\n\tprint ('Result= ', r.text)\n\n"
    
def process_string (line):
    list = line.split('\n')
#    print (list)
    list1 = str(list[0]).split('(')
#    print (list1)
    list2= str(list1[1]).split(')')
#    print (list2)
    list3 =str(list2[0]).split(',')
#    print (list3)
#    print (len(list3))
    s= '('
    for i in range (0, len(list3)):
        s += str(chr(i+97))+','
            
    s = s[:-1]
    s += ')'   
#    print (s)
    s= str(list1[0]) +s
#    print (s)
    return s, str(list1[0]), list3



#main (read the incomplete client and creating extentible executable file)       
f = open('/home/smriti/Downloads/apache-tomcat-8.5.50/webapps/hello/WEB-INF/classes/extendible_file.py', "w")

f.write(lib)

pattern= re.compile('^rpc_')
f_input= open("/home/smriti/Downloads/apache-tomcat-8.5.50/webapps/hello/WEB-INF/classes/client.py", "r")

contents= f_input.readlines()
#check for each line in client file if it has made a RPC call
for line in contents:
    if pattern.match(line):
        s, fun_name, list = process_string(line)
#        print (s)
#        print (fun_name)
#        print (list)
        
        args = ""
        
        index= 0
        for i in list:
            g= chr(index+97)
            args += "+\":\"+" + "str(type("+g+"))" + "+\"-\"+" +  "\"" + str(i)+ "\"" 
            index +=1
        print (args)
        
        f.write(code_gen.format(s, fun_name,args, '{', 'query', '}'))
       
f_input.close() 
f_input= open("/home/smriti/Downloads/apache-tomcat-8.5.50/webapps/hello/WEB-INF/classes/client.py", "r")
data= f_input.read()
f.write(data)  
f_input.close()       
f.close()
    



