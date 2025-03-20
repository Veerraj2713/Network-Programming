import subprocess

nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
decoded_nw = nw.decode('ascii')
print(decoded_nw)


#ntsh - net shell is a command used to display network available in region