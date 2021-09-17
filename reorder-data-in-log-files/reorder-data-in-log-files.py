class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        cnt = 1
        
        for i in logs:
            idx = i.find(' ')
          
            if i[idx + 1].isalpha():
                letter.append([i[:idx + 1],i[idx + 1:]])
            else:
                digit.append(i)
          
        sort_let = (sorted(letter,key=(lambda x : x[0])))     
        print(sort_let)
        sort_let = (sorted(sort_let,key=(lambda x : x[1])))
        print(sort_let)
        
        re = []
        for i in sort_let:
            complet_str = i[0] + i[1]
            re.append(complet_str)
            
        for i in digit:
            re.append(i)
            
        return re