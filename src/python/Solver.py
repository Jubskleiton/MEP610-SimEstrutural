import numpy as np

def solver():
    #Matriz de Rigidez Global para cada Elemento
    if el_type == "Mola" or el_type == "Barra":
        ke = k*np.array([[ m*m, m*n, -m*m, -m*n, 0, 0],
                         [ m*n, n*n, -m*n, -n*n, 0, 0],
                         [-m*m, -m*n, m*m,  m*n, 0, 0],
                         [-m*n, -n*n, m*n, n*n,  0, 0],
                         [0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0,]])

    elif el_type == "Viga":
        ke = np.array([[phi*n*n, -phi*m*n, lmbda*n, -phi*n*n, phi*m*n, -lmbda*n],
                       [-phi*m*n, phi*m*m, lmbda*m, phi*m*n, -phi*m*m, lmbda*m],
                       [-lmbda*n, lmbda*m, 2*rho, lmbda*n, -lmbda*m, rho]
                       [-phi*n*n, phi*m*n, lmbda*n, phi*n*n, -phi*m*n, lmbda*n],
                       [phi*m*n, -phi*m*m, -lmbda*n, -phi*m*n, phi*m*m, -lmbda*m],
                       [-lmbda*n, lmbda*m, rho, lmbda*n, -lmbda*m, 2*rho]])

    elif el_type == "Portico":
        ke = (ae/l) *np.array([[ m*m, m*n, 0, -m*m, -m*n, 0],
                        [ m*n, n*n, 0, -m*n, -n*n, 0],
                        [0, 0, 0, 0, 0, 0],
                        [-m*m, -m*n, 0, m*m, m*n, 0],
                        [-m*n, -n*n, 0, m*n, n*n, 0],
                        [0, 0, 0, 0, 0, 0,]])

        ke = ke + np.array([[phi*n*n, -phi*m*n, lmbda*n, -phi*n*n, phi*m*n, -lmbda*n],
                       [-phi*m*n, phi*m*m, lmbda*m, phi*m*n, -phi*m*m, lmbda*m],
                       [-lmbda*n, lmbda*m, 2*rho, lmbda*n, -lmbda*m, rho]
                       [-phi*n*n, phi*m*n, lmbda*n, phi*n*n, -phi*m*n, lmbda*n],
                       [phi*m*n, -phi*m*m, -lmbda*n, -phi*m*n, phi*m*m, -lmbda*m],
                       [-lmbda*n, lmbda*m, rho, lmbda*n, -lmbda*m, 2*rho]])

    #Matriz Transformacao apenas para o calculo das forcas
    if el_type == "Viga" or el_type == "Portico":

        T = [[m, n, 0, 0, 0, 0],
            [-n, m, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0,  0, 0, m, n, 0],
            [0,  0, 0, -n, m, 0],
            [0,  0, 0,  0,  0, 1]]

    elif el_type == "Barra" or el_type == "Mola":

        T = [[m, n, 0, 0, 0, 0],
             [-n, m, 0, 0, 0, 0],
             [0, 0, m, n, 0, 0],
             [0, 0, -n, m, 0 ,0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    # Matriz de Rigidez Global
    for el in range(1, nEL + 1):
        if el_type == "Viga" or el_type == "Portico":
            Kg[LM[:, el - 1], LM[:, el - 1]] += Ke[:, :, el - 1]

        elif el_type == "Barra" or el_type == "Mola":
            Kg[LM[0:4, el - 1], LM[0:4, el - 1]] += Ke[0:4, 0:4, el - 1]

    #Solução do deslocamento (X)
    X(Grau de liberdade desconhecidos) = (Kg(Gl desconhecidos até Gl desconhecidos)/Forcas) - Kg(Gl desconhecidos até Gl desconhecidos)*X(Gl conhecidos)

    pass