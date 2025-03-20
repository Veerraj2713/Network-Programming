from socket import *
import time
startime = time.time()

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    targetIP = gethostbyname(target)
    print('Starting scan on host: ', targetIP)

    #scan reserved ports
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((targetIP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()
print('Time taken:', time.time() - startime)