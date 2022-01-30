#!/bash/python3

import sys
import socket
from datetime import datetime

start_time = datetime.now()

if len(sys.argv) != 6:
    print("python3 portScanner.py <ip> -s <startport> -e <endport>")
    sys.exit(0)


def scan(ip_address, port_number):
    if not ip_address:
        return 0

    if not port_number:
        return 0

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Timeout in seconds
    result = tcp.connect_ex((ip_address, port_number))  # returns an error indicator => 0:success, 1:error
    tcp.close()

    if result == 0:
        return 1
    else:
        return 0


print(r"""\
        ╓░▒▒╦╗
        jÜ¢¢╩╩▒_               r▒▒Ü¢¢Ä¢ÄÄÄ▒╗╓r                     ╓░░▒▒Ä▒⌐
       j¢╩¢▒R╚ºªÜ▒mr╖╓╓.    ºΓ          º╚¢╩¢¢▒╗▒▒╓        ╓    ╖▒▒╝¢¢¢¢¢╩¢¢▒
      ºº╚ªº        j╚╩¢¢Ä=       ╖r▒▒▒▒▒▒m╓º¢╩¢╩¢¢¢¢¢¢▒▒▒Ü¢╩¢¢¢¢¢¢¢╝╩╩¢╩¢╩¢╩░
      ┌¢▒▒Ü░r▒▒▒»╓▒╝¢╩¢ª      ╓▒Ü╩¢¢¢╩¢¢¢¢¢¢▒╝¢╩¢╩¢╩¢╩¢¢¢╝¢╩¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢░r░═
      ¢╩¢¢╩¢¢¢¢¢¢¢¢╩╩╩▒      ▒Ü¢╩╩¢╩╩╩╩╩¢╩¢╩¢╝¢╩¢░º╝¢╩╩╩¢╩¢╩╩╩¢╩¢╩¢╩╩╩╩╩¢╩¢╩╩¢¢▒R
        «╩¢╩¢╩¢╩╩╩¢╩¢▒      ▒Ö╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╩╩Γ  ªºº ¢╩¢╩¢╩¢╩╩╩¢╩¢╩¢╩¢╩╩╩¢╩¢▒
        º▒╝╩¢╩¢╩¢╩╩╩¢▒     ▐Ü╝¢╝¢╩╩╩¢╩¢╩¢╩╩╩¢ª╙º      ╔▒╝╩╩╩¢╩¢╩¢╩╩╩¢╩¢╩¢╩╩╩¢╩¢¢▒
      º¬²ê╩╩¢╩¢╩¢╩¢╩¢░      ¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢¢▒▒▒¬     ²╩╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢░
        ª╝¢╩¢╩¢╩¢╩¢╩╩¢      j╝¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢¢¢Γ «Ä▒▒▒╝╝¢╩¢╩¢╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╝¢╓_
         «¢╩¢╩¢╩¢╩¢╩¢╩▒      º╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩¢╩¢░▒Ö¢¢¢¢¢╩╩╩¢╩¢╩¢╩¢╩¢╩╩╩¢╩╩╩¢╩¢╩▒╝▒.
          j╝╩╩¢╩¢╩¢╩╩╩¢▒╖      º¢╩╩╩¢╩¢╩¢╩╩╚j▒╝╩¢Ä¢╝¢╝¢╩¢╩¢╩╩╩¢╩¢╩╩¢¢╩▒╚╙ºΓ
            │¢╚╝╩╩¢╩¢╩¢▒╝▒╗         ºººº  ╓▒╝¢╩╩╩╩¢╩¢╩¢▒╚▒╝╩╩╩╩=º
                 ╩¢╩╩╩¢¬    º!r╗╓   ╓╖r   ╙==  j╩  ╙º
                  ╙ºº └       └¢¢¢▒Ä=º        ¢╩ª
""")

try:

    target = sys.argv[1]
    if not target:
        print("Invalid target!")
        sys.exit()

    startport = sys.argv[sys.argv.index('-s') + 1]
    if not startport:
        print("Invalid startport!")
        sys.exit()

    endport = sys.argv[sys.argv.index('-e') + 1]
    if not endport:
        print("Invalid endport!")
        sys.exit()

    target = socket.gethostbyname(target.strip())
    startport = int(startport.strip())
    endport = int(endport.strip())

    if startport < 1 or endport < 1 or startport > endport:
        print("Invalid port arguments!")
        sys.exit()

    for port in range(startport, endport):
        if scan(target, port):
            print(f"Port {port} open")

except KeyboardInterrupt:
    print("\nExiting... Keyboard Error")
    sys.exit()
except IndexError:
    print("\nExiting... Index Error")
    sys.exit()
except socket.gaierror:
    print("The hostname couldn't be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to the server.")
    sys.exit()

end_time = datetime.now()
total_time = end_time - start_time

print("Total time: ", total_time)
