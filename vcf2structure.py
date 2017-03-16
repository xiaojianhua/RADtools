#this  structure format, which puts all individuals genotype in one row.
import numpy as np
import glob
import os
import argparse
from collections import defaultdict


parser = argparse.ArgumentParser(description="Converter of VCF into structure format")
parser.add_argument("-vcf", dest="vcf_file", help="VCF file")
parser.add_argument("-popfile",dest="pop_file", help="population sample file"
parser.add_argument("-o", dest="output_file", help="Name of output file")
arg = parser.parse_args()

files=glob.glob("d9*_sorted.vcf")
dicgen={'A':'1','C':'2','G':'3','T':'4'}
		 popgen={'CN':'1','EM':'2','JF':'3','QC':'3','JY':'4','MS':'5','QL':'6','SF':'7','TL':'8','XY':'9','YC':'10','YJ':11}

def parse_popmap(popfile):
	"""
	popfile was simliart with STACKS file, there are third columns.
	the first column is taxa, the second column is pop, the third column is the code for pop.
	such as  A  POP1  1
		 B  POP1  1
		 C  POP2  2
	"""
	pop_handle=open(pop_file)
	pop=defaultdict()
	for line in pop_handle.readlines()
		    taxa=line.strip().split(' ')
		    pop[taxa[0]]=(taxa[1],taxa[2])
	pop_handle.close()
	return pop
		    
def parse_vcf(vcf_file):
	"""
	Parses the VCF file and returns a dictionary with the loci (chromossomes)
	as keys and a list of positions as values.
	"""
	vcf_handle = open(pop,vcf_file)
	for line in vcf_handle:
		if line.startswith("##"):
			pass
		elif line.startswith("#CHROM"):
			taxa_list = line.strip().split()[9:]
		    	b=np.empty((1,len(taxa_list)),dtype='S8')
			c=np.empty((1,len(taxa_list)),dtype='S8')
			for i in xrange(0,len(taxa_list)):
					b[0][i]=taxa_list[i]
					c[0][i]=pop[taxa_list[i]][1]
	ff=np.loadtxt(vcf_file,skiprows=10,delimiter='\t',dtype='S')
	vcf_handle.close()
	return ff, b,c,taxa_list


def vcf2str(ff,taxa_list)
	ar=np.empty((ff.shape[1],len(taxa_list))
	for row in ff:
		n=0
		for i in xrange(9,len(row)):
			seq=row[i][:3].split('/')
			if seq[0]=='0' and seq[1]=='0':
				seq=[dicgen[row[3]],dicgen[row[3]]]
			elif seq[0]=='1' and seq[1]=='1':
				seq=[dicgen[row[4]],dicgen[row[4]]]
			elif  seq[0]=='0' and seq[1]=='1':
				seq=[dicgen[row[3]],dicgen[row[4]]]
			elif  seq[0]=='1' and seq[1]=='0':
				seq=[dicgen[row[4]],dicgen[row[4]]]
			else:
				seq=['-9','-9']	
			ss='%3s'%(' ').join(seq)
			ar[n][i-9]=ss
		n+=1
	return ar
def write_tostructure(b,c,ar,output_file)
	temp=open(output_file+'.str','w')  
	for line in np.concatenate((b,c,ar)).T:
		for i in line:
			print >>tt,'%3s'%i,
		print >>tt	
	print "%s is done"%vcf_file
	temp.close()

def main():
	# Arguments
	vcf_file = arg.vcf_file
	pop_file = arg.pop_file
	output_file = arg.output_file
	
	# Parse popfile
	pop = parse_popmap(popfile)
	# Parse VCF
	ff,b,c,taxa_list= parse_vcf(pop,vcf_file)
	#vcf to structure
	ar=vcf2str(ff,taxa_list)
	# Write phylip file
	write_to_phy(b,c,ar,output_file)

if __name__ == "__main__":
	main()

