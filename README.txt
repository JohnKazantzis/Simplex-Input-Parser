Parsing a txt file containing a linear problem in general form:

min (max) c1x1 + c2x2 + … + cnxn
st       a11x1 + a12x2 + … + anxn ⊗ b1
         a21x1 + a22x2 + … + a2nxn ⊗ b2
         … … … ... … … … … …
         am1x1 + am2x2 + … + amnxn ⊗ bm
xj ≥ 0, (j = 1, …,n)

and outputting the same problem in matrix form:

min(max) c^Tx
s.t.  Ax⊗b
x≥0

> Coded in Python 3
