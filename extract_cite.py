import sys

import rispy

from PyPDF2 import PdfFileReader

try:
    to_parse = sys.argv[1]
except:
    raise Exception("no file given")

with open(to_parse, 'rb') as infile:
    reader = PdfFileReader(infile)
    firstpage = reader.getPage(0).extractText()
    
styles = ['Bluebook 21st ed.',
          'ALWD 7th ed.',
          'APA 7th ed.',
          'Chicago 17th ed.',
          'McGill Guide 9th ed.',
          'AGLC 4th ed.',
          'MLA 9th ed.',
          'OSCOLA 4th ed.',
          'Provided by:']

lines = [x.strip() for x in firstpage.split('\n')]

def find_style(style):
    next_style=styles[styles.index(style) + 1]
    start_ind = lines.index(style)
    end_ind = lines.index(next_style)
    return ' '.join(lines[start_ind + 1:end_ind])
        
chicago = find_style('Chicago 17th ed.')
bluebook = find_style('Bluebook 21st ed.')

def find_authors():
    authorlist = chicago.split(',')[0]
    if ';' in authorlist:
        return authorlist.split(';')
    else:
        return [authorlist]

def find_pages():
    pages = chicago.strip().split(' ')[-1]
    indiv = pages.split('-')
    return {'first_page': indiv[0], 'last_page': indiv[-1]}

def find_year():
    return bluebook.strip().split(' ')[-1][1:-2]
    
def to_ris():
    pages = find_pages()
    print(first)
    out = {'type_of_reference': 'JOUR',
           'first_authors': find_authors(),
           'start_page': pages['first_page'],
           'end_page': pages['last_'],
           'year': find_year()}
    return rispy.dumps([out])

print(to_ris())

# print(find_authors())
# print(find_pages())
# print(find_year())
