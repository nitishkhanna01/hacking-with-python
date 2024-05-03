# pip install python-nmap
import nmap
import socket
open_ports = []
nm = nmap.PortScanner()
domain = input("Enter Target Domain/Ip : ")
domain = domain.replace("https://","").replace("http://","").replace("/","")
try: 
    socket.gethostbyname(domain)
except:
    print("Wrong Domain/Ip!! Try Again")
    exit()
try:
    socket.inet_aton(domain)
    host = domain
except socket.error:
    host = socket.gethostbyname(domain)


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
for port in range(start, end + 1):
    my_scan = nm.scan(host, str(port))
    state = my_scan['scan'][host]['tcp'][port]['state']
    if state == 'open':
        open_ports.append(port)
        service = my_scan['scan'][host]['tcp'][port].get('name', 'Unknown')
        product = my_scan['scan'][host]['tcp'][port].get('product', 'Unknown')
        version = my_scan['scan'][host]['tcp'][port].get('version', 'Unknown')
        print(f'Port {port} is open - Service: {service}, Product: {product}, Version: {version}')
print("\n\n\t\t Scanning For Vulnerabilities")
for port in open_ports:
    try:
        nm.scan(host, arguments=f'-p {port} --script vuln')
        vulnerabilities = nm[host]['tcp'][port]['script'].keys()
        print(f'Vulnerabilities on port {port}: {", ".join(vulnerabilities)}')
    except KeyError:
        pass
