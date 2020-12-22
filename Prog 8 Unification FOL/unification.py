def Unify():
    LHSarguments = []
    RHSarguments = []
    print("Enter the LHS predicate")
    predicateLHS = input()
    
    print("How many arguments for the LHS?")
    n = int(input())
    print("Enter the arguments")
    for i in range(n):
        LHSarguments.append(input())

    print("Enter the RHS predicate/function")
    predicateRHS = input()

    

    print("How many arguments on the RHS?")
    m = int(input())
    print("Enter the arguments")
    for i in range(m):
        RHSarguments.append(input())
    
    print("We need to unify")
   
    print(predicateLHS,LHSarguments , " and  ", end = "")
    print(predicateRHS,RHSarguments)

    if(predicateLHS != predicateRHS):
        print("Cannot unify two different predicates or functions", predicateLHS, "and ", predicateRHS)
        return
    
    if(n != m):
        print("Cannot unify LHS and RHS as the number of arguments are different on both sides")
        return

    substitutions = {}
    

    for i in range(n):
        if(len(LHSarguments[i]) == 1 and len(RHSarguments[i]) > 1):
            substitutions[LHSarguments[i]] = RHSarguments[i]
        elif(len(LHSarguments[i]) > 1 and len(RHSarguments[i]) == 1):
            substitutions[RHSarguments[i]] = LHSarguments[i]
        elif(len(LHSarguments[i]) > 1 and len(RHSarguments[i]) > 1 and LHSarguments[i]!=RHSarguments[i] ):
            print("Cannot unify, two corresponding constants ",LHSarguments[i]," and", RHSarguments[i], "are different")
            return
    print("Unification is possible, following is the substitution set")
    print(substitutions)

Unify()



            
    

