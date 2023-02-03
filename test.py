import os
import sys
import time
import datetime 
import socket
import platform
import subprocess 

from ip2geotools.databases.noncommercial import DbIpCity


def test(arg1 , *vartuple):
           # df = response = DbIpCity.get(ip, api_key='free')
    
            print (arg1)
            
            
            for var in vartuple:
                response = DbIpCity.get(var, api_key='free')
                print (var)
                print (response.city)
            return
                

# Now you can call printme function

test( "40.113.110.67 ", "40.113.110.67", "13.107.5.88")

