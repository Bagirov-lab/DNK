from copy import deepcopy as copy


class GEN(object):
    def __init__(self, os, ox, gn, pe, sv, fasta):
        self.os = os
        self.ox = ox
        self.gn = gn
        self.pe = pe
        self.sv = sv
        self.fasta = fasta


# TODO: More complex logic if lengths of gens' FASTA is different
def compare_gens(gens):
    # We check that all gens are correct type
    for gen in gens:
        if not type(gen) is GEN:
            raise TypeError('All gens in supplied gens list shall be of type GEN !')

    # Make tuples of two different gens which would be compared
    gens_2 = [(gen1, gen2) for gen1 in gens for gen2 in gens if gen1.gn != gen2.gn]

    # We check the number of gens ( currently support only 2 )
    if len(gens_2) == 1:
        raise ValueError('The is no reason to compare 1 gen with its own !')

    # Logic for comparison of two gens

    result_2 = {}

    for i_gen, j_gen in gens_2:
        min_len = min(len(i_gen.fasta), len(j_gen.fasta))  # Minimal length of two gens FASTA
        i_inter = {}  # Store intersections

        # Compare element wise
        for iPos in range(min_len):  # Loop over position
            if i_gen.fasta[iPos] == j_gen.fasta[iPos]:  # Compare value in the same position of two FASTAs
                i_inter[iPos] = i_gen.fasta[iPos]  # Store intersection

        # Save result into dictionary container
        result_2[str(i_gen.gn) + ' and ' + str(j_gen.gn)] = copy(i_inter)

    # Return results
    return result_2


# TODO: return info from BLAST API
# https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=DeveloperInfo

def get_info():
    pass
