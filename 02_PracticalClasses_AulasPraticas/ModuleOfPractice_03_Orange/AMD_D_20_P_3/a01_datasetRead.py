# to use accented characters in the code
# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# ver: v07 (Python34, Orange3)
# ===============================


# __________________________________________
# Orange Documentation:
# http://docs.orange.biolab.si
#
# Orange Reference Manual:
# http://docs.orange.biolab.si/3/data-mining-library/#reference
#
# Tutorial:
# http://docs.orange.biolab.si/3/data-mining-library/#tutorial
#
# details about data (attribute+class) characterization:
# http://docs.orange.biolab.si/3/data-mining-library/tutorial/data.html#data-input
# __________________________________________

# _______________________________________________________________________________
# Modules to Evaluate
import sys
from u01_util import my_print
import Orange as DM


# _______________________________________________________________________________
# read a "dataset"
# the file name (that can be passed in the command line)
fileName = "./_dataset/lenses.tab"
# fileName = "./_dataset/adult_sample"
if len(sys.argv) > 1:
    fileName = sys.argv[1]

try:
    dataset = DM.data.Table(fileName)
except:
    my_print("--->>> error - can not open the file: %s" % fileName)
    exit()
'''
print('\nDataset\n', dataset)

print('\nDataset Domain\n', dataset.domain)

print('\nDataset Domain Variables\n', dataset.domain.variables)

print('\nDataset Domain Attributes\n', dataset.domain.attributes)
'''
'''
# _______________________________________________________________________________
# variables: name (type = discrete | continuous): [value1, value2, ...]
# variables, in Orange, refer to features or class
# cf., http://docs.orange.biolab.si/3/data-mining-library/tutorial/data.html#exploration-of-the-data-domain
variable_list = dataset.domain.variables
#variable_list = dataset.domain.attributes

my_print(aStr=">> %d Variables (attributes+class) <<" % len(variable_list))
print(":: name (type): [value1, value2, ...]")

nDisc = 0
nCont = 0
nStr = 0
for variable in variable_list:
    print(":: %s %s" % (variable.name, variable.TYPE_HEADERS)),
    if variable.is_discrete:
        print(": %s " % str(variable.values))
        nDisc += 1
    elif variable.is_continuous:
        nCont += 1
    else:
        nStr += 1
my_print(">> Types: %d discrete, %d continuous <<" % (nDisc, nCont))
'''
'''
# _______________________________________________________________________________
# Class: name (type = discrete | continuous): <value1, value2, ...>
the_class = dataset.domain.class_var
my_print(">> Class <<")
print(":: %s (%s): %s " % (the_class.name,
                           the_class.TYPE_HEADERS,
                           the_class.values))
'''
'''
# _______________________________________________________________________________
# First N Instances
N = 20
my_print("First %d instances:" % N)
for i in range(N):
    print(dataset[i])
'''

'''
j) A diferença entre 'dataset.domain.variables' e 'dataset.domain.attributes' é que
as variáveis têm em consideração as classes para além dos atributos.

k) 'dataset.domain.class_var' é semelhante a 'dataset.domain.attributes' onde
o primeiro contém só as classes e o segundo só os atributos.
'dataset.domain.variables' contém tudo (atributos + classes).

É possível obter os tipos e os valores com estes métodos.

É também possível aceder às linhas da tabela a partir do indice.
'''