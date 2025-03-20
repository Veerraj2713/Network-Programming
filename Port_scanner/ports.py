#nmap is a library used to scan ports
import nmap

begin = 75
end= 80

target = '127.0.0.1'

scanner = nmap.PortScanner()
for i in range(begin, end+1):
    res = scanner.scan(target, str(i))
    res = res['scan'][target]['tcp'][i]['state']
    print(f'port {i} is {res}')


#if any port is open, it will show open, otherwise it will show closed
#this is a simple port scanner
#it will scan the ports from 75 to 80
#if any of the port is open, then the network is not secure
