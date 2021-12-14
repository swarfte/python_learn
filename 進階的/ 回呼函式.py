# def test(arg):
#     arg("hello") #call Callback function , can give parameter 

# def handle(data):
#     print(data)

# #Callback function 
# test(handle)

def add(n1,n2,cb):
    cb(n1+n2)
    
def handel1(result):
    print("result is :",result)

def handel2(result):
    print("結果  :",result)
    
#this simple example for use callback function
add(3,4,handel1) #we can use handel1 to obtain the chinese result
add(4,5,handel2) #we also use handel2 to obtain the english result