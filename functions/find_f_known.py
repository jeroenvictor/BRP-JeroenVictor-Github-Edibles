import numpy as np

def find_F(ion, wave):


    filename = '/export/home/klay/python/edibles/atomic_lines.txt'

    with open(filename) as f:

        first_line = f.readline()
        names = first_line.split('|')
        indeces = []

        for i in range(len(names)):
            indeces.append(len(names[i]))
        for i in range(1, len(indeces)):
            indeces[i] += indeces[i-1] +1

        wavelength = []
        species = []
        TT = []
        Term = []
        J_ik = []
        f_ik = []
        TPF = []
        LVL_EN_CM_1 = []
        REF = []
        new_line = []
        data = [wavelength, species, TT, Term, J_ik, f_ik, TPF, LVL_EN_CM_1, REF, new_line]

        for line in f:
            start = 0
            for i in range(len(indeces)):
                stop = indeces[i] 
                data[i].append(line[start:stop].strip())
                start = indeces[i]
        data.insert(0, names)
        data = np.asarray(data)

    indeces = []
    for index in range(len(species)):
        if species[index] == ion:
            indeces.append(index)

    diff = []
    for i in indeces:
        wave_table = float(wavelength[i])
        diff.append(np.abs(wave_table-wave))

    index = np.argmin(diff)
    f_known = float(f_ik[index])
    return f_known


if __name__ == '__main__':

    ion = 'Na I'
    wave = 3302.7
    f = find_F(ion, wave)
    print(f)