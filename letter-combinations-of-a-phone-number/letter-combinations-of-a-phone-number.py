class Solution:
    from itertools import product
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        Can = []
        
        for i in digits:
            if i == '2':
                Can.append(['a','b','c'])
            elif i == '3':
                Can.append(['d','e','f'])
            elif i == '4':
                Can.append(['g','h','i'])
            elif i == '5':
                Can.append(['j','k','l'])
            elif i == '6':
                Can.append(['m','n','o'])
            elif i == '7':
                Can.append(['p','q','r','s'])
            elif i == '8':
                Can.append(['t','u','v'])
            elif i == '9':
                Can.append(['w','x','y','z'])
                
        answer = []
        a = list(product(*Can))
        print(a)
        for i in a:
            answer.append(''.join(i))
        return answer
        