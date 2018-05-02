from collections import defaultdict

# routing: la tabella di routing (locale)
# r_from: il router da cui ricevo l'advertisement
# advertisement: l'advertisement
def merge(routing,r_from,advertisement):
	# Ricopio la tabella locale nell'output
	t_out=defaultdict(list)
	for dest in advertisement.keys(): 
		advertisement[dest]=advertisement[dest]+1
	for dest in routing.keys(): 
		t_out[dest]=routing[dest]
	# Scansione della tabella in input
	for dest in advertisement.keys():
		# Se la destinazione e' nota
		if dest in t_out.keys():
			# e il prossimo router e' quello da cui ricevo la tabella, 
			# aggiorno il costo
			if t_out[dest][0] == r_from: t_out[dest]=[r_from,advertisement[dest]]
            # altrimenti, se il costo e' inferiore aggiorno il costo e il router
			elif t_out[dest][1] > advertisement[dest]: 
				t_out[dest]=[r_from,advertisement[dest]]
        # se invece la destinazione non e' nota aggiungo una nuova riga
		else: t_out[dest]=[r_from,advertisement[dest]]
	return t_out

# Esempio sugli appunti
tabella_routing={
 'n1':['A',1],
 'n2':['C',1],
 'n3':['A',3],
 'n4':['B',1],
 'n5':['B',2]}

out = merge(tabella_routing,'C',{'n2':1,'n3':0,'n6':4})
 
print(out)
