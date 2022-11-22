
class Tree():
    def __init__(self,label, children=None) -> None:
        self.label = label
        self.children = children or []
        
    def __repr__(self):
        if self.children:
            return '%s(%s)' % (self.label, ', '.join(map(str, self.children)))
        else:
            return self.label

    def __str__(self):
        return self.__repr__()


class CYK():
    def __init__(self, w, rules):
        self.n = len(w)
        self.w = w
        self.rules = rules
        self.table = [[[] for i in range(self.n)] for j in range(self.n)]


    
    def CreateTable(self):
        
        if len(self.w) == 0 and self.rules["S"].contains(""):
            return True
        
        for i in range(self.n):
            for key, value in self.rules.items():
                for item  in value: 
                    if self.w[i] in item:
                        self.table[i][i].append(key)  
                    
        for l in range(1,self.n):
            for i in range(self.n-l):
                j = i+l

                for k in range(i, j):           
                    for key, value in self.rules.items():
                        for item in value:
                            if len(item) == 2:
                                B = item[0]
                                C = item[1]
                                if B in self.table[i][k] and C in self.table[k+1][j]:
                                    if key not in self.table[i][j]:
                                        self.table[i][j].append(key)
        return self.table
    
    def Accept(self):
        return ("S" in self.table[0][self.n-1])

                                    
    def PrintTable(self):
        print("\t", self.w)
        for i in range(len(self.table)):
            print(self.w[i], "\t", self.table[i])
                    
    def CreateTree(self,i, j, key):
        for rule in self.rules[key]:
            if len(rule) == 1:
                if rule[0] == self.w[i]:
                    return Tree(key, [Tree(rule[0])])
            else:
                B = rule[0]
                C = rule[1]
                for k in range(i, j):

                    if B in self.table[i][k] and C in self.table[k+1][j]:
                        return Tree(key, [self.CreateTree(i, k, B), self.CreateTree(k+1, j, C)])
        return None
    
    def ShowTree(self,i,j,key):
        print(self.CreateTree(i,j,key))
  


rules1 = {
    "S": [["NP", "VP"]],
    "VP": [["VP", "PP"],["V", "NP"],["cooks"], ["drinks"], ["eats"], ["cuts"]],
    "PP": [["P", "NP"]],
    "NP": [["Det", "N"],["he"], ["she"]],
    "V" : [["cooks"], ["drinks"], ["eats"], ["cuts"]],
    "P" : [["in"], ["with"]],
    "N":  [["cat"], ["dog"],["beer"], ["cake"], ["juice"], ["meat"], ["soup"],["fork"], ["knife"], ["spoon"], ["oven"]],
    "Det": [["a"], ["the"]]
	}


rules2 = {"S"  : [["A", "B"], ["B","C"]],
         "A" : [["B","A"], ["a"]],
         "B" : [["C","C"], ["b"]],
         "C" : [["A","B"], ["a"]],
        }  



w =  "she eats a cake with a fork"
w2 = "baaba"
#(NP), (VP, V), (Det), (N), (P), (Det), (N),

w = w.split(" ") 


hola = CYK(w, rules1)
hola2 = CYK(w2, rules2)

h1 = hola.CreateTable()
h2 = hola2.CreateTable()



hola.PrintTable()
hola2.PrintTable()

hola2.ShowTree(0, len(w2)-1, "S")


