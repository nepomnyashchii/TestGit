from mendeleev import Fe, element

Si = element("Si")

print(Si)

o = element('O')
print(o.ionenergies)

print("{0:^4s} {1:^4s} {2:^10s} {3:8s} {4:6s} {5:5s}\n{6}".format("AN", "MN", "Mass", "Unc.", "Abu.", "Rad.", "-"*42))
for iso in Fe.isotopes:
    print('{0:4d} {1:4d} {2:100.10f} {3:8.2e} {4:6.2f} {5:}'.format(
        iso.atomic_number, iso.mass_number, iso.mass, iso.mass_uncertainty, iso.abundance * 100.0, iso.is_radioactive)
        )

for ir in Fe.ionic_radii:
    print(ir)