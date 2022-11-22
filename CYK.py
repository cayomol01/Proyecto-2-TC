

class CYK():
    def __init__(self, w, rules):
        self.n = len(w)
        self.w = w
        self.rules = rules
        self.table = [[[] for i in range(self.n)] for j in range(self.n)]

    non_terminals = ["S","VP", "PP", "NP", "V","P", "N", "Det"]

    
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
                    
            


rules1 = {
    "S": [["NP", "VP"]],
    "VP": [["VP", "PP"],["V", "NP"],["cooks"], ["drinks"], ["eats"], ["cuts"]],
    "PP": [["P", "NP"]],
    "NP": [["Det", "N"],["he"], ["she"]],
    "V" : [["cooks"], ["drinks"], ["eats"], ["cuts"]],
    "P" : [["in"], ["with"]],
    "N": [["cat"], ["dog"],["beer"], ["cake"], ["juice"], ["meat"], ["soup"],["fork"], ["knife"], ["spoon"], ["oven"]],
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

hola.CreateTable()
hola2.CreateTable()

hola.PrintTable()
hola2.PrintTable()



