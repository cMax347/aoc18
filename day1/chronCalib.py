import os
import sys
import numpy as np
import hashlib
import uuid
#
#
#
#----------------------------------------------------------------------------------
#		HELPERS
#----------------------------------------------------------------------------------
def get_sys_args():
	# exit if no file name is provided
	if len(sys.argv)>1:
				f_in	=	sys.argv[1]
	else:
		print('please provide a input file')
		sys.exit()
	return f_in
#----
#
#
def md5(fname):
	# generate md5 checksum of file fname, from:
	#	https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-fileß
    #
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
#----
#
#
#
#----------------------------------------------------------------------------------
#		FILE I/O
#----------------------------------------------------------------------------------
def read_input(f_in):
	#	read the input file 
	# 	expects one value per line
	if os.path.isfile(f_in):
		freq_lst 	=	np.genfromtxt(f_in,dtype=int, usecols=0)
	else:
		print('[read_input]: file '+f_in+' does not exist ')
		sys.exit()
	return freq_lst
#----
#
#
def write_freq_lst(f_out, freq_lst):
	#	write frequency list freq_lst to file f_out
	if os.path.isfile(f_out):
		os.remove(f_out)
	with open(f_out,'w') as outfile:
		for idx, freq in enumerate(freq_lst):
			outfile.write('{:+d}'.format(freq)+'\n')
		outfile.close()
#----
#
#
def check_integrity(f_in, freq_lst):
	#	compares checksum of input file and output file
	integrity 	= 	False
	in_hash		=	md5(f_in)
	#
	#	write to unique file 
	f_out		=	str(uuid.uuid4())
	write_freq_lst(f_out, freq_lst)
	#
	out_hash	=	md5(f_out)
	integrity	=	(out_hash == in_hash) and (freq_lst.size > 0)
	#
	if integrity:
		os.remove(f_out)
	return integrity
#----
#
#
#----------------------------------------------------------------------------------
#		MAIN
#----------------------------------------------------------------------------------
def main():
	#
	#	get filename from sysargs
	f_in		=	get_sys_args()	
	#
	#	read input file
	freq_lst	=	read_input(f_in)
	#
	#	if data valid SUM
	if check_integrity(f_in, freq_lst):
		freq_sum	=	np.sum(freq_lst)
		print(freq_sum)
	else:
		print("[main]: data integrity not given, abort!")
		sys.exit()
#----
#
#
main()












