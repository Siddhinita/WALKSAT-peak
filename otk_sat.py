import random
import sys
import time
threshold = 50000

def parse(filename):
    clauses = []
    count = 0
    for line in open(filename):

        if line[0] == 'c':
            continue
        if line[0] == 'p':
            n_vars = int(line.split()[2])
            lit_clause = [[] for _ in xrange(n_vars * 2 + 1)]
            continue

        clause = []
        for literal in line[:-2].split():
            literal = int(literal)
            clause.append(literal)
            lit_clause[literal].append(count)
        clauses.append(clause)
        count += 1
    return clauses, n_vars, lit_clause


def get_random_interpretation(n_vars):
    return [i if random.random() < 0.5 else -i for i in xrange(n_vars + 1)]


def get_true_sat_lit(clauses, interpretation):
    true_sat_lit = [0 for _ in clauses]
    for index, clause in enumerate(clauses):
        for lit in clause:
            if interpretation[abs(lit)] == lit:
                true_sat_lit[index] += 1
    return true_sat_lit


def update_tsl(literal_to_flip, true_sat_lit, lit_clause):
    for clause_index in lit_clause[literal_to_flip]:
        true_sat_lit[clause_index] += 1
    for clause_index in lit_clause[-literal_to_flip]:
        true_sat_lit[clause_index] -= 1


def compute_broken(clause, true_sat_lit, lit_clause, omega=0.4):
    break_min = sys.maxint
    best_literals = []
    for literal in clause:

        break_score = 0

        for clause_index in lit_clause[-literal]:
            if true_sat_lit[clause_index] == 1:
                break_score += 1

        if break_score < break_min:
            break_min = break_score
            best_literals = [literal]
        elif break_score == break_min:
            best_literals.append(literal)

    if break_min != 0 and random.random() < omega:
        best_literals = clause

    return random.choice(best_literals)


def run_sat(clauses, n_vars, lit_clause, max_flips_proportion=4):
    start = time. time()
    max_flips = n_vars * max_flips_proportion
    while 1:
        interpretation = get_random_interpretation(n_vars)
        true_sat_lit = get_true_sat_lit(clauses, interpretation)
        for _ in xrange(max_flips):

            unsatisfied_clauses_index = [index for index, true_lit in enumerate(true_sat_lit) if
                                         not true_lit]
            end = int((time.time() - start)*1000000) 
            if not unsatisfied_clauses_index:
                return interpretation, end

            #print(end)   
            if end > threshold:
                return None,int(end) 
            clause_index = random.choice(unsatisfied_clauses_index)
            unsatisfied_clause = clauses[clause_index]

            lit_to_flip = compute_broken(unsatisfied_clause, true_sat_lit, lit_clause)

            update_tsl(lit_to_flip, true_sat_lit, lit_clause)

            interpretation[abs(lit_to_flip)] *= -1


def main():

    clauses, n_vars, lit_clause = parse(sys.argv[1])

    solution = run_sat(clauses, n_vars, lit_clause)

    print ('s SATISFIABLE')
    print ('v ' + ' '.join(map(str, solution[1:])) + ' 0')


#if __name__ == '__main__':
#    main()
