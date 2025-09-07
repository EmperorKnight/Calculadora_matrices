from fractions import Fraction
import menu
import copy

def parse_number(s: str) -> Fraction:
    s = s.strip()
    if s == "":
        raise ValueError("Entrada vacía")
    try:
        return Fraction(s)
    except Exception:
        return Fraction(float(s))

def meter_valores():
    while True:
        try:
            m = int(input("Número de filas: ").strip())
            if m <= 0:
                print("El número de filas debe ser mayor que 0.")
                continue
            break
        except Exception:
            print("Entrada inválida (ingresa un entero).")
    while True:
        try:
            n = int(input("Número de columnas: ").strip())
            if n <= 0:
                print("El número de columnas debe ser mayor que 0.")
                continue
            break
        except Exception:
            print("Entrada inválida (ingresa un entero).")

    print(f"\nIngrese matriz aumentada, separados por espacios.")
    A = []
    for i in range(m):
        while True:
            row_input = input(f"Fila {i+1}: ").strip().split()
            if len(row_input) != n + 1:
                print(f"Necesitas ingresar {n+1} valores (los {n} coeficientes y el término independiente). Intenta de nuevo.")
                continue
            try:
                row = [parse_number(x) for x in row_input]
                A.append(row)
                break
            except Exception as e:
                print("Entrada inválida:", e)
    return A, m, n

def format_frac(x: Fraction) -> str:
    if isinstance(x, Fraction):
        if x.denominator == 1:
            return str(x.numerator)
        else:
            return f"{x.numerator}/{x.denominator}"
    else:
        return str(x)

def print_matrix(M):
    rows = len(M)
    cols = len(M[0])
    col_widths = [0] * cols
    for j in range(cols):
        col_widths[j] = max(len(format_frac(M[i][j])) for i in range(rows))
    for i in range(rows):
        row_str = ""
        for j in range(cols):
            cell = format_frac(M[i][j]).rjust(col_widths[j])
            if j == cols - 1:
                row_str += " | " + cell
            else:
                row_str += " " + cell
        print(row_str)

def gaussian_elimination_steps(A_aug):
    m = len(A_aug)
    n = len(A_aug[0]) - 1
    A = copy.deepcopy(A_aug)
    A_orig = [row[:-1] for row in copy.deepcopy(A_aug)]
    row_map = list(range(m))
    pivots = []

    print('\nMatriz aumentada inicial:')
    print_matrix(A)

    current_row = 0
    for col in range(n):
        pivot_row = None
        max_val = Fraction(0)
        for r in range(current_row, m):
            if abs(A[r][col]) > max_val:
                max_val = abs(A[r][col])
                pivot_row = r
        if pivot_row is None or A[pivot_row][col] == 0:
            continue
        if pivot_row != current_row:
            A[current_row], A[pivot_row] = A[pivot_row], A[current_row]
            row_map[current_row], row_map[pivot_row] = row_map[pivot_row], row_map[current_row]
            print(f"\nIntercambiar R{current_row+1} <-> R{pivot_row+1}")
            print_matrix(A)

        pivot_val_current = A[current_row][col]
        orig_row_idx = row_map[current_row]
        orig_pivot_val = A_orig[orig_row_idx][col]
        pivots.append({
            'row': current_row,
            'col': col,
            'pivot_current': pivot_val_current,
            'orig_row': orig_row_idx,
            'orig_pivot_val': orig_pivot_val,
        })

        for r in range(current_row + 1, m):
            if A[r][col] != 0:
                factor = A[r][col] / A[current_row][col]
                A[r] = [A[r][c] - factor * A[current_row][c] for c in range(n + 1)]
                print(f"\nR{r+1} <- R{r+1} - ({format_frac(factor)}) * R{current_row+1}")
                print_matrix(A)

        current_row += 1
        if current_row == m:
            break

    for r in range(m):
        if all(A[r][c] == 0 for c in range(n)) and A[r][n] != 0:
            print("\nSistema inconsistente: existe una fila 0 ... 0 | b != 0. No hay solución.")
            print('\nMatriz tras eliminación:')
            print_matrix(A)
            return {
                'type': 'inconsistent',
                'pivots': pivots,
                'A': A,
            }

    print("\nComenzando reducción hacia la forma escalonada reducida (RREF):")
    for p in reversed(pivots):
        r = p['row']
        c = p['col']
        if A[r][c] != 1:
            factor = A[r][c]
            A[r] = [val / factor for val in A[r]]
            print(f"\nR{r+1} <- R{r+1} / ({format_frac(factor)})")
            print_matrix(A)
        for i in range(0, r):
            if A[i][c] != 0:
                factor = A[i][c]
                A[i] = [A[i][j] - factor * A[r][j] for j in range(n + 1)]
                print(f"\nR{i+1} <- R{i+1} - ({format_frac(factor)}) * R{r+1}")
                print_matrix(A)

    print('\nMatriz en RREF final:')
    print_matrix(A)

    pivot_cols = [p['col'] for p in pivots]
    basic_vars = [c + 1 for c in pivot_cols]
    free_vars = [i + 1 for i in range(n) if i not in pivot_cols]

    if len(basic_vars) == 0:
        print('\nVariables básicas: No hay varibles basicas')
    else:
        print('\nVariables básicas:')
        for z in basic_vars:
            print(f"x{z}")

    if len(free_vars) == 0:
        print("Varibles libres: No hay varibles libres")
    else:
        print("Variables libres:")
        for a in free_vars:
            print(f"x{a}")

    if len(pivots) == n:
        sol = [Fraction(0) for _ in range(n)]
        for p in pivots:
            sol[p['col']] = A[p['row']][n]
        print('\nSolución única:')
        for i, val in enumerate(sol):
            print(f"x{i+1} = {format_frac(val)}")
    else:
        print('\nEl sistema tiene infinitas soluciones.')

def main():
    print("=== Resolvedor de sistemas con pasos (Eliminación Gaussiana y RREF) ===")
    A_aug, m, n = meter_valores()
    gaussian_elimination_steps(A_aug)
    input("\nPresione enter para regresar al menu principal . . . ")
    menu.main()

main()