#import requests
#response = requests.get('http://localhost:81')
#if response.status_code == 200:
#    print('Web site exists')
#else:
#    print('Web site does not exist') 

#import webbrowser
#webbrowser.open('http://localhost:81')  # Go to example.com

import urllib.request

# This variable contain the request on 'http://localhost:1234/'.
# You must wondering what is 'http://localhost:1234'?
# localhost: This means that the server is local.
# 1234: Remember we define 1234 as the server port.

#fp = urllib.request.urlopen("http://localhost:81/")
fp = urllib.request.urlopen("http://localhost:81/")
print('done!!!!')