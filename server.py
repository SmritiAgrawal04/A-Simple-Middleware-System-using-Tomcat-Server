import threading
import sys 

class Server:
    def rpc_sub(self, *args):
        diff= args[0]
        
        for i in range (1, len(args)):
            diff -= args[i]
            
        return str(diff)

    def rpc_multiply(self, *args):
        sum= args[0]
        
        for i in range (1, len(args)):
            sum *= args[i]
            
        return str(sum)

    def rpc_modulo(*args):
        return str(args[0]%args[1])

    #process the required function names and their types to call the function defined in server
    def process_string(self, line):
        list= line.split(':')
    #    print (list)
        func= "self." str(list[0]) +"("
    #    print (func_name)
        
        for i in range (1, len(list)):
            l= str(list[i]).split('\'')
    #        print (l)
            d_type= str(l[1])
    #        print (d_type)
            func += d_type +"("
            l= str(l[2]).split('-')
    #        print (l)
            value= str(l[1])
            func += value + "),"
    #        print (value)
    #        print()
        
        func = func[:-1]
        func += ")"        
        print ("function= ", func)  
        result= eval(func)
        print (result)
        print()
        return result



