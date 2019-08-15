from mendeleev import Fe, element

print(Fe.name)
print(Fe.atomic_number)


al = element(13)
print(al.name)


c, h, o = element(['C', 'Hydrogen', 8])

print(c.name, h.name, o.name )

Fe = element('Fe')

for isotopes in Fe.isotopes:
    print(isotopes)


# element.py Si





