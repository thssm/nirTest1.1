import ctypes
from constants import *

class CONFIG_HEAD(ctypes.Structure):
	_fields_ = [
		("scan_type", ctypes.c_uint8),
		("scanConfigIndex", ctypes.c_uint16),
		("ScanConfig_serial_number", ctypes.c_char * SER_NUM_LEN),
		("config_name", ctypes.c_char * SCAN_CFG_FILENAME_LEN),
		("num_repeats", ctypes.c_uint16),
		("num_sections", ctypes.c_uint8),
	]

class ScanSection(ctypes.Structure):
	_fields = [
		("section_scan_type", ctypes.c_uint8),
		("width_px", ctypes.c_uint8),
		("wavelength_start_nm", ctypes.c_uint16),
		("wavelength_end_nm", ctypes.c_uint16),
		("num_patterns", ctypes.c_uint16),
		("exposure_time", ctypes.c_uint16),
	]

class calibCoeffs(ctypes.Structure):
	_fields_ = [
		("ShiftVectorCoeffs", ctypes.c_double * 3),
		("PixelToWavelengthCoeffs", ctypes.c_double * 3),
	]

class ScanConfig(ctypes.Structure):
	_fields_ = [
		("head", CONFIG_HEAD),
		("section", ScanSection * SCAN_MAX_SECTIONS)
	]

class ScanResult(ctypes.Structure):
	_fields_ = [
		# SCAN_DATA_VERSION
		("header_version", ctypes.c_uint32),

		# SCAN_DATA_HEAD_NAME
		("scan_name", ctypes.c_char * 20),
		
		# DATE_TIME_STRUCT 
		("year", ctypes.c_uint8),
		("month", ctypes.c_uint8),
		("day", ctypes.c_uint8),
		("day_of_week", ctypes.c_uint8),
		("hour", ctypes.c_uint8),
		("minute", ctypes.c_uint8),
		("second", ctypes.c_uint8),
		
		# SCAN_DATA_HEAD_BODY
		# ("system_temp_hundredths", ctypes.c_int16),
		# ("detector_temp_hundredths", ctypes.c_int16),
		# ("humidity_hundredths", ctypes.c_uint16),
		# ("lamp_pd", ctypes.c_uint16),
		# ("scanDataIndex", ctypes.c_uint32),
		# ("calibration_coeffs", calibCoeffs),
		# ("serial_number", ctypes.c_char * SER_NUM_LEN),
		# ("adc_data_length", ctypes.c_uint16),
		# ("black_pattern_first", ctypes.c_uint8),
		# ("black_pattern_period", ctypes.c_uint8),
		# ("pga", ctypes.c_uint8),

		# ("cfg", ScanConfig),
		("wavelength", ctypes.c_double * ADC_DATA_LEN),
		("intensity", ctypes.c_int * ADC_DATA_LEN),
		("length", ctypes.c_int),
	]