import re


class Octopus:
    def __init__(self, dna):
        self.dna = dna

    def oct_revised_dna(self):
        dna = str(self.dna)

        for i in range(len(dna)):
            if dna[i] == 'x':
                dna += str(i)
                break

        for i in range(len(dna) - 2):
            if dna[i] == dna[i + 1] == dna[i + 2]:
                dna = dna.replace(dna[i] + dna[i + 1] + dna[i + 2], '(0_0)')

        return dna


class Crab:
    def __init__(self, dna):
        self.dna = dna

    def crab_revised_dna(self):
        dna = str(self.dna)

        dna += dna[:10]
        dna = dna.replace('tt', 'o')

        return dna


class Bob(Crab):
    def merge(self, left, right):
        merged = []
        right_index = 0
        left_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    def merge_sort(self, seq):
        if len(seq) <= 1:
            return seq

        mid = len(seq) // 2
        left_half = seq[:mid]
        right_half = seq[mid:]

        left = self.merge_sort(left_half)
        right = self.merge_sort(right_half)

        return self.merge(left, right)


def process_dna_sequence(dna):
    matched_dna = re.fullmatch('^s[^b].*', dna)
    if matched_dna:
        dorsa = Octopus(dna)
        print(dorsa.oct_revised_dna())
    else:
        matched_dna = re.fullmatch('^m.*', dna)
        if matched_dna:
            dorsa = Crab(dna)
            print(dorsa.crab_revised_dna())
        else:
            matched_dna = re.fullmatch('^sb.*', dna)
            if matched_dna:
                dorsa = Bob(dna)
                revised_dna = dorsa.crab_revised_dna()
                print(''.join(map(str, dorsa.merge_sort(list(str(len(revised_dna)))))))
            else:
                reversed_dna = dna[::-1]
                matched_dna = re.fullmatch('^s[^b].*', reversed_dna)
                if matched_dna:
                    dorsa = Octopus(reversed_dna)
                    print(dorsa.oct_revised_dna())
                else:
                    matched_dna = re.fullmatch('^m.*', reversed_dna)
                    if matched_dna:
                        dorsa = Crab(reversed_dna)
                        print(dorsa.crab_revised_dna())
                    else:
                        matched_dna = re.fullmatch('^sb.*', reversed_dna)
                        if matched_dna:
                            dorsa = Bob(reversed_dna)
                            revised_dna = dorsa.crab_revised_dna()
                            print(''.join(map(str, dorsa.merge_sort(list(str(len(revised_dna)))))))
                        else:
                            print('Invalid input')


dna_input = input()
process_dna_sequence(dna_input)
