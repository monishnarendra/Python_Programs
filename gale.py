def input_men_or_women(n,z):
    g={}
    for i in range(n):
        print("enter the prefernce of ",z," for",i+1,end=":")
        g[i+1]=list(map(int,input().split()))
    return g

def priority(men1,women1,men2,women):
    if(women[women1].index(men1)<women[women1].index(men2)):
        return True
    else:
        return False

def gale_shapey(men,women,n):
    paired_men={}
    paired_women={}
    while(len(paired_men)!=n):
        for i in men:
            if i not in paired_men:
                for j in men[i]:
                    if j not in paired_women:
                        paired_men[i]=j
                        paired_women[j]=i
                        break
                    else:
                        if(priority(i,j,paired_women[j],women)):
                            del paired_men[paired_women[j]]
                            paired_men[i] = j
                            paired_women[j]=i
                            break
    return paired_men,paired_women
n=int(input("number of men"))
men1=input_men_or_women(n,"men")
women1=input_men_or_women(n,"women")
dict1={1:'A',2:'B',3:'C'}
dict2={1:'V',2:'W',3:'X'}
a,b=gale_shapey(men1,women1,n)
for i,j in a.items():
    print(dict1[i],':married:',dict2[j])