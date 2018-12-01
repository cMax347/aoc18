import os
import numpy as np
import hashlib















def md5(fname):
	# generate md5 checksum of file fname
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def write_freq_lst(f_out, freq_lst):
	try:
		os.remove(f_out)
	with open(f_out,'w') as outfile:
		for idx, freq in enumerate(freq_lst):
	    	f_out.write('{:+d}'.format(freq)+'\n')
		f_out.close()
	print('[write_freq_lst]: wrote '+str(idx)+' frequencies to'+f_out)



def check_integrity(f_in, freq_lst):
	integrity 	= 	False
	in_hash		=	md5(f_in)
	#
	f_out		=	'input.out'
	write_freq_lst(f_out, freq_lst)
	out_hash	=	md5(f_out)
	#
	integrity	=	(out_hash == in_hash)
	return integrity





def read_input(fname='input.txt'):
	if os.path.isfile(fname):
		freq_lst 	=	np.genfromtxt(fname,dtype=int, usecols=0)
		print('[read_input]: got '+str(freq_lst.size)+' frequencies from '+fname)
	else:
		print('[read_input]: could not read input! '+fname+' was not found!')
		sys.exit()





def main():
	freq_lst	=	read_input()



main()












