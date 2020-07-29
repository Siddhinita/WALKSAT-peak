from rnd_cnf_gen import CNF
from otk_sat import run_sat, parse

for i in range(3,90):
	for j in range(3*i,5*i):
		cnf_formula = CNF(i,j,3)
		
		# Show formula
		cnf_formula.show()
		clauses, n_vars, lit_clause = parse('./inputs/' + str(i)+'_'+str(j)+'.txt')
		solution, time = run_sat(clauses, n_vars, lit_clause)
		print(time)
		f = open('results.txt','a+')
		print((j*1.0)/i)
		if solution is None:
			f.write(str((j*1.0)/i)+','+str(time)+','+'0')
		else:        	
			f.write(str((j*1.0)/i)+','+str(time)+','+'1')
			print('v ' + ' '.join(map(str, solution[1:])) + ' 0')
		f.write("\n")
		f.close()

	
		
