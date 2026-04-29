📊 Singular Value Decomposition (SVD)

SVD is a powerful matrix factorization that decomposes any matrix into rotation + scaling + rotation.

🎯 Definition

For any matrix $A \in \mathbb{R}^{m \times n}$:

$A = U \Sigma V^T$

📌 Components

Matrix	Shape	Meaning
$U$	$m \times m$	Left singular vectors (output space basis)
$\Sigma$	$m \times n$	Diagonal matrix (singular values)
$V^T$	$n \times n$	Right singular vectors (input space basis)

📌 Singular Values
$\Sigma = \text{diag}(\sigma_1, \sigma_2, ..., \sigma_r)$
$\sigma_1 \ge \sigma_2 \ge \dots \ge 0$

🧠 Intuition

SVD breaks transformation into 3 steps:

Rotate input space → $V^T$
Scale along axes → $\Sigma$
Rotate to output space → $U$
🔄 Geometric Interpretation
$V$ defines directions in input space
$\Sigma$ stretches/shrinks along those directions
$U$ maps them to output space

📌 Relation to Eigen Decomposition

$A^T A = V \Lambda V^T$
$A A^T = U \Lambda U^T$

Where:

$\Lambda = \Sigma^2$
Eigenvalues = squared singular values
📊 Connection to PCA
Concept	PCA	SVD
Input	Covariance matrix	Data matrix
Output	Eigenvectors	Singular vectors
Use	Dimensionality reduction	Same (more stable)
📌 PCA via SVD

Given centered data $X$:

$X = U \Sigma V^T$

Principal components = columns of $V$
Variance = $\Sigma^2 / n$
🔢 Small Example

Let:

$A = \begin{bmatrix} 3 & 1 \ 1 & 3 \end{bmatrix}$

SVD gives:

$U$ → rotation
$\Sigma$ → scaling
$V$ → rotation

📌 Applications
Dimensionality reduction (PCA)
Image compression
Noise reduction
Recommendation systems
Latent semantic analysis (NLP)

🚀 Key Properties
Property	Value
Works for any matrix	Yes
Orthogonal matrices	$U^T U = I$, $V^T V = I$
Singular values	Non-negative
🧠 Intuition Summary
SVD = rotate → scale → rotate
It reveals the intrinsic structure of data
🚀 One-Line Summary
SVD decomposes a matrix into $A = U \Sigma V^T$, representing rotation, scaling, and rotation again.
