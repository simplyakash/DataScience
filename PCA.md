📊 Principal Component Analysis (PCA) — Step-by-Step

PCA is used to reduce dimensionality by finding directions (principal components) that maximize variance.

🎯 Goal
Transform data into a new coordinate system
Keep directions with maximum variance
Reduce dimensions while preserving information

📌 Step 1: Prepare Data Matrix

Let data matrix be:

$X = [x_1, x_2, \dots, x_n]^T$

Shape: $n \times d$
$n$ = number of samples
$d$ = number of features

📌 Step 2: Mean Centering

Compute mean:

$\mu = \frac{1}{n} \sum_{i=1}^{n} x_i$

Center data:

$X_{centered} = X - \mu$

📌 Step 3: Compute Covariance Matrix

$C = \frac{1}{n} X_{centered}^T X_{centered}$

📌 Step 4: Eigen Decomposition

Solve:

$C v = \lambda v$

$\lambda$ → eigenvalues (variance)
$v$ → eigenvectors (directions)

📌 Step 5: Sort Eigenvalues
Sort eigenvalues in descending order
Select top $k$ eigenvectors

📌 Step 6: Form Projection Matrix

$W = [v_1, v_2, ..., v_k]$

📌 Step 7: Project Data

$X_{reduced} = X_{centered} W$

📊 Summary Table
| **Step** | **Operation**       | **Output**     |
| -------- | ------------------- | -------------- |
| 1        | Data matrix         | $X$            |
| 2        | Mean centering      | $X_{centered}$ |
| 3        | Covariance          | $C$            |
| 4        | Eigen decomposition | $\lambda, v$   |
| 5        | Select top $k$      | $W$            |
| 6        | Projection          | $X_{reduced}$  |

🔢 Small Example (2D → 1D)

📊 PCA — Full Numerical Example (Start → Final Projection)

This example shows complete PCA computation from raw data to final projected values.

🎯 Given Data (2D)

Points:

$(2, 0)$
$(0, 2)$
$(3, 1)$

📌 Step 1: Form Data Matrix

$X = [(2,0), (0,2), (3,1)]$

📌 Step 2: Compute Mean

$\mu = \left(\frac{2+0+3}{3}, \frac{0+2+1}{3}\right) = \left(\frac{5}{3}, 1\right)$

📌 Step 3: Center the Data

Subtract mean from each point:

$(2,0) \rightarrow (1/3, -1)$
$(0,2) \rightarrow (-5/3, 1)$
$(3,1) \rightarrow (4/3, 0)$

📌 Step 4: Covariance Matrix

$C = \frac{1}{3} X_{centered}^T X_{centered}$

After computation:

$C = \begin{bmatrix} 14/9 & -2/3 \ -2/3 & 2/3 \end{bmatrix}$

📌 Step 5: Eigenvalues

Solve:

$|C - \lambda I| = 0$

Result:

$\lambda_1 = 2$
$\lambda_2 = 2/9$

📌 Step 6: Eigenvectors

For largest eigenvalue $\lambda_1 = 2$:

$v_1 = (2, -1)$

Normalize:

$v_1 = \frac{1}{\sqrt{5}} (2, -1)$

📌 Step 7: Projection (Final Step)

Project each centered point onto $v_1$:

Projection formula:

$z = X_{centered} \cdot v_1$

🔢 Final Projections

$(1/3, -1) \rightarrow \frac{1}{\sqrt{5}} (2/3 + 1) = \frac{5/3}{\sqrt{5}}$
$(-5/3, 1) \rightarrow \frac{1}{\sqrt{5}} (-10/3 - 1) = \frac{-13/3}{\sqrt{5}}$
$(4/3, 0) \rightarrow \frac{1}{\sqrt{5}} (8/3)$

📊 Final Result (1D Data)


| **Original Point** | **Projected Value (PC1)** |
| ------------------ | ------------------------- |
| $(2,0)$            | $5/(3\sqrt{5})$           |
| $(0,2)$            | $-13/(3\sqrt{5})$         |
| $(3,1)$            | $8/(3\sqrt{5})$           |



🧠 Interpretation
Data is reduced from 2D → 1D
All variation is captured along principal direction
Second component (small eigenvalue) is ignored
🚀 One-Line Summary
PCA = center → covariance → eigenvectors → project onto top eigenvector



📊 PCA — Computing PC2 and PC3

Continuing from the same dataset:

$(2,0)$
$(0,2)$
$(3,1)$

📌 Important Fact
Data is 2D → only 2 principal components exist
So:
PC1 → exists ✅
PC2 → exists ✅
PC3 → ❌ does NOT exist

🎯 Step 1: Recall Eigenvalues

From previous computation:

$\lambda_1 = 2$ → PC1
$\lambda_2 = 2/9$ → PC2

📌 Step 2: Compute PC2 (Second Principal Component)

Solve:

$(C - \lambda_2 I)v = 0$

Result eigenvector:

$v_2 = (1, 2)$

Normalize:

$v_2 = \frac{1}{\sqrt{5}} (1, 2)$

📌 Step 3: Project Data onto PC2

Projection formula:

$z_2 = X_{centered} \cdot v_2$

🔢 Projections

Using centered points:

$(1/3, -1)$
$(-5/3, 1)$
$(4/3, 0)$
Point 1: $(1/3, -1)$

$z = \frac{1}{\sqrt{5}} \left( \frac{1}{3} - 2 \right) = \frac{-5/3}{\sqrt{5}}$

Point 2: $(-5/3, 1)$

$z = \frac{1}{\sqrt{5}} \left( -\frac{5}{3} + 2 \right) = \frac{1/3}{\sqrt{5}}$

Point 3: $(4/3, 0)$

$z = \frac{1}{\sqrt{5}} \left( \frac{4}{3} \right) = \frac{4/3}{\sqrt{5}}$

📊 Final PC2 Values

| **Point** | **PC2 Projection** |
| --------- | ------------------ |
| $(2,0)$   | $-5/(3\sqrt{5})$   |
| $(0,2)$   | $1/(3\sqrt{5})$    |
| $(3,1)$   | $4/(3\sqrt{5})$    |
