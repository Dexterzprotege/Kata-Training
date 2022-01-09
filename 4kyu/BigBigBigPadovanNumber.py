# Question: https://www.codewars.com/kata/5819f1c3c6ab1b2b28000624/train/python

# Approach:
# According to the solution: https://math.stackexchange.com/questions/3798107/is-there-a-better-way-to-calculate-padovan-sequence-than-on
'''
Identity matrix (M) =  0 1 0
                       0 0 1
                       1 1 0
M^n = P(n-4) P(n-2) P(n-3)
      P(n-3) P(n-1) P(n-2)
      P(n-2) P(n)   P(n-1)
 
Hence: Padovan Number = M^n[-1][1] '''
  

# Solution:
def padovan(n):
    def matmul(M1, M2):
        a1 = (M1[0][0]*M2[0][0]) + (M1[0][1] * M2[1][0]) + (M1[0][2] * M2[2][0])
        a2 = (M1[0][0]*M2[0][1]) + (M1[0][1] * M2[1][1]) + (M1[0][2] * M2[2][1])
        a3 = (M1[0][0]*M2[0][2]) + (M1[0][1] * M2[1][2]) + (M1[0][2] * M2[2][2])
        a4 = (M1[1][0]*M2[0][0]) + (M1[1][1] * M2[1][0]) + (M1[1][2] * M2[2][0])
        a5 = (M1[1][0]*M2[0][1]) + (M1[1][1] * M2[1][1]) + (M1[1][2] * M2[2][1])
        a6 = (M1[1][0]*M2[0][2]) + (M1[1][1] * M2[1][2]) + (M1[1][2] * M2[2][2])
        a7 = (M1[2][0]*M2[0][0]) + (M1[2][1] * M2[1][0]) + (M1[2][2] * M2[2][0])
        a8 = (M1[2][0]*M2[0][1]) + (M1[2][1] * M2[1][1]) + (M1[2][2] * M2[2][1])
        a9 = (M1[2][0]*M2[0][2]) + (M1[2][1] * M2[1][2]) + (M1[2][2] * M2[2][2])
        return [[a1, a2, a3], [a4, a5, a6], [a7, a8, a9]]
      
    def matpow(mat, p):
        result = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
        while p > 0:
            if p & 1:
                result = matmul(result, mat)
            mat = matmul(mat, mat)
            p >>= 1
        return result
      
    matrix = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
    return matpow(matrix, n)[-1][1]

# Sample testcases:
'''@test.describe("Sample tests")
def sample_tests():
    @test.it("Small numbers")
    def tests_for_small_numbers():
        test.assert_equals(padovan(0), 1)
        test.assert_equals(padovan(1), 1)
        test.assert_equals(padovan(2), 1)
        test.assert_equals(padovan(3), 2)
        test.assert_equals(padovan(4), 2)
        test.assert_equals(padovan(5), 3)
    
    @test.it("Bigger values")
    def tests_for_bigger_values():
        test.assert_equals(padovan(20), 200)
        test.assert_equals(padovan(43), 128801)
        test.assert_equals(padovan(13), 28)
        test.assert_equals(padovan(21), 265)
        test.assert_equals(padovan(56), 4983377)
    
    @test.it("Large values")
    def tests_for_large_values():
        test.assert_equals(padovan(10000), 1238358674810225710362658358305326353370085565931480149540034178112109760421015368749092070315121317870307038461488247956649708270657794894885538925517998388256742182698382456427711487422223038736627967155267078110981718834020538207808586743711286143816901810046359193981629027093200200508417293576478290133427896373130524152915913791962807043255794740446866326974355835006521669447583271229269202722266564495741496188243513249480056909851881145447606787553763287102543679736466917309837173929654707675604451464881452000229987246555452074450251348990846417360558197609644968211961428439293100876070846602777333215135786401695835291812116617171128079762494461137781825625222566318201912094773214136061441206078387058357868441106686658265385073871486740643233175195911867015708104495734874596876979897722105812013852492945492721475554173381085310702750145747360244997526194100256682358074472811516635989554395219200062517637855903323313305244981191583938347395130737709135610410619241163145637108749292778366122098610083472666493806370147233676522253740527327122274074241570609223409271855541745949311673614243417005985937607758981579784801122742308711394667390781254387866417408992983075631849543130311840238397801845770130)
        test.assert_equals(padovan(3450), 15290542901917498710980478480175171734044111509449974256136444682038299606236013509928901745590803544097013581729494627028132167291410901681380317922934072540064735046317881429412874207889041384358102260504703807884535106008621364115073354573431544947041652396476005905820872828794694064963233139215518804783365787482781149012781315674129005218887791525943176680081123189298474501891974741083308571884684763124456770206684)
        test.assert_equals(padovan(7111), 18979122406847752793961243379525291536030166630502076496669925404749864284000041316147241255414177230507092555344793125667600122281306770400287636684506300503127252493231367470684174324835505688122147924215802733552228876602660619955782560465116888881003007703094721791661104468545125077245750852403225154699124611716118943555618728158489946522178206552160629794128601512343346987141425105171064195460211556637596861905158327310787836167272740122301572364000138490591491154483123274154624208060181176004878463515174861409735310096468899468029544136999515416101389430555642222170186380708334307606249224905561085198322664677969328756552702525447016480239817987686259771139886999253803378345212257482648599936768934514489799742803154759533552754367360936328051104895946564572465777145009158159465369095881813556291340543724049817255768467516997201126017466529171045799760)
'''