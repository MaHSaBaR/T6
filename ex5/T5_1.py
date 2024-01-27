import re


class oct:
    def __init__(self,DNA):
        self.dna = DNA

    
    def oct_revised_dna(self):
        
        dna = str(self.dna)

        for i in range(len(dna)):
            if dna[i] == 'x':
                dna += str(i)
                break

        for i in range(len(dna)-2):
            if dna[i] == dna[i+1] == dna[i+2]:
                dna = dna.replace(dna[i]+dna[i+1]+dna[i+2],'(0_0)')

        return dna
                    


class crab:
    def __init__(self,DNA):
        self.dna = DNA

    def crab_revised_dna(self):
        dna = str(self.dna)
        
        dna += dna[:10]
        dna = dna.replace('tt','o')

        return dna



class Bob(crab):
    

    def merge(self,left,right):
        merged = []
        right_index = 0
        left_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index +=1
            else:
                merged.append(right[right_index])
                right_index +=1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index +=1
    
        while right_index < len(right):
            merged.append(right[right_index])
            right_index +=1

        return merged
    
    def merge_sort(self,list):
        if len(list) <= 1 :
            return list
    
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        left = self.merge_sort(left_half)
        right = self.merge_sort(right_half)

        return self.merge(left, right)
        





dna = input()

matched_dna = re.fullmatch('^s[^b].*',dna)
if matched_dna != None:
    dorsa = oct(dna)
    print(dorsa.oct_revised_dna())
else:

    matched_dna = re.fullmatch('^m.*',dna)
    if matched_dna != None:
        dorsa = crab(dna)
        print(dorsa.crab_revised_dna())
    else:

        matched_dna = re.fullmatch('^sb.*',dna)
        if matched_dna != None:
            dorsa = Bob(dna)
            dna = dorsa.crab_revised_dna()
            print(''.join(dorsa.merge_sort(list(str(len(dna))))))

        else:

            matched_dna = re.fullmatch('^s[^b].*',dna[::-1])
            if matched_dna != None:
                dorsa = oct(dna[::-1])
                print(dorsa.oct_revised_dna())
            else:

                matched_dna = re.fullmatch('^m.*',dna[::-1])
                if matched_dna != None:
                    dorsa = crab(dna[::-1])
                    print(dorsa.crab_revised_dna())
                else:

                    matched_dna = re.fullmatch('^sb.*',dna[::-1])
                    if matched_dna != None:
                        dorsa = Bob(dna[::-1])
                        dna = dorsa.crab_revised_dna()
                        print(''.join(dorsa.merge_sort(list(str(len(dna))))))

                    else:

                        print('invalid input')




    
