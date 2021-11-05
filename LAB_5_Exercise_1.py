def calculator(N):
    total = 0
    average = 0
    N = int(input("N = "))
    
    for n in range(1,(N+1)):
         if n % 2 == 1:
          total+= n  
           
         else:
             even =list(a for a in range(2,(N+1),2))
             average+= n
             result = (average) /(N/2) 
    print(f"Sum of odd numbers is : {total}")         
    print(f"Average of even numbers is : {result}")           
       
         

calculator("N")
