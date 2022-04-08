from PyQt5 import uic


designer_interfaces_to_compile = ['designerlogininterface', 'designerchatinterface']

for interface in designer_interfaces_to_compile:
    with open(f'{interface}.py', 'w') as interfacepy:
        uic.compileUi(f'{interface}.ui', interfacepy)

