def HelloWorld():
	print "Hello World!"

if __name__=="__main__":
    HelloWorld()
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback
from ptp.PtpUsbTransport import PtpUsbTransport
from ptp.PtpSession import PtpSession, PtpException
from ptp import PtpValues

ptpTransport = PtpUsbTransport(PtpUsbTransport.findptps()[0])
ptpSession = PtpSession(ptpTransport)

vendorId = PtpValues.Vendors.STANDARD
try:
    ptpSession.OpenSession()
    deviceInfo = ptpSession.GetDeviceInfo()
    vendorId = deviceInfo.VendorExtensionID

    # Read all the possible fstops
    fstops = ptpSession.GetDevicePropInfo(PtpValues.StandardProperties.F_NUMBER).Enumeration
    for fstop in fstops:
        ptpSession.SetFNumber(fstop)
        print "Capturing %i" % fstop

        ptpSession.InitiateCapture(objectFormatId=PtpValues.StandardObjectFormats.EXIF_JPEG)
        while True:
            evt = ptpSession.CheckForEvent(None)
            if evt.eventcode == PtpValues.StandardEvents.OBJECT_ADDED:
                break

except PtpException, e:
    print "PTP Exception: %s" % PtpValues.ResponseNameById(e.responsecode, vendorId)
except Exception, e:
    print "An exception occurred: %s" % e
    traceback.print_exc()

del ptpSession
del ptpTransport