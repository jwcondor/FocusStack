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
    
    id = 0
    while True:
        ptpSession.InitiateCapture(objectFormatId=PtpValues.StandardObjectFormats.EXIF_JPEG)

        objectid = None
        while True:
            evt = ptpSession.CheckForEvent(None)
            if evt == None:
                raise Exception("Capture did not complete")
            if evt.eventcode == PtpValues.StandardEvents.OBJECT_ADDED:
                objectid = evt.params[0]
                break

        if objectid != None:
            file = open("capture_%i.jpg" % id, "w")
            ptpSession.GetObject(objectid, file)
            file.close()
            id+=1
            ptpSession.DeleteObject(objectid)

except PtpException, e:
    print "PTP Exception: %s" % PtpValues.ResponseNameById(e.responsecode, vendorId)
except Exception, e:
    print "An exception occurred: %s" % e
    traceback.print_exc()

del ptpSession
del ptpTransport

