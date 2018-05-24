import csv


with open ('out.csv', 'r', newline='', encoding='utf-8') as ifp:
	
	ir = csv.reader(ifp)
	for	s, p, o in ir:   
		s='_:'+s
		p='<'+p+'>'
		if p=="<http://dilab77.ionio.gr/sw/p14pagk/myvocab#ΗΜΕΡΑ>":
			o='"'+o+'"'
		elif p=='<http://dilab77.ionio.gr/sw/p14pagk/myvocab#ΕΝΑΡΞΗ>' or p=="<http://dilab77.ionio.gr/sw/p14pagk/myvocab#ΛΗΞΗ>":
			
			o='"'+o+':00"^^<http://www.w3.org/2001/XMLSchema#time>'
		else:
			o='<'+o+'>'
		print('{} {} {} .'.format(s,p,o))
			
