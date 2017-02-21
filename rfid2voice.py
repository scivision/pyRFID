#!/usr/bin/env python
from pyrfid import tagreader

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('--dbfn',default='rfid2name.xlsx')
    p.add_argument('-p','--port',help='serial port file ID',default='/dev/ttyUSB0')

    p = p.parse_args()

    tagreader(p.dbfn,p.port)
