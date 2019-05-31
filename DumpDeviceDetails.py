def HelloWorld():
	print ("Hello World!")

if __name__=="__main__":
    HelloWorld()
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback
from ptp.PtpUsbTransport import PtpUsbTransport
from ptp.PtpSession import PtpSession, PtpException
from ptp import PtpValues

jjw = PtpUsbTransport(PtpUsbTransport.findptps())
ptpTransport = PtpUsbTransport((PtpUsbTransport.findptps())[0])
ptpSession = PtpSession(ptpTransport)

vendorId = PtpValues.Vendors.STANDARD
try:
    ptpSession.OpenSession()
    deviceInfo = ptpSession.GetDeviceInfo()
    vendorId = deviceInfo.VendorExtensionID
    
    print ("----------- DEVICE -----------")
    print ("StandardVersion: %i" % deviceInfo.StandardVersion)
    print ("VendorExtensionID: %i (%s)" % (deviceInfo.VendorExtensionID, PtpValues.VendorNameById(deviceInfo.VendorExtensionID)))
    print ("VendorExtensionVersion: %i" % deviceInfo.VendorExtensionVersion)
    print ("VendorExtensionDesc: %s" % deviceInfo.VendorExtensionDesc)
    print ("FunctionalMode: %i (%s)" % (deviceInfo.FunctionalMode, PtpValues.FunctionalModeNameById(deviceInfo.FunctionalMode)))
    print ("OperationsSupported:\n\t%s" % "\n\t".join([PtpValues.OperationNameById(op, deviceInfo.VendorExtensionID) for op in deviceInfo.OperationsSupported]))
    print ("EventsSupported:\n\t%s" % "\n\t".join([PtpValues.EventNameById(op, deviceInfo.VendorExtensionID) for op in deviceInfo.EventsSupported]))
    print ("CaptureFormats:\n\t%s" % "\n\t".join([PtpValues.ObjectFormatNameById(op, deviceInfo.VendorExtensionID) for op in deviceInfo.CaptureFormats]))
    print ("ImageFormats:\n\t%s" % "\n\t".join([PtpValues.ObjectFormatNameById(op, deviceInfo.VendorExtensionID) for op in deviceInfo.ImageFormats]))
    print ("Manufacturer: %s" % deviceInfo.Manufacturer)
    print ("Model: %s" % deviceInfo.Model)
    print ("DeviceVersion: %s" % deviceInfo.DeviceVersion)
    print ("SerialNumber: %s" % deviceInfo.SerialNumber)

    print (" ")
    print ("----------- PROPERTIES -----------")
    first = True
    for propertyId in deviceInfo.DevicePropertiesSupported:
        propertyInfo = ptpSession.GetDevicePropInfo(propertyId)
        
        if not first:
            print (" ")
        first = False
        print ("PropertyCode: 0x%04x (%s)" % (propertyInfo.PropertyCode, PtpValues.PropertyNameById(propertyInfo.PropertyCode, deviceInfo.VendorExtensionID)))
        print ("DataType: %s" % PtpValues.SimpleTypeDetailsById(propertyInfo.DataType)[0])
        print ("GetSet: %s" % PtpValues.GetSetNameById(propertyInfo.GetSet, deviceInfo.VendorExtensionID))
        print ("FactoryDefaultValue: %s" % propertyInfo.FactoryDefaultValue)
        print ("CurrentValue: %s" % propertyInfo.CurrentValue)
        if propertyInfo.MinimumValue != None:
            print ("MinimumValue: %s" % propertyInfo.MinimumValue) 
        if propertyInfo.MaximumValue != None:
            print ("MaximumValue: %s" % propertyInfo.MaximumValue) 
        if propertyInfo.StepSize != None:
            print ("StepSize: %s" % propertyInfo.StepSize) 
        if propertyInfo.Enumeration != None:
            print ("Enumeration:",)
            print (propertyInfo.Enumeration)

    print (" ")
    print ("----------- STORAGE -----------")
    first = True
    for storageId in ptpSession.GetStorageIDs():
        storageInfo = ptpSession.GetStorageInfo(storageId)
        
        if storageInfo == None:
            continue        
        if not first:
            print (" ")
        first = False
        print ("StorageId: 0x%08x" % storageId)
        print ("StorageType: %s" % PtpValues.StorageTypeNameById(storageInfo.StorageType, deviceInfo.VendorExtensionID))
        print ("FilesystemType: %s" % PtpValues.FilesystemTypeNameById(storageInfo.FilesystemType, deviceInfo.VendorExtensionID))
        print ("AccessCapability: %s" % PtpValues.AccessCapabilityNameById(storageInfo.AccessCapability, deviceInfo.VendorExtensionID))
        print ("MaxCapacity: %i" % storageInfo.MaxCapacity)
        print ("FreeSpaceInBytes: %i" % storageInfo.FreeSpaceInBytes)
        print ("FreeSpaceInImages: %i" % storageInfo.FreeSpaceInImages)
        print ("StorageDescription: %s" % storageInfo.StorageDescription)
        print ("VolumeLabel: %s" % storageInfo.VolumeLabel)
        
    
    print (" ")
    print ("----------- OBJECTS -----------")
    first = True
    for objectHandle in ptpSession.GetObjectHandles():
        objectInfo = ptpSession.GetObjectInfo(objectHandle)
        
        if not first:
            print (" ")
        first = False
        print ("ObjectHandle: 0x%08x" % objectHandle)
        print ("StorageId: 0x%08x" % objectInfo.StorageId)
        print ("ObjectFormat: %s" % PtpValues.ObjectFormatNameById(objectInfo.ObjectFormat, deviceInfo.VendorExtensionID))
        print ("ProtectionStatus: %s" % PtpValues.ProtectionStatusNameById(objectInfo.ProtectionStatus, deviceInfo.VendorExtensionID))
        print ("ObjectCompressedSize: %i" % objectInfo.ObjectCompressedSize)
        print ("ThumbFormat: %s" % PtpValues.ObjectFormatNameById(objectInfo.ThumbFormat, deviceInfo.VendorExtensionID))
        print ("ThumbCompressedSize: %i" % objectInfo.ThumbCompressedSize)
        print ("ThumbPixWidth: %i" % objectInfo.ThumbPixWidth)
        print ("ThumbPixHeight: %i" % objectInfo.ThumbPixHeight)
        print ("ImagePixWidth: %i" % objectInfo.ImagePixWidth)
        print ("ImagePixHeight: %i" % objectInfo.ImagePixHeight)
        print ("ImageBitDepth: %i" % objectInfo.ImageBitDepth)
        print ("ParentObjectHandle: 0x%08x" % objectInfo.ParentObjectHandle)
        print ("AssociationType: %s" % PtpValues.AssociationTypeNameById(objectInfo.AssociationType, deviceInfo.VendorExtensionID))
        print ("AssociationDesc: 0x%08x" % objectInfo.AssociationDesc)
        print ("SequenceNumber: %i" % objectInfo.SequenceNumber)
        print ("Filename: %s" % objectInfo.Filename)
        print ("CaptureDate: %s" % objectInfo.CaptureDate)
        print ("ModificationDate: %s" % objectInfo.ModificationDate)
        print ("Keywords: %s" % objectInfo.Keywords)

#        STANDARD:SEND_OBJECT_INFO
#        STANDARD:SEND_OBJECT



except PtpException as err:
    print ("PTP Exception: %s" % PtpValues.ResponseNameById(err, vendorId))
#except Exception, e:
#
except Exception as err2:
    print ("An exception occurred: %s" % err2)
    traceback.print_exc()

del ptpSession
del ptpTransport