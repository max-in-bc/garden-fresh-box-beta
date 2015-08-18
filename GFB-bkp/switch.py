import os,sys

for i in os.listdir("."):
	if '.mako' in i:
		f = open(i, "r")
		newLines = ''
		for lines in f.readlines():
			if "adminSidebar" in lines:
				print i, lines
				newLines += lines.replace('adminSidebar', 'sidebar')
			else:
				newLines += lines
				
		f.close()
		open(i,"w").close()
		f = open(i,"r+")
		
		
		for lines in newLines:
			f.write(lines)
		
		f.close()