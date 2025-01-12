# linear system solve
def solve(A, b):
    X = deepcopy(A)
    sol = deepcopy(b)
    n = len(X)
    for i in range(n):
        print('---- i번째 실행 시작! ----')
        x_row = X[i]
        y_val = sol[i]
        if x_row[i] != 0:
            tmp = 1 / x_row[i]
        else:
            tmp = 0
        x_row = [element * tmp for element in x_row]
        y_val = y_val * tmp
        X[i] = x_row
        sol[i] = y_val
        print(x_row)
        print(y_val)
        print('---- 행 나누기 완료 ----')
        for j in range(n):
            if i == j:
                continue
            print('---- j번째 실행 시작 ----')
            x_next = X[j]
            y_next = sol[j]
            x_tmp = [element * -x_next[i] for element in x_row]
            y_tmp = y_val * (-x_next[i])
            for k in range(len(x_row)):
                x_next[k] += x_tmp[k]
            y_next += y_tmp
            X[j] = x_next
            sol[j] = y_next
            print(X)
            print(sol)
            print('---- j번째 실행 종료 ----')
        print('---- i번째 실행 완료 ----')
    return sol


# zero matrix
def zero_mat(n, p):
    Z = []
    for i in range(n):
        row = []
        for j in range(p):
            row.append(0)
        Z.append(row)
    return Z


# deepcopy
def deepcopy(A):
    if type(A[0]) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n, p)
        for i in range(n):
            for j in range(p):
                res[i][j] = A[i][j]
        return res
    else:
        n = len(A)
        res = []
        for i in range(n):
            res.append(A[i])
        return res


X = [[3, 1, 2], [2, 6, -1], [4, 0, -1]]
y = [5, 1, 3]
sol = solve(X, y)