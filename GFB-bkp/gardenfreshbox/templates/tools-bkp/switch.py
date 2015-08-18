import os,sys

for i in os.listdir("/home/edgard/homework/CIS4910/gardenFB/gardenfreshbox/templates/tools"):
	if '.mako' in i:
		f = open(i, "r")
		newLines = ''
		for lines in f.readlines():
			if "adminSidebar" in lines:
				newLines += lines.replace('adminSidebar', 'sidebar')
			else:
				newLines += lines
				
		f.close()
		open(i,"w").close()
		f = open(i,"r+")
		
		
		for lines in newLines:
			f.write(lines)
		
		f.close()