from Bio.Seq import Seq


#Можуль biopython мне понравился тк он позвояет работать с биологическими объектами ДНК, белки и тд
#С ними я работал при получении кандидатской степени
def print_protein_sequence_from_DNA (DNA):
    coding_DNA = Seq(DNA)
    protein_seq = coding_DNA.translate()
    print(f'Последовательность кодирующей ДНК: {coding_DNA}')
    print(f'Последовательность кодируемого белка: {protein_seq}')


