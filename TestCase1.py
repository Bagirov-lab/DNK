from DNK import GEN, compare_gens
import json
# Create two gens

# Example 1

# OS=Homo sapiens OX=9606 GN=CCKBR PE=1 SV=1
# MELLKLNRSVQGTGPGPGASLCRPGAPLLNSSSVGNLSCEPPRIRGAGTRELELAIRITL
# YAVIFLMSVGGNMLIIVVLGLSRRLRTVTNAFLLSLAVSDLLLAVACMPFTLLPNLMGTF
# IFGTVICKAVSYLMGVSVSVSTLSLVAIALERYSAICRPLQARVWQTRSHAARVIVATWL
# LSGLLMVPYPVYTVVQPVGPRVLQCVHRWPSARVRQTWSVLLLLLLFFIPGVVMAVAYGL
# ISRELYLGLRFDGDSDSDSQSRVRNQGGLPGAVHQNGRCRPETGAVGEDSDGCYVQLPRS
# RPALELTALTAPGPGSGSRPTQAKLLAKKRVVRMLLVIVVLFFLCWLPVYSANTWRAFDG
# PGAHRALSGAPISFIHLLSYASACVNPLVYCFMHRRFRQACLETCARCCPRPPRARPRAL
# PDEDPPTPSIASLSRLSYTTISTLGPG

Gen_1 = GEN(os='Homo sapiens', ox=9606, gn='CCKBR', pe=1, sv=1,
            fasta='MELLKLNRSVQGTGPGPGASLCRPGAPLLNSSSVGNLSCEPPRIRGAGTRELELAIRITLYAVIFLMSVGGNMLIIVVLGLSRRLRTVTNAFLLSLAVSDLLLAVACMPFTLLPNLMGTFIFGTVICKAVSYLMGVSVSVSTLSLVAIALERYSAICRPLQARVWQTRSHAARVIVATWLLSGLLMVPYPVYTVVQPVGPRVLQCVHRWPSARVRQTWSVLLLLLLFFIPGVVMAVAYGLISRELYLGLRFDGDSDSDSQSRVRNQGGLPGAVHQNGRCRPETGAVGEDSDGCYVQLPRSRPALELTALTAPGPGSGSRPTQAKLLAKKRVVRMLLVIVVLFFLCWLPVYSANTWRAFDGPGAHRALSGAPISFIHLLSYASACVNPLVYCFMHRRFRQACLETCARCCPRPPRARPRALPDEDPPTPSIASLSRLSYTTISTLGPG')

# Example 2

# OS=Homo sapiens OX=9606 GN=CCKAR PE=1 SV=1
# MDVVDSLLVNGSNITPPCELGLENETLFCLDQPRPSKEWQPAVQILLYSLIFLLSVLGNT
# LVITVLIRNKRMRTVTNIFLLSLAVSDLMLCLFCMPFNLIPNLLKDFIFGSAVCKTTTYF
# MGTSVSVSTFNLVAISLERYGAICKPLQSRVWQTKSHALKVIAATWCLSFTIMTPYPIYS
# NLVPFTKNNNQTANMCRFLLPNDVMQQSWHTFLLLILFLIPGIVMMVAYGLISLELYQGI
# KFEASQKKSAKERKPSTTSSGKYEDSDGCYLQKTRPPRKLELRQLSTGSSSRANRIRSNS
# SAANLMAKKRVIRMLIVIVVLFFLCWMPIFSANAWRAYDTASAERRLSGTPISFILLLSY
# TSSCVNPIIYCFMNKRFRLGFMATFPCCPNPGPPGARGEVGEEEEGGTTGASLSRFSYSH
# MSASVPPQ

Gen_2 = GEN(os='Homo sapiens', ox=9606, gn='CCKAR', pe=1, sv=1,
            fasta='MDVVDSLLVNGSNITPPCELGLENETLFCLDQPRPSKEWQPAVQILLYSLIFLLSVLGNTLVITVLIRNKRMRTVTNIFLLSLAVSDLMLCLFCMPFNLIPNLLKDFIFGSAVCKTTTYFMGTSVSVSTFNLVAISLERYGAICKPLQSRVWQTKSHALKVIAATWCLSFTIMTPYPIYSNLVPFTKNNNQTANMCRFLLPNDVMQQSWHTFLLLILFLIPGIVMMVAYGLISLELYQGIKFEASQKKSAKERKPSTTSSGKYEDSDGCYLQKTRPPRKLELRQLSTGSSSRANRIRSNSSAANLMAKKRVIRMLIVIVVLFFLCWMPIFSANAWRAYDTASAERRLSGTPISFILLLSYTSSCVNPIIYCFMNKRFRLGFMATFPCCPNPGPPGARGEVGEEEEGGTTGASLSRFSYSHMSASVPPQ')


# Compare them
Results = compare_gens([Gen_1, Gen_2, Gen_2])
print(json.dumps(Results))

