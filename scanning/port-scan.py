import socket
import sys
domain = input("Enter Target Domain/Ip : ")
domain = domain.replace("https://","").replace("http://","").replace("/","")
try: 
    socket.gethostbyname(domain)
except:
    print("Wrong Domain/Ip!! Try Again")
    exit()
try:
    socket.inet_aton(domain)
    address = domain
except socket.error:
    address = socket.gethostbyname(domain)

start =input(("Enter Starting Port (BY DEFAULT = 1): "))
if start == "":
    start = 1
else:
    start = int(start)
end =input(("Enter Ending Port (BY DEFAULT = 1024): "))
if end =="":
    end = 1024
else:
    end = int(end)


try:
    print("Scanning started at " + address + " ....")
    print("PORT     Service  Status")
    for port in range(start, end):
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = so.connect_ex((address, port))
        if result == 0:
            service_name = socket.getservbyport(port)
            print(f"{port:<9}{service_name:<9}Open")
        so.close()
    print("ALL OPEN PORTS ARE SCANNED AND LISTED ...")
except :
    print("Keyboard Intrupted / Connection Failed")
    sys.exit()
