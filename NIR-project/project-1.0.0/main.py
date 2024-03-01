from ctypes import *
from sys import platform
from time import sleep
from sys import platform, exit

# Local modules
from helpers import *
from button_pressed import *
from constants import *
from struct_defs import *

if __name__ == "__main__":
	if platform == "linux":
		bin_lib_path = "./lib/libmetascan-RPI.so"
	elif platform == "win32":
		bin_lib_path = "./lib/libmetascan.dll"
	nir_lib = cdll.LoadLibrary(bin_lib_path)
	
	# Get Library Version
	major = c_uint32()
	minor = c_uint32()
	version = c_uint32()
	get_lib_res = nir_lib._Z17GetLibraryVersionPiS_S_(byref(major), byref(minor), byref(version))
	if (get_lib_res != 0):
		raise Exception("Unable to fetch the library version")
	print(f"LIBRARY VERSION: {major.value}.{minor.value}.{version.value}", )

	# Open Device
	open_res = nir_lib._Z10OpenIscDevv()
	if (open_res != 0):
		raise Exception("Opening NIR Device unsuccessful.")	
	print("Scanner ready. Press button to initiate scan.")

	# Wait for button press to scan
	wait_for_button_press()
	
	# Perform Scan
	print("Scanning...")
	perform_scan_read_res = nir_lib._Z19PerformScanReadDatav()
	if (perform_scan_read_res != 0):
		raise Exception("Scanning unsuccessful")
	print("Scan completed")
	
	print("Getting scan result")
	scan_result = ScanResult()
	get_scan_result_res = nir_lib._Z13GetScanResultP10ScanResult(byref(scan_result))
	if (get_scan_result_res != 0):
		raise Exception("Unable to get scan result.")
	
	print("SCAN RESULT:")
	print(f"\tHeader Version: {scan_result.header_version}")
	print(f"\tScan Name: {decode_bytes_to_str(scan_result.scan_name)}")
	print(f"\tYear: {scan_result.year}")
	print(f"\tMonth: {scan_result.month}")
	print(f"\tDay: {scan_result.day}")
	print(f"\tDay of Week: {scan_result.day_of_week}")
	print(f"\tHour: {scan_result.hour}")
	print(f"\tMinute: {scan_result.minute}")
	print(f"\tSecond: {scan_result.second}")
	print(f"\tWavelength: {scan_result.wavelength}")
	print(f"\tIntensity: {scan_result.intensity}")
	print(f"\tLength: {scan_result.length}")
			
	
	# Using data, use a model to infer if material is authentic or fake.
	
	# Close Device
	close_res = nir_lib._Z11CloseIscDevv()
	if (close_res != 0):
		raise Exception("NIR Device not successfully closed.")
	exit(0)
