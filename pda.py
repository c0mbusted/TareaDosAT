
#RSV
def Rsvq6(w,pila,PDA):  
    if (pila==""):
        PDA=False
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:] 
    return (w,pila,PDA)

def Rsvq5(w):
    simbolo = w[0:1]
    w=w[1:]
    return (w)

def Rsvq4(w,pila,PDA):
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:]
    return (w,pila,PDA)

def Rsvq3(w,pila,PDA):
    simbolo = w[0:1]
    w=w[1:]
    pila="&" + pila
    return (w,pila,PDA)
    

def Rsvq2(w,pila,PDA): #estado final 
    if (pila==""):
        PDA=False
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:] 
    return (w,pila,PDA)

def Rsvq1(w,pila,PDA):
    simbolo = w[0:1]
    w=w[1:]
    pila="$" + pila
    return (w,pila,PDA)


# -----------PDA RSV -------------#
def pdaRsv(w, pila, PDA):

    contadorC=0
    contadorG=0
    
    while(w[0:1]=="T"):
        w,pila,PDA=Rsvq1(w,pila,PDA)
        contadorC+=1
    
    while(w[0:1]=="C"):
        if(contadorC==0):
            w,pila,PDA=Rsvq3(w,pila,PDA)
            
            contadorG+=1
            continue
        else:

            w,pila,PDA=Rsvq2(w,pila,PDA)

        contadorC-=1
        
        
    if(pila[0:1]=="$"):
        pila="@" + pila 

    
    while(w[0:1]=="G"):
        if(contadorG==0):
            if(len(w)>=1):
                if(w[0:1]=="G"):
                    pila="@"+pila
                    break

            w,pila,PDA=Rsvq4(w,pila,PDA)
            continue
        else:
            w,pila,PDA=Rsvq4(w,pila,PDA)
            
           
        contadorG-=1     
        
    while (len(w)>=1):
        if (w[0:1] =="A"):
            w=Rsvq5(w)
            
            
        else:
            simbolo=w[0]
            w=w[1:]
            pila="&" + pila
           


    if (not PDA):
        print("pda: No reconocida [Rsv]")
        return False
    else:
        if(len(w)==0 and len(pila)==0):
            print("len: Reconocida [Rsv]")
            return True
        else:
            print("len: NO reconocida [Rsv]")
            return False



########------ COVID --------########

def q4(w,pila,PDA):
    if (pila==""):
        PDA=False
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:] 
    return (w,pila,PDA)

def q3(w,pila,PDA):
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:]
    return (w,pila,PDA)

def q2(w,pila,PDA):
    simbolo = w[0:1]
    w=w[1:]
    pila="$" + pila
    return (w,pila,PDA)

def q1(w,pila):
    simbolo=w[0:1] 
    w=w[1:] 
    pila="$" + pila
    return(w,pila)

############ PDA (1): COVID ##########
def pdaCovid(w, pila, PDA):
    while(w[0:1]=="A"):
        w,pila=q1(w,pila)

    while(w[0:1]=="C"):
        w,pila,PDA=q2(w,pila,PDA)

    while(w[0:1]=="T"):
        w,pila,PDA=q3(w,pila,PDA)

    while(w[0:1]=="G"):
        w,pila,PDA=q4(w,pila,PDA)

    if (not PDA):
        print("pda: No reconocida [COVID-19]", end=" ")
        return False
    else:
        if(len(w)==0 and len(pila)==0):
            print("len: Reconocida [COVID-19]", end=" ")
            return True
        else:
            print("len: NO reconocida [COVID-19]", end=" ")
            return False

# -------------Neumonia-------------#
def Neuq7(w,pila,PDA):  
    if (pila==""):
        PDA=False
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:] 
    return (w,pila,PDA)

def Neuq6(w,pila,PDA): 
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:]
    return (w,pila,PDA)

def Neuq5(w,pila,PDA):
    simbolo = w[0:1]
    w=w[1:]
    pila="$$" + pila
    return (w,pila,PDA)

def Neuq4(w,pila,PDA):  
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[2:]
    return (w,pila,PDA)

def Neuq3(w,pila,PDA):  
    if (pila==""):
        PDA=False
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:] 
    return (w,pila,PDA)


def Neuq2(w,pila,PDA):
    simbolo = w[0:1]
    w=w[1:]
    pila=pila[1:]
    return (w,pila,PDA)

def Neuq1(w,pila,PDA):
    simbolo = w[0:1]
    w=w[1:]
    pila="$$" + pila
    return (w,pila,PDA)

def Neuq0(w,pila):
    simbolo=w[0:1] 
    w=w[1:]
    pila="$" + pila
    return(w,pila)

################ PDA (2): NEUMONIA ##################
def pdaNeumonia(w, pila, PDA):
    while(w[0:1]=="T"):
        w,pila=Neuq0(w,pila)
    
    while(w[0:1]=="A"):
        w,pila,PDA=Neuq1(w,pila,PDA)

    while(w[0:1]=="G"):
        w,pila,PDA=Neuq2(w,pila,PDA)

    while(w[0:1]=="T"):
        w,pila,PDA=Neuq3(w,pila,PDA)

    while(w[0:1]=="C"):
        w,pila,PDA=Neuq4(w,pila,PDA)
    
    while(w[0:1]=="A"):
        w,pila,PDA=Neuq5(w,pila,PDA)
    
    while(w[0:1]=="G"):
        w,pila,PDA=Neuq6(w,pila,PDA)
    
    while(w[0:1]=="G"):
        w,pila,PDA=Neuq7(w,pila,PDA) 

    if (not PDA):
        print("pda: No reconocida [Neumonia]", end=" ")
        return False
    else:
        if(len(w)==0 and len(pila)==0):
            print("len: Reconocida [Neumonia]", end=" ")
            return True
        else:
            print("len: NO reconocida [Neumonia]", end=" ")
            return False


def porcentaje(total,x,y,z):

    print("\n--> Porcentajes: ", end=" ")
    print("COVID: " + '{percent:.1%}'.format(percent=x/total), end=" ")
    print("Neumonía: " + '{percent:.1%}'.format(percent=y/total), end=" ")
    print("RSV: "+ '{percent:.1%}'.format(percent=z/total), end=" ")

#lectura archivo

with open("input.txt",'r') as f: 
    c, n, r = 0, 0, 0
    lineas = f.readlines()  

    for line in lineas: 
        pila=""
        w=line.split("\n")[0] 
        print(w)
        PDA=True


        # Comprobamos cadena en los 3 PDA
        if pdaCovid(w, pila, PDA):
            c += 1

        if pdaNeumonia(w, pila, PDA):
            n += 1

        if pdaRsv(w, pila, PDA):
            r += 1

    print("\n--> Resultados finales: ", end=" ")
    print("C:", c, end=" ")
    print("N:", n, end=" ")
    print("RSV:", r , end=" ")
    print("Ninguno: ", len(lineas) - (c + n + r))
    tot = len(lineas)
    porcentaje(tot, c, n, r)
    

