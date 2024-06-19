import socket
import nmap

scanner = nmap.PortScanner()

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    if(verbose):
        scanner.scan(target, '1-1024', '-v sS -sV -sC -A -O')
        open_ports = scanner[target]['tcp'].keys()
    else:
        scanner.scan(target, '1-1024', 'sS -sV -sC -A -O')
        open_ports = scanner[target]['tcp'].keys()
    

    print(open_ports)
    


    return(open_ports)