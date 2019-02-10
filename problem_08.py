"""Problem 08 - Largest product in a series

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?"""

_1000_digit_number = f'731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947' \
    f'88518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668' \
    f'96648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629' \
    f'04915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220' \
    f'23542180975125454059475224352584907711670556013604839586446706324415722155397536978179778461740649551492908625' \
    f'69321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758' \
    f'86668811642717147992444292823086346567481391912316282458617866458359124566529476545682848912883142607690042242' \
    f'19022671055626321111109370544217506941658960408071984038509624554443629812309878799272442849091888458015616609' \
    f'79191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252' \
    f'483600823257530420752963450'

number_of_adjacent = 13
max_number = 0
for i in range(len(_1000_digit_number) - number_of_adjacent - 1):
    this_number = 1
    for j in _1000_digit_number[i:i + number_of_adjacent]:
        # adding this break condition skips multiplication by zero
        # 723 loops are skipped and code runs 2 times faster
        if j == '0':
            break

        this_number *= int(j)

    if max_number < this_number:
        max_number = this_number

print(max_number)

