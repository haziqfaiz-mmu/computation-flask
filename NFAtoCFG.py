#convert NFA into regular grammar, return string
def NFAtoCFG(Q,sigma,delta):

    cfg = []
    sigma = list(sigma)
    sigma.append("")
    #create empty array
    i=0
    for x in Q:
        cfg.append("")
        i=i+1
    #fill in LHS of cfg
    i=0
    for state in delta:
        cfg[i]+=(state +" ->")
        i=i+1
    
    #use transition function to fill inn the rest
    i=0
    for state in delta:
        for letter in sigma:
            deltastring = (delta[state][letter])
            if(delta[state][letter]):
                #print(f"{letter} : {deltastring}")
                #print(f"'{letter}' {deltastring}")
                j=0
                while(j<len(deltastring)):
                   
                    block=(f" '{letter}' {deltastring[j]}")
                    block2 = f" {deltastring[j]}"
                    if(letter!=""):
                        cfg[i]+=block
                        
                    else:
                        cfg[i]+=block2
                    
                    cfg[i]+=" |"

                    
                    
                    j=j+1

        if(cfg[i][-1]=="|"):
            cfg[i] = cfg[i][:-1]
        i=i+1 

    #combine string
    cfgstring=""
    i=0
    for x in cfg:
        cfgstring+=cfg[i]+"\n"
        i=i+1

    return cfgstring  
