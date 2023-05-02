from Bio.Seq import Seq



def print_protein_sequence_from_DNA (DNA):
    coding_DNA = Seq(DNA)
    protein_seq = coding_DNA.translate()
    print(f'Последовательность кодирующей ДНК: {coding_DNA}\n')
    print(f'Последовательность кодируемого белка: {protein_seq}')

DNA = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

print_protein_sequence_from_DNA(DNA)
