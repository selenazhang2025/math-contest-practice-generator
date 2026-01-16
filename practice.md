# Math Contest Practice Set
**Seed:** `42`

## Problems

**1. (Algebra)** Solve $x^2 + (8)x + (0) = 0$.

**2. (Number Theory)** Find the multiplicative inverse of 4 modulo 9.

**3. (Algebra)** Solve $x^2 + (1)x + (-30) = 0$.

**4. (Algebra)** Solve $x^2 + (14)x + (48) = 0$.

**5. (Number Theory)** Find the multiplicative inverse of 8 modulo 9.

**6. (Functions)** Given $f(x)=2x+(7)$, find $f^{-1}(x)$.

**7. (Number Theory)** Find the multiplicative inverse of 15 modulo 19.

**8. (Number Theory)** Find the multiplicative inverse of 11 modulo 13.

**9. (Combinatorics)** How many integers from 1 to 80 are divisible by 4 or 8?

**10. (Combinatorics)** How many integers from 1 to 115 are divisible by 4 or 6?

## Answer Key

- **1**: x = -8, 0
- **2**: 7
- **3**: x = -6, 5
- **4**: x = -8, -6
- **5**: 8
- **6**: (x-(7))/2
- **7**: 14
- **8**: 6
- **9**: 20
- **10**: 38

## Solutions

### 1. (Algebra)

Factor the quadratic:

$x^2 + (8)x + (0) = (x - (-8))(x - (0))$.

Set each factor to zero:

$x = -8$ or $x = 0$.

### 2. (Number Theory)

We need $x$ such that $4x \equiv 1 \pmod{9}$.

Testing residues (or using the Euclidean algorithm), we find $4\cdot7 = 28 \equiv 1 \pmod{9}$.

So the inverse is 7.

### 3. (Algebra)

Factor the quadratic:

$x^2 + (1)x + (-30) = (x - (-6))(x - (5))$.

Set each factor to zero:

$x = -6$ or $x = 5$.

### 4. (Algebra)

Factor the quadratic:

$x^2 + (14)x + (48) = (x - (-8))(x - (-6))$.

Set each factor to zero:

$x = -8$ or $x = -6$.

### 5. (Number Theory)

We need $x$ such that $8x \equiv 1 \pmod{9}$.

Testing residues (or using the Euclidean algorithm), we find $8\cdot8 = 64 \equiv 1 \pmod{9}$.

So the inverse is 8.

### 6. (Functions)

Let $y=f(x)$.

$y=2x+(7)$.

Swap $x$ and $y$: $x=2y+(7)$.

Solve for $y$: $x-(7)=2y \Rightarrow y=\frac{x-(7)}{2}$.

So $f^{-1}(x)=\frac{x-(7)}{2}$.

### 7. (Number Theory)

We need $x$ such that $15x \equiv 1 \pmod{19}$.

Testing residues (or using the Euclidean algorithm), we find $15\cdot14 = 210 \equiv 1 \pmod{19}$.

So the inverse is 14.

### 8. (Number Theory)

We need $x$ such that $11x \equiv 1 \pmod{13}$.

Testing residues (or using the Euclidean algorithm), we find $11\cdot6 = 66 \equiv 1 \pmod{13}$.

So the inverse is 6.

### 9. (Combinatorics)

Count multiples of 4: $\lfloor 80/4\rfloor = 20$.

Count multiples of 8: $\lfloor 80/8\rfloor = 10$.

Subtract multiples of lcm(4,8)=8: $\lfloor 80/8\rfloor = 10$.

Total = 20+10-10 = 20$.

### 10. (Combinatorics)

Count multiples of 4: $\lfloor 115/4\rfloor = 28$.

Count multiples of 6: $\lfloor 115/6\rfloor = 19$.

Subtract multiples of lcm(4,6)=12: $\lfloor 115/12\rfloor = 9$.

Total = 28+19-9 = 38$.
