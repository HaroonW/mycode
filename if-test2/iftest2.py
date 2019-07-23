#!usr/bin/python3

ipchk = input("apply an ip address: ") #thisline now prompts theuser forinput
if ipchk == "192.168.70.1": #if a match
    print("looks like the ip address of the gateway was set: " + ipchk + " this is not recommded.")
elif ipchk: #if any datais provided, this will test true
    print("look like the ipaddress was set: " + ipchk) 
    

else: # if data in not provided
    print ("you did not provide input.") 

    
