import importlib

import aula99_m

print(aula99_m.variavel)

for i in range(10):
    importlib.reload(aula99_m)
    print(i)

print('Fim')

#caso voce queira "recarregar um singleton vc faz importlibe"
