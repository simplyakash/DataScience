# 📊 Principal Component Analysis (PCA) — Step-by-Step

PCA is used to reduce dimensionality by finding directions (principal components) that maximize variance.

# 🎯 Goal

- Transform data into a new coordinate system
- Keep directions with maximum variance
- Reduce dimensions while preserving information

---

# 📌 Step 1: Prepare Data Matrix

Let data matrix be:

X = [x₁, x₂, ..., xₙ]ᵀ

Shape: n × d

- n = number of samples
- d = number of features

---

# 📌 Step 2: Mean Centering

Compute mean:

μ = (1/n) Σᵢ₌₁ⁿ xᵢ

Center data:

X_centered = X − μ

---

# 📌 Step 3: Compute Covariance Matrix

C = (1/n) X_centeredᵀ X_centered

---

# 📌 Step 4: Eigen Decomposition

Solve:

Cv = λv

- λ → eigenvalues (variance)
- v → eigenvectors (directions)

---

# 📌 Step 5: Sort Eigenvalues

Sort eigenvalues in descending order.

Select top k eigenvectors.

---

# 📌 Step 6: Form Projection Matrix

W = [v₁, v₂, ..., v_k]

---

# 📌 Step 7: Project Data

X_reduced = X_centered W

---

# 📊 Summary Table

| **Step** | **Operation**       | **Output**     |
| -------- | ------------------- | -------------- |
| 1        | Data matrix         | X              |
| 2        | Mean centering      | X_centered     |
| 3        | Covariance          | C              |
| 4        | Eigen decomposition | λ, v           |
| 5        | Select top k        | W              |
| 6        | Projection          | X_reduced      |

---

# 🔢 Small Example (2D → 1D)

# 📊 PCA — Full Numerical Example (Start → Final Projection)

This example shows complete PCA computation from raw data to final projected values.
# 🔢 PCA — Complete Numerical Example (2D → 1D)

This example demonstrates **Principal Component Analysis (PCA)** step by step, starting from the raw data and ending with the final projected values.

---

# 📊 Given Dataset

We have three 2-dimensional data points.

| Point | Coordinates |
| :---: | :---------: |
| A | (2, 0) |
| B | (0, 2) |
| C | (3, 1) |

---

# 📌 Step 1: Form the Data Matrix

```
      x   y
A = [ 2   0 ]
B = [ 0   2 ]
C = [ 3   1 ]
```

or

```
X =
[ 2   0 ]
[ 0   2 ]
[ 3   1 ]
```

- Rows = Data Points
- Columns = Features

Shape:

```
3 × 2
```

---

# 📌 Step 2: Compute the Mean of Each Feature

## Mean of X-coordinate

```
μx = (2 + 0 + 3) / 3
```

```
   = 5 / 3
```

```
   = 1.667
```

---

## Mean of Y-coordinate

```
μy = (0 + 2 + 1) / 3
```

```
   = 3 / 3
```

```
   = 1
```

Therefore,

```
Mean Vector

μ = (5/3 , 1)
```

---

# 📌 Step 3: Center the Data

Subtract the mean from every point.

## Point A

Original

```
(2 , 0)
```

Subtract Mean

```
(2 - 5/3 , 0 - 1)
```

Calculate each coordinate

```
2 = 6/3
```

```
6/3 - 5/3 = 1/3
```

```
0 - 1 = -1
```

Centered Point

```
(1/3 , -1)
```

---

## Point B

Original

```
(0 , 2)
```

Subtract Mean

```
(0 - 5/3 , 2 - 1)
```

```
= (-5/3 , 1)
```

---

## Point C

Original

```
(3 , 1)
```

Subtract Mean

```
(3 - 5/3 , 1 - 1)
```

Convert 3

```
3 = 9/3
```

```
9/3 - 5/3 = 4/3
```

```
1 - 1 = 0
```

Centered Point

```
(4/3 , 0)
```

---

# 📌 Step 4: Construct the Centered Data Matrix

```
Xcentered =

[  1/3   -1 ]
[ -5/3    1 ]
[  4/3    0 ]
```

---

# 📌 Step 5: Compute the Covariance Matrix

Formula

```
C = (1/n) × Xᵀ × X
```

Since

```
n = 3
```

---

## Transpose of Centered Matrix

```
Xᵀ =

[  1/3   -5/3   4/3 ]
[  -1      1     0  ]
```

---

## Compute XᵀX

### Element (1,1)

Multiply first row with first column.

```
(1/3 × 1/3)
+
(-5/3 × -5/3)
+
(4/3 × 4/3)
```

```
=
1/9
+
25/9
+
16/9
```

```
=
42/9
```

```
=
14/3
```

---

### Element (1,2)

Multiply first row with second column.

```
(1/3 × -1)
+
(-5/3 × 1)
+
(4/3 × 0)
```

```
=
-1/3
-
5/3
+
0
```

```
=
-6/3
```

```
=
-2
```

---

### Element (2,1)

Covariance matrices are symmetric.

```
= -2
```

---

### Element (2,2)

```
(-1 × -1)
+
(1 × 1)
+
(0 × 0)
```

```
=
1
+
1
+
0
```

```
= 2
```

---

Therefore

```
XᵀX =

[ 14/3   -2 ]
[ -2      2 ]
```

---

Now divide every element by 3.

```
C =
(1/3)

×

[ 14/3   -2 ]
[ -2      2 ]
```

Final covariance matrix

```
C =

[ 14/9   -2/3 ]
[ -2/3    2/3 ]
```

---

# 📌 Step 6: Compute the Eigenvalues

Solve

```
| C - λI | = 0
```

Substitute the covariance matrix

```
| 14/9 - λ     -2/3     |
|                       |
| -2/3        2/3 - λ   |
```

The determinant is

```
(14/9 - λ)(2/3 - λ)
-
(-2/3 × -2/3)
```

First compute

```
(-2/3 × -2/3)
=
4/9
```

Expand

```
(14/9 × 2/3)

-

(14/9)λ

-

(2/3)λ

+

λ²

-

4/9
```

Compute constants

```
14/9 × 2/3

=

28/27
```

```
28/27 - 4/9
```

Convert

```
4/9 = 12/27
```

```
28/27 - 12/27

=

16/27
```

Combine λ terms

```
-(14/9 + 2/3)
```

Convert

```
2/3 = 6/9
```

```
14/9 + 6/9

=

20/9
```

Characteristic equation

```
λ²

-

20/9 λ

+

16/27

=

0
```

Solving gives

```
λ₁ = 2
```

```
λ₂ = 2/9
```

The largest eigenvalue is

```
λ₁ = 2
```

---

# 📌 Step 7: Compute the Principal Eigenvector

Substitute

```
λ = 2
```

```
C - 2I
```

```
=

[ 14/9 - 2    -2/3 ]
[ -2/3       2/3-2 ]
```

Simplify

```
=

[ -4/9   -2/3 ]
[ -2/3   -4/3 ]
```

Let

```
v = (x , y)
```

Using the first equation

```
(-4/9)x

-

(2/3)y

=

0
```

Multiply by 9

```
-4x

-

6y

=

0
```

```
4x + 6y = 0
```

Divide by 2

```
2x + 3y = 0
```

Choose

```
x = 3
```

Then

```
2(3) + 3y = 0
```

```
6 + 3y = 0
```

```
3y = -6
```

```
y = -2
```

Eigenvector

```
v = (3 , -2)
```

---

# 📌 Step 8: Normalize the Eigenvector

Magnitude

```
||v||

=

√(3² + (-2)²)
```

```
=

√(9 + 4)
```

```
=

√13
```

Normalized Eigenvector

```
v =

(1/√13)

×

(3 , -2)
```

or

```
v =

(3/√13 , -2/√13)
```

---

# 📌 Step 9: Project Each Point onto the Principal Component

Projection Formula

```
Projection

=

Centered Point

·

Principal Eigenvector
```

---

## Point A

Centered Point

```
(1/3 , -1)
```

Projection

```
(1/3 × 3/√13)

+

(-1 × -2/√13)
```

```
=

1/√13

+

2/√13
```

```
=

3/√13
```

---

## Point B

Centered Point

```
(-5/3 , 1)
```

Projection

```
(-5/3 × 3/√13)

+

(1 × -2/√13)
```

```
=

-5/√13

-

2/√13
```

```
=

-7/√13
```

---

## Point C

Centered Point

```
(4/3 , 0)
```

Projection

```
(4/3 × 3/√13)

+

(0 × -2/√13)
```

```
=

4/√13
```

---

# 📊 Final Projected Dataset

| Original Point | Centered Point | Projection on PC1 |
|---------------|----------------|-------------------|
| (2, 0) | (1/3, -1) | 3/√13 |
| (0, 2) | (-5/3, 1) | -7/√13 |
| (3, 1) | (4/3, 0) | 4/√13 |

---

# 🎯 Final Result

Original 2D Data

```
(2,0)

(0,2)

(3,1)
```

↓

Centered Data

```
(1/3,-1)

(-5/3,1)

(4/3,0)
```

↓

Covariance Matrix

```
[ 14/9   -2/3 ]
[ -2/3    2/3 ]
```

↓

Principal Eigenvector

```
(3/√13 , -2/√13)
```

↓

Final 1D Representation

```
3/√13

-7/√13

4/√13
```

---

# 🧠 Key Takeaways

- Compute the mean of each feature.
- Center the data by subtracting the mean.
- Compute the covariance matrix.
- Find the eigenvalues and eigenvectors.
- Select the eigenvector corresponding to the **largest eigenvalue** (the first principal component).
- Normalize the eigenvector.
- Project each centered point onto the principal component using the dot product.
- The resulting scalar values are the new lower-dimensional representation of the original data.
```
---

