import cmath
import sys


def solve_quadratic(a, b, c):
    """Solve quadratic equation ax^2 + bx + c = 0 analytically."""
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero for a quadratic equation.")
    discriminant = b ** 2 - 4 * a * c
    sqrt_discriminant = cmath.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return root1, root2


def verify_roots(a, b, c, roots, tol=1e-9):
    """Verify that each root satisfies the quadratic equation."""
    for r in roots:
        if abs(a * r ** 2 + b * r + c) > tol:
def verify_roots(a, b, c, roots, tol=1e-9, verbose=False):
    """Verify that each root satisfies the quadratic equation.

    Parameters
    ----------
    a, b, c : float
        Coefficients of the quadratic equation ``ax^2 + bx + c = 0``.
    roots : iterable of complex
        Roots obtained from :func:`solve_quadratic`.
    tol : float, optional
        Tolerance for considering a root valid.
    verbose : bool, optional
        If True, print the residual for each root.
    """
    for idx, r in enumerate(roots, start=1):
        residual = a * r ** 2 + b * r + c
        if verbose:
            print(f"Root {idx} check: {residual}")
        if abs(residual) > tol:
            return False
    return True


def main(args):
    if len(args) != 3:
        print("Usage: python solve_quadratic.py a b c")
        return 1
    a, b, c = map(float, args)
    roots = solve_quadratic(a, b, c)
    print("Roots:", roots)
    print("Verification:", verify_roots(a, b, c, roots))
    verification = verify_roots(a, b, c, roots, verbose=True)
    print("Verification:", verification)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))