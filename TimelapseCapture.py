def HelloWorld():
	print "Hello World!"

if __name__=="__main__":
    HelloWorld()
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback
import time
from ptp.PtpUsbTransport import PtpUsbTransport
from ptp.PtpSession import PtpSession, PtpException
from ptp import PtpValues

if len(sys.argv) != 2:
    print >>sys.stderr, "Syntax: TimelapseCapture <interval in seconds>"
    sys.exit(1)
delay = int(sys.argv[1])

while True:
    # Setup connection to camera
    ptpTransport = PtpUsbTransport(PtpUsbTransport.findptps()[0])
    ptpSession = PtpSession(ptpTransport)
    vendorId = PtpValues.Vendors.STANDARD

    ptpSession.OpenSession()
    deviceInfo = ptpSession.GetDeviceInfo()
    vendorId = deviceInfo.VendorExtensionID

    ptpSession.InitiateCapture(objectFormatId=PtpValues.StandardObjectFormats.EXIF_JPEG)
    while True:
        evt = ptpSession.CheckForEvent(None)
        if evt.eventcode == PtpValues.StandardEvents.OBJECT_ADDED:
            break

    del ptpSession
    del ptpTransport

    time.sleep(delay)
