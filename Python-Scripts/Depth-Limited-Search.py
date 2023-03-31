Dict= {
    "a" : ['b','c'],
    'b' : ['d','e'], 'c' : ['f','g'],
    'd' : ['h','i'], 'e' : ['j','k'], 'f' : ['l','m'], 'g' : ['n','o'],
    'h' : [], 'i' : [], 'j' : [], 'k' : [], 'l' : [], 'm' : [], 'n' : [], 'o' : []
    }
visited = set()

def DLS(visited,Dict,Node,Target,Limit):
    if Node not in visited:
        print(Node,end=" ")
        if Node == Target:
            return True
        visited.add(Node)
        while Limit > 1 :
            Limit -=1
            for i in Dict[Node]:
                if DLS(visited,Dict,i,Target,Limit):
                    return True
        return False
                
found = DLS(visited,Dict,"a","g",3)
print("Target Found" if found else "Target not Found")