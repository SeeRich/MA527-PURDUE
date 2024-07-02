import numpy as np
import numpy.linalg as la
import numpy.typing as npt


def build_hilbert(n: int) -> np.ndarray:
    res = np.zeros((n, n))
    for i in range(1, n+1):
        for j in range(1, n+1):
            res[i-1, j-1] = 1/(i+j-1)
    return res


if __name__ == "__main__":
    for n in [20, 200, 1000]:
        ########## Part A.1: build the system ##########
        A = build_hilbert(n)
        x_0 = np.ones((n, 1))
        b = la.matmul(A, x_0)

        ########## Part A.2: Solve the system ##########
        x = la.solve(A, b)
        # Compute the error
        error = x - x_0

        ########## Part A.3: Compute the maximum of absolute value of error ##########
        max_error = np.max(np.abs(error))
        print(f"N: {n}, Max Error: {max_error}")
