import usb.core
import usb.util
import struct
import sys
import traceback



def findptps(cls):
    ptps = ()
    print("Into Findpts")
    for bus in usb.busses():
        print("Findpts bus loop")
        for device in bus.devices:
            if (device.configurations[0].interfaces[0][0].interfaceClass != PtpUsbTransport.USB_CLASS_PTP):
                continue
            if (device.deviceClass == usb.CLASS_HUB):
                continue
            ptps += (device,)

    return ptps

def jjwfindptps(cls):
    ptps = ()
    print("Into Findpts")

    for bus in usb.busses():
        print("Findpts bus loop")
    dev = usb.core.find(find_all=True)
    print ("after find")
    for d in dev:
        print ('into loop')
        print (usb.util.get_string(d, 128, d.iManufacturer))
        print (usb.util.get_string(d, 128, d.iProduct))
        print(d.idProduct, d.idVendor)
    return ptps



def HelloWorld():
	print ("Hello World!")

if __name__=="__main__":
    HelloWorld()

try:
    jjwfindptps(0)

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise