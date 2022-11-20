

class CYK():
    def __init__(self, w, rules):
        self.w = w
        self.rules = rules
        self.table = [[[] for i in range(len(w))] for i in range(len(w))]
    
    def Accept(self):
        val = list(self.rules.values())
        keys = list(self.rules.keys())
        n = len(self.w)
        
        if len(self.w) == 0 and self.rules["s"].contains(""):
            return True
        
        for i in range(n):
            add = []
            for key, value in self.rules.items():
                if self.w[i] in value:
                    self.table[i][i].append(key)
                    
                    
        for l in range(1,n+1):
            for i in range(n-l+1):
                j = i+l-1

                for k in range(i, j):
                    for key, value in self.rules.items():
                        for item in value:
                            if len(item) == 2:
                                if item[0] in self.table[i][k] and item[1] in self.table[k+1][j]:
                                    if key not in self.table[i][j]:
                                        self.table[i][j].append(key)
        if "S" in self.table[0][n-1]:
            return True
        return False
                                    
    def printing(self):
        for i in self.table:
            print(i)
                    
            
rules = {"S": ["AB"],
         "A": ["CD", "CF"],
         "B": ["c", "EB"],
         "C": ["a"],
         "D": ["b"],
         "E": ["c"],
         "F": ["AD"]
        }        
hola = CYK("aaabbbcc", rules)
print(hola.Accept())


hola.printing()