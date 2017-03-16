#this  structure format, which puts all individuals genotype in one row.
import numpy as np
import glob
import os


files=glob.glob("d9*_sorted.vcf")

for file in files:
	name="ran"+file.split('_sorted.vcf')[0]+'.str'
	tt=open(name,'w')
	b=np.empty((1,72),dtype='S8')
	c=np.empty((1,72),dtype='S8')
	dicgen={'A':'1','C':'2','G':'3','T':'4'}
	popgen={'CN':'1','EM':'2','JF':'3','QC':'3','JY':'4','MS':'5','QL':'6','SF':'7','TL':'8','XY':'9','YC':'10','YJ':11}

	with open(file) as temp:
		for line in temp.readlines():
			if line.startswith(r'#CHROM'):
				id=line.rstrip('\n').split('\t')[9::] 
				for i in xrange(0,72):
					b[0][i]=id[i]
					c[0][i]=popgen[id[i][:2:]]

	ff=np.loadtxt(file,skiprows=10,delimiter='\t',dtype='S')
	np.random.shuffle(ff) 
	
	if ff.shape[0]>=5000:
		a=np.empty((5000,72),dtype='S8')
		n=0
		for row in ff[:5000]:
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
				a[n][i-9]=ss
			n+=1
		for line in np.concatenate((b,c,a)).T:
			for i in line:
				print >>tt,'%3s'%i,
			print >>tt
	else:
		a=np.empty((ff.shape[0],72),dtype='S8')
		n=0
		for row in ff:
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
				a[n][i-9]=ss
			n+=1
		for line in np.concatenate((b,c,a)).T:
			for i in line:
				print >>tt,'%3s'%i,
			print >>tt
		
	print "%s is done"%file
	tt.close()
	temp.close()

