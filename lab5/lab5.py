# Computation of First rules
# 1. If X is a terminal, then FIRST(X) = {X}.
# 2. If X → ε is a production, then add ε to FIRST(X).
# 3. If X is a non-terminal and X → Y1 Y2 ··· Yk is a
#    production, then add FIRST(Y1) to FIRST(X). If Y1
#    derives ε, then add FIRST(Y2) to FIRST(X).

# Computation of Follow rules
# 1. For the FOLLOW(start symbol) place $, where $ is
#    the input end marker.
# 2. If there is a production A → αBβ, then everything
#    in FIRST(β) except ε is in FOLLOW(B).
# 3. If there is a production A → αB, or a production
#    A → αBβ where FIRST(β) contains ε, then
#    everything in FOLLOW(A) is in FOLLOW(B).

def first(string):
    first_ = set()
    if string in non_terminals:
        alternatives = productions_dict[string]
        for alternative in alternatives:
            first_2 = first(alternative)
            first_ = first_ |first_2
    
    # Rule 1
    elif string in terminals:
        first_ = {string}
    
    # Rule 2
    elif string=='' or string=='@':
        first_ = {'@'}

    else:
        first_2 = first(string[0])
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                first_ = first_ | (first_2 - {'@'})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = first(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2

    return  first_

def follow(nT):
    follow_ = set()
    prods = productions_dict.items()
    # Rule 1
    if nT==starting_symbol:
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | follow(nt)
                    else:
                        follow_2 = first(following_str)
                        if '@' in follow_2:
                            follow_ = follow_ | follow_2-{'@'}
                            follow_ = follow_ | follow(nt)
                        else:
                            follow_ = follow_ | follow_2
    return follow_

terminals = []
non_terminals = []
productions = []
productions_dict = {}

# Terminals
n1=int(input("Enter no. of terminals: "))
print("Enter terminals:")
for _ in range(n1):
    terminals.append(input())

# Non Terminals
n2=int(input("Enter no. of non terminals: "))
print("Enter non terminals:")
for _ in range(n2):
    non_terminals.append(input())

# Starting Symbol
starting_symbol = input("Enter starting symbol: ")

# Production
n3 = int(input("Enter no of productions: "))
print("Enter productions (Sample input: A->B|cdE) (Epsilon is @):")
for _ in range(n3):
    productions.append(input())

# Converting Productions to dict
for nT in non_terminals:
    productions_dict[nT] = []
for production in productions:
    # print(production)
    nonterm_to_prod = production.split("->")
    # print(nonterm_to_prod)
    alternatives = nonterm_to_prod[1].split("|")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)
# print(productions_dict)

FIRST = {}
FOLLOW = {}

for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal])))