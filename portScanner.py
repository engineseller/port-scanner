#!/bash/python3

import sys
import socket
import datetime

help="""---------------- PORT SCAN ---------------
	python3 portScanner.py <ip> -s <startport> -e <endport>
	"""

if len(sys.argv) != 6:
	print(help)
	sys.exit(0)

try:

    target = socket.gethostbyname(sys.argv[1].strip())
    startport = int(sys.argv[sys.argv.index('-s')+1].strip())
    endport = int(sys.argv[sys.argv.index('-e')+1].strip())
    
    if (startport < endport):
      print("Invalid amount of arguments!")

    # adding a basic banner
    print("-" * 20)
    print("Scanning target: " + target)
    print("Time started: " + str(datetime.datetime.now()))
    print("-" * 20) 
  
    for port in range(startport, endport:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifying the address family and socket type
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # returns an error indicator => 0:success, 1:error
    
        if (result == 0):
            print(f"Port {port} open")
        else:
            print(f"Port {port} closed")
            
        s.close()    #close the connection
    
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
    
except socket.gaierror:
    print("The hostname couldn't be resolved.")
    sys.exit()
    
except socket.error:
    print("Couldn't connect to the server.")
    sys.exit()   
