The aim of the project is to experimentally show that the sharp peak in the WALSAT algorithm occurs around a value of 4.3.

The code contains the following files:
- **rnd_cnf_gen.py** - This code generates a 3 SAT expression in the DIMACS format and writes them to the input directory.
- **otk_sat.py** - This code contains the WALKSAT algorithm and returns a assignment for the expression for which it is satisfiable. The script will not finish if the formula of the graph generated is unsatisfiable if you use a local search solver. If the expression is not satifiable, then the algorithm runs in an infinite loop. However, we restrict this loop by keeping a threshold of 50000 microseconds.
- **run.py** - This file loops for 3 to 70 variables(say n) and 3*n to 5*n(say m) clauses for each n and creates a corresponding random 3SAT expression by using the rnd_gen_py file. It then calls the otk_sat module which returns a 2-tuple (solution, time) for every expression. The time is in microseconds. If the expression is not satisfiable(we break the loop at a suitable threshold), the return value is (None,threshold)   The code then logs these values in a file results.txt that contains the following format - (clause/variable (m/n), time (in microseconds), 0/1 (0 if satifiable and 1 if not satisfiable) ).
- **plot.py** - generates a plot with time(microseconds) on the Y-AXIS and m/n ratio on the X-AXIS.

**ANALYSIS**

The time is maximum around a value of 4.3 in the graph (final.png) which is close to the theoretically proven value of 4.3.(n = 3 to 70)
I have also plotted values for n = 3 to 40(fig1.png) and n = 3 to 50(fig2.png). The peak in those graphs is also close to the theoretical value of 4.3.



