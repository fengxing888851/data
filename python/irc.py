#! /usr/bin/python

import re 
import os
import sys
import glob

p1 = re.compile(r'NAtoms=\s+(\d+)') #match atoms number
p2 = re.compile(r'Maximum\spoints\sper\spath\s+=\s+(\d+)') # match maximun points in '*irc.log'

def atoms(filename):
	''' get atoms number.'''
	file = open(filename)
	filecontent = file.read()
	number = int(p1.search(filecontent).groups(1)[0])
	file.close()
	return number

def inputfilename(filename):
	''' get filename '''
	inputfn = os.path.splitext(filename)[0]
	return inputfn

def ircfilename(filename):
	'''get filename before '-'. '''
	name = filename.split('-')[0]
	return name

def maxpoints(filename):
	''' get irc maxpoints. '''
	file = open(filename)
	filecontent = file.read()
	pointnumber = int(p2.search(filecontent).groups(1)[0])
	file.close()
	return pointnumber


class Coordinate:
	''' get coordinates in log of TS. '''
	def __init__(self, tsfilename):
		self.tsfilename = tsfilename
	def tscoordinate(self):
		'''TS coordinates. 
		get last paragraph ,match coordinate and extract it. 
		'''
		content = ''
		file = open(self.tsfilename)
		filelines = file.readlines()
		record = False
		p = re.compile('Freq\\\\RM062X')	
		for fn in filelines:
			m = p.search(fn)
			if m:
				record = True
			if record:
				content += fn.strip()
		file.close()
		cutoff = content.index('Version')
		coordcontent = content[:cutoff].split('\\')
		coord = ''
		for co in coordcontent:
			p_co = re.compile(r'[A-Z][a-z]?,')
			m_co = p_co.findall(co)
			if m_co:
				coord += co + '\n'
		return coord


class IrcCom:
	'''input file including TS coordinates of last paragraph from '*.log'. '''
	def __init__(self, inputfn, coordinate):
		self.inputfn = inputfn
		self.coordinate = coordinate
	def tsinputfile(self):
		file = open('%s.com' % self.inputfn, 'w')
		file.write('%%chk=%s.chk\n%%nprocshared=8\n%%mem=200Mw\n' %self.inputfn)
		file.write('# m062x/6-31+G(d,p) freq 5D int(ultrafine) irc=(maxpoints=50,calcfc,maxcycle = 200)\n\n')
		file.write('%s m062x/6-31+G(d,p)\n\n' %self.inputfn)
		file.write('0 1\n')
		file.write(self.coordinatei + '\n')
		file.close()


class IrcCoordinate:
	'''get first or last coordinates from '*irc.log'.'''
	def __init__(self, filename, number, pointnumber):
		self.filename = filename
		self.number = number
		self.pointnumber = pointnumber - 1
		self.p = re.compile(r'Point\sNumber:\s+%d\s+Path\sNumber:\s+1' %self.pointnumber)
	def coordinate(self):
		content = ''
		file = open(self.filename)
		fileline  = file.readlines()
		record = False
		for fn in fileline:
			m = self.p.search(fn)
			if m:
				record = True
				count = 0
			if record:
				count = count + 1
				if count >= 14 :
					fnlist = re.split(r'\s+', fn.strip())
#					print fnlist
					fnstr = fnlist[1] + '\t' + fnlist[3]  + '\t' + fnlist[4] + '\t' + fnlist[5] + '\n'
					content += fnstr
				if count >= self.number + 13:
					record = False		
		file.close()
		return content 


class Com:
	'''input file including first or last coordinates from '*irc.log'.'''
	def __init__(self, inputfn, coordinate):
		self.inputfn = inputfn
		self.coordinate = coordinate
	def inputfile(self):
		file = open('%s.com' % self.inputfn, 'w')
		file.write('%%chk=%s.chk\n%%nprocshared=8\n%%mem=200Mw\n' %self.inputfn)
		file.write('# m062x/6-31+G(d,p) freq 5D int(ultrafine) opt(maxcyc=200)\n\n')
		file.write('%s m062x/6-31+G(d,p)\n\n' %self.inputfn)
		file.write('0 1\n')
		file.write(self.coordinate + '\n')
		file.close()


class G09sub:
	'''modify filename ing09sub.'''
	def __init__(self,inputfn):
		self.inputfn = inputfn
	def g09sub(self):
		file = open('g09sub')
		filecontent = file.read()
		filecontent = re.sub(r'#\$\s+-N\s+\w+', '#$ -N %s' %self.inputfn, filecontent)
		filecontent = re.sub(r'JOBNAME=\w+', 'JOBNAME=%s' %self.inputfn, filecontent)
#		print filecontent
		file.close()
		g09subfile = open('g09sub', 'w')
		g09subfile.write(filecontent)
		g09subfile.close()
			
	

if __name__ == "__main__":
	fn = raw_input('Please input filename:')  #filename is name of '*.log' about TS.
	ircname = inputfilename(fn) + 'irc'  #defining irc filename like '*irc.log'
	if glob.glob(r'%s.log' %ircname): 
		'''if having '*irc.log', qsub starting state and final state input file '''
		iname = ircname + '.log'
		number = atoms(iname)
		pointnumber = maxpoints(iname)
		
	# qsub input file about reactants .

		irccoforward = IrcCoordinate(iname,number,pointnumber)
		coordforward = irccoforward.coordinate()
#		print irccoforward.pointnumber
#		print coordforward
		inputfn = ircfilename(fn) + 'R'
		comforward = Com(inputfn,coordforward)
		comforward.inputfile()
		g09subfor = G09sub(inputfn)
		g09subfor.g09sub()
		os.system('qsub g09sub')
		
	# qsub input file about product.

		irccobackward = IrcCoordinate(iname, number, pointnumber)
#		print irccobackward.pointnumber
		irccobackward.p = re.compile(r'Point\sNumber:\s+%d\s+Path\sNumber:\s+2' %irccobackward.pointnumber)
		#print irccobackward.p
		coordbackward = irccobackward.coordinate()
#		print coordbackward
		inputfn = ircfilename(fn) + 'P'
		combackward = Com(inputfn, coordbackward)
		combackward.inputfile()
		g09subback = G09sub(inputfn)
		g09subback.g09sub()
		os.system('qsub g09sub')

	else:
		''' if not, qsub irc input file named '*irc.log'. '''
		tscoordinate = Coordinate(fn)
		tsco = tscoordinate()
		irccom = IrcCom(ircname, tsco)
		irccom.tsinputfile()
		g09subirc = G09sub(ircname)
		g09subirc.g09sub()
		os.system('qsub g09sub')
	


