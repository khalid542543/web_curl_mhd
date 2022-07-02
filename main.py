from subprocess import Popen, STDOUT, PIPE
from threading import Thread
import sys
 

currentArgument = str(sys.argv[1])

if currentArgument in ("-h", "-help"):
    print ("Displaying Help\n")
    print ("-h help",end="")
    print ("\n-a All scan" ,end="")
    print ("\n-d Target Domain" , end="" )
    print ("\n-s SubDomain takeover" , end="")
   
elif  currentArgument in ("-d"):
   
    p = Popen(['ping',str(sys.argv[2])], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
  
    while p.stdout.readline(): 
        print("\n" , p.stdout.readline().decode().strip())


# while p.poll() is None :
#     i = input("\n")
#     i = i + "\n"
#     i = p.stdin.write(i.encode())
#     p.stdin.flush() 
#     print(p.stdout.readline() , i)
