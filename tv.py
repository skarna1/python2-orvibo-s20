#!/bin/env python
from orvibo.s20 import S20, discover
import argparse
import logging
import binascii


#logging.basicConfig(level=logging.DEBUG)

class Pistorasia(object):

    def __init__(self, sockets):
        self.pistorasiat = []
        for (name, ip, mac) in sockets:
            self.pistorasiat.append((name, S20(ip, mac)))
    
    def lista(self):
        for pistorasia in self.pistorasiat:
            print (pistorasia[0])

    def get(self, name):
        for pistorasia in self.pistorasiat:
            if pistorasia[0] == name:
                print(pistorasia[0]),
                if pistorasia[1].on:
                    print("ON")
                else:
                    print ("OFF")

    def set(self, name, value):
        for pistorasia in self.pistorasiat:
            if pistorasia[0] == name:
                pistorasia[1].on = value

def parseargs():
    parser = argparse.ArgumentParser(description='Ohjaa pistorasioita')
    subparsers = parser.add_subparsers(help='sub-command help', dest='cmd')
    parser_a = subparsers.add_parser('list', help='list')
    parser_b = subparsers.add_parser('set', help='set')
    parser_c = subparsers.add_parser('get', help='get')
    
    parser_b.add_argument('--name', dest='name',
                          help='Pistorasian nimi', required=True)

    parser_b.add_argument('--on', dest='value', action='store_true', help='set on')
    parser_b.add_argument('--off', dest='value', action='store_false', help='set off')


    parser_c.add_argument('--name', dest='name',
                          help='Pistorasian nimi', required=True)

    args = parser.parse_args()
    return args

def socket_factory():
    sockets = []
    socket_names = {"ac:cf:23:83:73:28": 'tv', "ac:cf:23:82:d9:ae": 'pc'}
    hosts = discover()
    for host in hosts:
        mac = add_colons(binascii.hexlify(hosts[host]['mac']))
        if mac in socket_names:
            sockets.append((socket_names[mac], host, mac))
    return Pistorasia(sockets)

def add_colons(mac):
    return ':'.join(s.encode('hex') for s in mac.decode('hex'))

def main():
    args = parseargs()
    if args.cmd == 'list':
        socket_factory().lista()
    elif args.cmd == 'get':
        socket_factory().get(args.name)
    elif args.cmd == 'set':
        socket_factory().set(args.name, args.value)


if __name__ == "__main__":
    main()
