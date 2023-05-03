from datetime import datetime
import locale
from biopython import print_protein_sequence_from_DNA
from salary import calculate_salary
from people import get_employees

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
DNA = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"



if __name__ == '__main__':
    print(f"Сегодня: {datetime.now().strftime('%d %B %Y')}\n")
    print_protein_sequence_from_DNA(DNA)
    print('')
    calculate_salary('Максим Павленко', 100000)
    print('')
    get_employees('company_employees.txt')
    print('')