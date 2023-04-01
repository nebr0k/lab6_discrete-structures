def read_graph(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split())
        edges = []
        for i in range(m):
            u, v = map(int, file.readline().split())
            edges.append((u, v))
    return n, m, edges


def adjacency_matrix(n, edges):
    adj_matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj_matrix[u - 1][v - 1] = 1
    return adj_matrix


def incidence_matrix(n, m, edges):
    inc_matrix = [[0] * m for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        inc_matrix[u - 1][i] = 1
        inc_matrix[v - 1][i] = -1
    return inc_matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    input_filename = input("Enter input file name: ")
    n, m, edges = read_graph(input_filename)

    print("Adjacency matrix:")
    adj_matrix = adjacency_matrix(n, edges)
    print_matrix(adj_matrix)

    print("Incidence matrix:")
    inc_matrix = incidence_matrix(n, m, edges)
    print_matrix(inc_matrix)

    output_option = input("Do you want to output the matrices to a file? (Y/N) ")
    if output_option.upper() == "Y":
        output_filename = input("Enter output file name: ")
        write_matrix_to_file(adj_matrix, output_filename + "_adj.txt")
        write_matrix_to_file(inc_matrix, output_filename + "_inc.txt")
        print("Matrices written to files: {}_adj.txt and {}_inc.txt".format(output_filename, output_filename))




