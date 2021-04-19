import os, sys

osname = os.uname()[0] + ' ' + os.uname()[1]
arch = os.uname()[4]
kernel = os.uname()[2]
def uptime():
    time = int(float(open('/proc/uptime').read().split(' ')[0]) - (float(open('/proc/uptime').read().split(' ')[0]) % 1))
    d = int(time / 86400)
    h = int(time / 3600 % 24)
    m = int(time / 60 % 60)

    uptime = ''
    if d > 1:
        uptime += str(d) + ' days '
    if h > 1:
        uptime += str(h) + ' hours '
    if m > 1:
        uptime += str(m) + ' mins '
    return uptime
encoding = os.device_encoding(0)
pythonv = sys.version[0] + sys.version[1] + sys.version[2] + sys.version[3] + sys.version[4] + sys.version[5]
cpu_number = os.cpu_count()

print('OS:', osname)
print('Architecture:', arch)
print('Kernel:', kernel)
print('Uptime: %s' % uptime())
print('Encoding:', encoding)
print('Python version:', pythonv)
print('CPU number:', cpu_number)
