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

---

# 🎯 Given Data (2D)

Points:

- (2, 0)
- (0, 2)
- (3, 1)

---

# 📌 Step 1: Form Data Matrix

X = [(2,0), (0,2), (3,1)]

---

# 📌 Step 2: Compute Mean

μ = ((2+0+3)/3 , (0+2+1)/3)
  = (5/3, 1)

---

# 📌 Step 3: Center the Data

Subtract mean from each point:

- (2,0) → (1/3, −1)
- (0,2) → (−5/3, 1)
- (3,1) → (4/3, 0)

---

# 📌 Step 4: Covariance Matrix

C = (1/3) X_centeredᵀ X_centered

After computation:

C = [ 14/9    −2/3 ]
    [ −2/3    2/3 ]

---

# 📌 Step 5: Eigenvalues

Solve:

|C − λI| = 0

Result:

- λ₁ = 2
- λ₂ = 2/9

---

# 📌 Step 6: Eigenvectors

For largest eigenvalue λ₁ = 2:

v₁ = (2, −1)

Normalize:

v₁ = (1/√5)(2, −1)

---

# 📌 Step 7: Projection (Final Step)

Project each centered point onto v₁.

Projection formula:

z = X_centered · v₁

---

# 🔢 Final Projections

(1/3, −1)
→ (1/√5)(2/3 + 1)
→ (5/3)/√5

---

(−5/3, 1)
→ (1/√5)(−10/3 − 1)
→ (−13/3)/√5

---

(4/3, 0)
→ (1/√5)(8/3)

---

# 📊 Final Result (1D Data)

| **Original Point** | **Projected Value (PC1)** |
| ------------------ | ------------------------- |
| (2,0)              | 5/(3√5)                   |
| (0,2)              | −13/(3√5)                 |
| (3,1)              | 8/(3√5)                   |

---

# 🧠 Interpretation

- Data is reduced from 2D → 1D
- All variation is captured along principal direction
- Second component (small eigenvalue) is ignored

---

# 🚀 One-Line Summary

PCA = center → covariance → eigenvectors → project onto top eigenvector

---

# 📊 PCA — Computing PC2 and PC3

Continuing from the same dataset:

- (2,0)
- (0,2)
- (3,1)

---

# 📌 Important Fact

Data is 2D → only 2 principal components exist.

So:

- PC1 → exists ✅
- PC2 → exists ✅
- PC3 → ❌ does NOT exist

---

# 🎯 Step 1: Recall Eigenvalues

From previous computation:

- λ₁ = 2 → PC1
- λ₂ = 2/9 → PC2

---

# 📌 Step 2: Compute PC2 (Second Principal Component)

Solve:

(C − λ₂I)v = 0

Result eigenvector:

v₂ = (1, 2)

Normalize:

v₂ = (1/√5)(1, 2)

---

# 📌 Step 3: Project Data onto PC2

Projection formula:

z₂ = X_centered · v₂

---

# 🔢 Projections

Using centered points:

- (1/3, −1)
- (−5/3, 1)
- (4/3, 0)

---

## Point 1: (1/3, −1)

z = (1/√5)(1/3 − 2)
  = (−5/3)/√5

---

## Point 2: (−5/3, 1)

z = (1/√5)(−5/3 + 2)
  = (1/3)/√5

---

## Point 3: (4/3, 0)

z = (1/√5)(4/3)
  = (4/3)/√5

---

# 📊 Final PC2 Values

| **Point** | **PC2 Projection** |
| --------- | ------------------ |
| (2,0)     | −5/(3√5)           |
| (0,2)     | 1/(3√5)            |
| (3,1)     | 4/(3√5)            |
