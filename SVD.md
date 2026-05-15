# 📊 Singular Value Decomposition (SVD)

SVD is a powerful matrix factorization that decomposes any matrix into rotation + scaling + rotation.

---

# 🎯 Definition

For any matrix A ∈ ℝᵐˣⁿ:

A = UΣVᵀ

---

# 📌 Components

| Matrix | Shape | Meaning |
|---|---|---|
| U | m × m | Left singular vectors (output space basis) |
| Σ | m × n | Diagonal matrix (singular values) |
| Vᵀ | n × n | Right singular vectors (input space basis) |

---

# 📌 Singular Values

Σ = diag(σ₁, σ₂, ..., σᵣ)

σ₁ ≥ σ₂ ≥ ... ≥ 0

---

# 🧠 Intuition

SVD breaks transformation into 3 steps:

1. Rotate input space → Vᵀ  
2. Scale along axes → Σ  
3. Rotate to output space → U  

---

# 🔄 Geometric Interpretation

- V defines directions in input space
- Σ stretches/shrinks along those directions
- U maps them to output space

---

# 📌 Relation to Eigen Decomposition

AᵀA = VΛVᵀ

AAᵀ = UΛUᵀ

Where:

Λ = Σ²

- Eigenvalues = squared singular values

---

# 📊 Connection to PCA

| Concept | PCA | SVD |
|---|---|---|
| Input | Covariance matrix | Data matrix |
| Output | Eigenvectors | Singular vectors |
| Use | Dimensionality reduction | Same (more stable) |

---

# 📌 PCA via SVD

Given centered data X:

X = UΣVᵀ

Principal components = columns of V

Variance = Σ² / n

---

# 🔢 Small Example

Let:

A = [ 3   1 ]
    [ 1   3 ]

SVD gives:

- U → rotation
- Σ → scaling
- V → rotation

---

# 📌 Applications

- Dimensionality reduction (PCA)
- Image compression
- Noise reduction
- Recommendation systems
- Latent semantic analysis (NLP)

---

# 🚀 Key Properties

| Property | Value |
|---|---|
| Works for any matrix | Yes |
| Orthogonal matrices | UᵀU = I, VᵀV = I |
| Singular values | Non-negative |

---

# 🧠 Intuition Summary

SVD = rotate → scale → rotate

It reveals the intrinsic structure of data.

---

# 🚀 One-Line Summary

SVD decomposes a matrix into:

A = UΣVᵀ

representing rotation, scaling, and rotation again.
