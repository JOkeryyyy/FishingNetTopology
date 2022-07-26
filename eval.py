from sklearn.metrics import r2_score

result10 = [2, 0, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 0, 2, 1, 4, 5, 2, 1, 0, 2, 2, 1, 3, 0, 2, 1, 3,
            0, 2, 2, 1, 3, 0, 2, 2, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 4, 0, 1, 3, 4, 0, 1, 4,
            1, 0, 1, 4, 0, 0, 0, 0, 2, 2, 2]

result05 = [2, 0, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 0, 2, 1, 4, 5, 2, 1, 0, 2, 2, 1, 3, 0, 2, 1, 3,
            0, 2, 2, 1, 3, 0, 2, 2, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 4, 0, 1, 3, 4, 0, 1, 4,
            1, 0, 1, 4, 0, 0, 0, 0, 2, 2, 2]

result02 = [2, 5, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 5, 2, 2, 1, 3, 0, 2, 1, 3,
            5, 2, 2, 1, 3, 0, 2, 2, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 4, 0, 1, 3, 4, 5, 1, 4,
            1, 0, 1, 4, 5, 5, 0, 5, 2, 2, 2]

aresult20 = [2, 0, 1, 4, 0, 2, 1, 4, 5, 2, 1, 4, 0, 2, 1, 4, 0, 2, 1, 4, 0, 2, 1, 4, 0, 2, 1, 0, 2, 2, 1, 3, 0, 2, 1, 3,
             0, 2, 2, 1, 3, 0, 2, 2, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 4, 0, 1, 3, 4, 0, 1, 4,
             1, 0, 1, 4, 0, 0, 0, 0, 2, 2, 2]

aresult10 = [2, 0, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 0, 2, 1, 4, 0, 2, 1, 0, 2, 2, 1, 3, 0, 2, 1, 3,
             0, 2, 2, 1, 3, 0, 2, 2, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 4, 0, 1, 3, 4, 0, 1, 4,
             1, 0, 1, 4, 0, 0, 0, 0, 2, 2, 2]
aresult05 = [2, 0, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 0, 2, 1, 4, 5, 2, 1, 0, 2, 2, 1, 3, 0, 2, 1, 3,
             0, 2, 2, 1, 3, 0, 2, 2, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 4, 0, 1, 3, 4, 0, 1, 4,
             1, 0, 1, 4, 0, 0, 0, 0, 2, 2, 2]
aresult02 = [2, 0, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 4, 5, 2, 1, 5, 2, 2, 1, 3, 5, 2, 1, 3,
             5, 2, 2, 1, 3, 0, 2, 2, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 4, 0, 1, 3, 4, 0, 1, 4,
             1, 0, 1, 4, 0, 0, 0, 0, 2, 2, 2]
aresult02v2 = [0, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 0, 2, 1, 2, 2, 2, 1,
               2, 2, 2, 2, 1, 2, 2, 0, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 0, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2,
               1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2]

aresult02v3 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 5, 2, 0, 1, 3, 5, 0, 1,
               3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 4, 0, 1, 3, 4, 0,
               1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 5, 2, 2]

standardv1 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 5, 2, 0, 1, 3, 5, 0, 1,
              3, 5, 2, 0, 1, 3, 5, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 4, 0, 1, 3, 4, 0,
              1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 2, 2, 2]

result02v2 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 5, 2, 0, 1, 3, 5, 0, 1,
              3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 4, 0, 1, 3, 4, 0,
              1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 5, 2, 2]

result02vrf = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 5, 2, 0, 1, 3, 5, 0, 1,
               3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 4, 0, 1, 3, 4, 0,
               1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
result015vrf = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 5, 2, 0, 1, 3, 5, 0, 1,
                3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 4, 5, 1, 3, 4, 0,
                1, 4, 1, 0, 1, 4, 5, 5, 0, 0, 5, 2, 2]
aresult015v2 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 5, 1, 4, 5, 0, 1, 5, 2, 0, 1, 3, 5, 0, 1,
                3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 4, 5, 1, 3, 4, 5,
                1, 4, 1, 0, 1, 4, 5, 5, 0, 5, 5, 2, 2]
aresult02v2 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 5, 2, 0, 1, 3, 5, 0, 1,
               3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 4, 0, 1, 3, 4, 0,
               1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 5, 2, 2]
liner = [2, 5, 1, 4, 5, 5, 1, 4, 5, 5, 1, 4, 5, 5, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 5, 1, 4, 5,
         5, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 5, 1, 3, 5, 2, 5, 1, 3, 5, 1, 3, 5, 1, 3, 2, 5, 1, 3, 2, 5, 1, 3, 2, 5,
         1, 3, 4, 5, 1, 3, 4, 5, 1, 4, 1, 5, 1, 4, 0, 0, 0, 5, 5, 2, 2]

mlp = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 0, 1, 4, 5, 0,
       1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3,
       4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]

standard = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 0, 1, 4,
            5, 0, 1, 5, 2, 0, 1, 3, 5, 0, 1, 3, 5, 2, 0, 1, 3, 5, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3,
            2, 0, 1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 2, 2, 2]

forest = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
          0, 1, 5, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
tree = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
        0, 1, 5, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
        1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
tree01 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 0, 1, 4, 5,
          0, 1, 5, 2, 5, 1, 3, 5, 0, 1, 3, 5, 2, 0, 1, 3, 5, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5,
          1, 3, 4, 5, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 5, 5, 0, 0, 5, 2, 2]

tree02 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 0, 1, 4, 5,
          0, 1, 5, 2, 0, 1, 3, 5, 0, 1, 3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5,
          1, 3, 4, 5, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 5, 2, 2]

tree03 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
          0, 1, 5, 2, 0, 1, 3, 0, 0, 1, 3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]

tree04 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
          0, 1, 5, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]

tree05 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
          0, 1, 5, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]

tree06 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
          0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]

tree07 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
          0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]

tree08 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
          0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]

tree09 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 0,
          0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
tree10 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 0,
          0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
          1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
mlp1 = [2, 5, 1, 4, 5, 5, 1, 4, 5, 5, 1, 4, 5, 5, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 5, 1, 4, 5,
        5, 1, 5, 2, 5, 1, 3, 5, 5, 1, 3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5,
        1, 3, 4, 5, 1, 3, 4, 5, 1, 4, 1, 5, 1, 4, 5, 5, 5, 5, 5, 2, 2]
mlp2 = [2, 5, 1, 4, 5, 5, 1, 4, 5, 5, 1, 4, 5, 5, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 5, 1, 4, 5,
        0, 1, 5, 2, 0, 1, 3, 0, 0, 1, 3, 5, 2, 0, 1, 3, 0, 2, 5, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 5, 1, 3, 2, 5,
        1, 3, 4, 0, 1, 3, 4, 5, 1, 4, 1, 0, 1, 4, 5, 5, 0, 5, 5, 2, 2]
mlp3 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 0, 1, 4, 5,
        0, 1, 5, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
        1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
mlp4 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 0, 1, 4, 5,
        0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
        1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
mlp5 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
        0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
        1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
mlp6 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
        0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
        1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
mlp7 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
        0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
        1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
mlp8 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
        0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
        1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
mlp9 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
        0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
        1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]
mlp10 = [2, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 0, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 0, 0, 1, 4, 5,
         0, 1, 0, 2, 0, 1, 3, 0, 0, 1, 3, 0, 2, 0, 1, 3, 0, 2, 0, 1, 3, 0, 1, 3, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0,
         1, 3, 4, 0, 1, 3, 4, 0, 1, 4, 1, 0, 1, 4, 0, 0, 0, 0, 0, 2, 2]

# results = [result10, result05, result02, aresult20, aresult10, aresult05, aresult02, aresult02v2,aresult02v3]
# results = [liner, mlp, forest, tree]
# results = [tree01, tree02, tree03, tree04, tree05, tree06, tree07, tree08, tree09, tree10]
results = [mlp1, mlp2, mlp3, mlp4, mlp5, mlp6, mlp7, mlp8, mlp9, mlp10]
# resultOPT
# for a in results:
#     r2=r2_score(a,standard)
#     print(r2)
counter = 1
for b in results:
    print(b)
    i = 0
    sum = 0
    xorarrar = []
    while i < 83:
        if b[i] != standard[i]:
            print(i, " input ", b[i], " standard ", standard[i])
            sum += 1
        i += 1
    print("param ", counter, " sum ", sum)
    print("========================================================")
    counter += 1

# xorresult = []
# for thisresult in results:
#     xorarray = []
#     for x,y in thisresult,standard:
#         a = (x ^ y)
#         xorarray.append(a)
#     xorresult.append(xorarray)
#     counter = 0
#     for countxor in xorarray:
#         if countxor == 0:
#             counter+=1
#
#     print(counter)
