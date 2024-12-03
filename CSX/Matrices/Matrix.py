#Name: Irhan Iftikar
#Date: November/December 2024
#Description: CSX Assignment - Matrices
#Bonuses: Determinant, Transpose, REF, Integer Power, Rank, Orthogonal Check, Dot Product, Hadamard Product, Frobenius Norm
#Bugs: No notable bugs found in program
#Sources: Several Internet Sources for Syntax (w3schools, Stack Overflow, GeeksForGeeks, etc.)

#Import sys module used if the user wants to quit the program
import sys

#Defines Matrix Class
class Matrix:
    def __init__(self):
        #Description: Function that asks user for matrix dimensions and initializes matrix row, column, and data values
        #Parameters - self
        #Returns - null
        while True:
            try:
                rows = int(input("Enter number of rows for your matrix: "))
                cols = int(input("Enter number of columns for your matrix: "))
                if rows <= 0 or cols <= 0:
                    print("Invalid input. You must enter a positive integer for both rows and columns.")
                    continue
                break
            except ValueError:
                print("Invalid input. You must enter a positive integer for both rows and columns.")
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def menu(self):
        #Description: Function that displays the menu options for the user to select
        #Parameters - self
        #Returns - null
        print('''
    Matrix Calculation Options:
    -------------------------------------------------------------
    1 - Print the Matrices
    2 - Add the Matrices
    3 - Multiply the Matrices
    4 - Multiply a Row by a Scalar
    5 - Switch Rows of Matrix
    6 - Add Scalar times Row to another Row
    7 - Reduced Row Echelon Form (RREF) of Matrix
    8 - Inverse of Matrix
    9 - Determinant of Matrix
    10 - Transpose of Matrix
    11 - Row Echelon Form (REF) of Matrix
    12 - Integer Powers of Matrix
    13 - Rank of Matrix
    14 - Orthogonality Check of Matrix
    15 - Dot Product of Matrices
    16 - Hadamard Product of Matrices
    17 - Frobenius Norm of Matrix
    18 - Quit Program''')  

    def operate(self, matrix2):
        #Description: Function that takes user option from menu and calls on other functions within the Matrix class
        #Parameters - self, matrix2
        #Returns - various returns to the user
        choice = input("\nSelect an option from the menu (numbers 1-18): ") 
        if choice == "1":
            print("Matrix 1: ")
            self.print()
            print("Matrix 2: ")
            matrix2.print()
        elif choice == "2":
            self.plus(matrix2)
        elif choice == "3":
            self.times(matrix2)
        elif choice == "4":
            scalar = float(input("Enter a scalar value: "))
            row = int(input("Enter the row number to be multipled: "))
            matrix_number = int(input("Which matrix do you want to modify? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.scalarTimesRow(scalar, row)
        elif choice == "5":
            row1 = int(input("Enter the first row to be switched: "))
            row2 = int(input("Enter the second row to be switched: "))
            matrix_number = int(input("Which matrix do you want to modify? (1 or 2)"))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.switchRows(row1, row2)
        elif choice == "6":
            scalar = float(input("Enter a scalar value: "))
            row1 = int(input("Enter the row number to be multipled by the scalar: "))
            row2 = int(input(f"Enter the row number to be modified by the scalar times row {row1}: "))
            matrix_number = int(input("Which matrix do you want to modify? (1 or 2)"))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.linearCombRows(scalar, row1, row2)
        elif choice == "7":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            rref, valid_answer = matrix.rowreduce()
            if valid_answer == True:
                print("Reduced Row Echelon Form (RREF) of the matrix:")
                for row in rref:
                    print([round(num, 2) for num in row])
        elif choice == "8":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            rref, valid_answer = matrix.rowreduce()
            matrix.invert(rref, valid_answer)
        elif choice == "9":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            determinant = matrix.determinant()
            print(f"Determinant of Matrix: {determinant}")
        elif choice == "10":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.transpose()
        elif choice == "11":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            ref, valid_answer = matrix.REF()
            if valid_answer == True:
                print("Row Echelon Form (REF) of the matrix:")
                for row in ref:
                    print([round(num, 2) for num in row])
        elif choice == "12":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            integer = int(input("To what integer power n should the matrix be raised up to? "))
            matrix.integer_power(integer)
        elif choice == "13":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            ref, valid_answer = matrix.REF()
            matrix.rank(ref, valid_answer)
        elif choice == "14":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.orthogonal_check()
        elif choice == "15":
            self.dot_product(matrix2)
        elif choice == "16":
            self.hadamard_product(matrix2)
        elif choice == "17":
            matrix_number = int(input("Which matrix do you want to view? (1 or 2) "))
            if matrix_number == 1:
                matrix = self
            elif matrix_number == 2:
                matrix = matrix2
            else:
                print("Invalid matrix entry.")
                return None
            matrix.frobenius_norm()
        elif choice == "18":
            sys.exit(0)
        else:
            print("Option choice not valid, try again.")

    def initialize_matrix(self):
        #Description: Function that has the user create the matrix by entering values at each position
        #Parameters - self
        #Returns - null
        for i in range(self.rows):
            for j in range(self.cols):
                while True:
                    try:
                        self.data[i][j] = float(input(f"Enter a value at row {i+1}, column {j+1}: "))
                        break
                    except ValueError:
                        print("User didn't enter a numerical value. Try again.")
    
    def print(self):
        #Description: Function that prints the matrix to the user
        #Parameters - self
        #Returns - null
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j], end=" ")
            print()
        print("\n")
 
    def plus(self, matrix2):
        #Description: Function that finds the sum of two matrices
        #Parameters - self, matrix2
        #Returns - None if matrices can't be added
        if self.rows != matrix2.rows or self.cols != matrix2.cols:
            print("Matrices cannot be added as they have different dimensions.\n")
            return None
        result = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] + matrix2.data[i][j]
        print("Sum of Matrices: ")
        for row in result:
            print(row)
        print("\n")

    def times(self, matrix2):
        #Description: Function that finds the product of two matrices
        #Parameters - self, matrix2
        #Returns - None if matrices can't be multiplied
        if self.cols != matrix2.rows:
            print("Matrices cannot be multipled as columns in the first matrix is not equal to rows in the second matrix.")
            return None
        result = [[0 for _ in range(self.rows)] for _ in range(matrix2.cols)]
        print("Product of Matrices: ")
        for i in range(self.rows):
            for j in range(matrix2.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * matrix2.data[k][j]
                print(result[i][j], end = " ")
            print()
        print("\n")

    def scalarTimesRow(self, scalar, row):
        #Description: Function that multiples a row in the matrix by a scalar value
        #Parameters - self, scalar, row
        #Returns - None if the entered row doesn't exist
        row -= 1
        if 0 <= row < self.rows:
            for col in range(self.cols):
                self.data[row][col] *= scalar
        else:
            print("The entered row doesn't exist in the matrix.")
            return None
        print(f"Matrix result of scalar value {scalar} times row {row + 1}:")
        self.print()
        print("\n")

    def switchRows(self, firstrow, secondrow):
        #Description: Function that switches two rows in a matrix
        #Parameters - self, firstrow, secondrow
        #Returns - None if the entered row doesn't exist
        firstrow -= 1
        secondrow -=1
        if 0 <= firstrow < self.rows and 0 <= secondrow < self.rows:
            self.data[firstrow], self.data[secondrow] = self.data[secondrow], self.data[firstrow]
            print(f"Matrix result of switching rows {firstrow + 1} and {secondrow + 1}:")
            self.print()
        else:
            print("The entered row(s) don't exist in the matrix.")
        print("\n")
    
    def linearCombRows(self, scalar, firstrow, secondrow):
        #Description: Function that multiples a row by a scalar and adds it to another row
        #Parameters - self, scalar, firstrow, secondrow
        #Returns - None if the entered row doesn't exist
        firstrow -= 1
        secondrow -= 1
        if 0 <= firstrow < self.rows and 0 <= secondrow < self.rows:
            for i in range(self.cols):
                self.data[secondrow][i] += scalar * self.data[firstrow][i]
            print(f"Matrix result of multiplying row {firstrow + 1} by scalar {scalar} and adding to row {secondrow + 1}:")
            self.print()
        else:
            print("The entered row(s) don't exist in the matrix.")
        print("\n")
        
    def rowreduce(self):
        #Description: Function that displays the Reduced Row Echelon Form (RREF) of a matrix
        #Parameters - self
        #Returns - RREF of matrix, True/False Boolean if there is a valid RREF

        #On TI-84 Calculator, RREF of any matrix where rows > columns returned an Invalid Dimension Error message
        if self.rows > self.cols:
            print("Error: Invalid Dimension. RREF cannot be found.")
            return None, False
        #Creates a copy of the inputted matrix that will be modified to be the RREF of the original matrix
        rows = self.rows
        cols = self.cols
        rref = [row[:] for row in self.data]

        #Starts with column index 0 and iterates through each row
        start_index = 0 
        for col in range(cols):
            proper_index = False
            for row in range(start_index, rows):
                #Finds the first non-zero element and swaps it to be the first row
                if abs(rref[row][col]) > 1e-10:
                    proper_index = True
                    if row != start_index:
                        rref[row], rref[start_index] = rref[start_index], rref[row]
                    break
            #Iterates to next column if pivot isn't found
            if not proper_index:
                continue
            #Divides the row to modify by the largest absolute element value to make the first element equal to 1
            element = rref[start_index][col]
            for j in range(cols):
                rref[start_index][j] /= element
            #Subtracts multiples of the row from other rows to make all other elements in row equal to 0
            for row in range(rows):
                if row != start_index:
                    factor = rref[row][col]
                    for j in range(cols):
                        rref[row][j] -= factor * rref[start_index][j]
            #Continues to next row
            start_index += 1
            if start_index == rows:
                break

        #Fixes rounding errors - ensures that very small decimal numbers are essentially set to be 0.0
        for row in range(rows):
            for col in range(cols):
                if abs(rref[row][col]) < 1e-10:
                    rref[row][col] = 0.0
        return rref, True
    
    def invert(self, rref, valid_answer):
        #Description: Function that calculates and displays the inverse of a matrix
        #Parameters - self, rref, valid_answer
        #Returns - None if the inverse of matrix doesn't exist

        #Checks that entered matrix is a square matrix
        if self.rows != self.cols or valid_answer == False:
            print("Inverse of matrix does not exist, as only square matrices can be inverted.")
            return None
        rows = self.rows
        cols = self.cols
        #Checks that RREF of the matrix is the identity matrix
        for i in range(rows):
            for j in range(cols):
                if (i == j and abs(rref[i][j] - 1) > 1e-10) or (i != j and abs(rref[i][j]) > 1e-10):
                    print("Inverse of matrix does not exist, as RREF of matrix is not the identity matrix.")
                    return None
        
        #Calculates the inverse of the matrix, starts by creating an augmented matrix
        augmented_matrix = [row[:] + [1 if i == j else 0 for j in range(cols)] for i, row in enumerate(self.data)]
        #Row reduction to transform the left side of augmented matrix to the identity matrix
        start_index = 0
        for row in range(rows):
            if start_index >= cols:
                break
            row_to_modify = row
            #Finds a row with a non-zero element in the current column
            while abs(augmented_matrix[row_to_modify][start_index]) < 1e-10:
                row_to_modify += 1
                if row_to_modify == rows:
                    row_to_modify = row
                    start_index += 1
                    if start_index == cols:
                        break
            if start_index == cols:
                break
            #Swaps rows to bring the largest element to the current position
            if row_to_modify != row:
                augmented_matrix[row], augmented_matrix[row_to_modify] = augmented_matrix[row_to_modify], augmented_matrix[row]
            #Makes the current element of the position 1
            element = augmented_matrix[row][start_index]
            if abs(element) > 1e-10:
                for j in range(2 * cols):
                    augmented_matrix[row][j] /= element
            #Eliminates values in current column to fit lower triangluar form
            for i in range(rows):
                if i != row:
                    factor = augmented_matrix[i][start_index]
                    for j in range(2 * cols):
                        augmented_matrix[i][j] -= factor * augmented_matrix[row][j]
            start_index += 1

        #Takes and prints only the right-hand side of the augmented matrix, which is the inverse
        inverse_matrix = [row[cols:] for row in augmented_matrix]
        print("Inverse of matrix:")
        for row in inverse_matrix:
            print([round(num, 2) for num in row])

    def determinant(self):
        #Description: Function that finds the determinant of a matrix
        #Parameters - self
        #Returns - Determinant
        if self.rows != self.cols:
            print("Determinant does not exist as the entered matrix is not a square matrix.")
            return None
        dimension = self.rows
        if dimension == 1:
            determinant = self.data[0][0]
            return determinant
        elif dimension == 2: 
            determinant = self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
            return determinant
        else:
            determinant = 0
            for col in range(dimension):
                #Below method uses Laplace Expansion to recursively find the determinant of a matrix with dimensions > 2x2
                submatrix = [[self.data[i][j] for j in range(dimension) if j != col] for i in range (1, dimension)]
                #Bypasses the __init__ function while still creating new object of class Matrix
                minor = Matrix.__new__(Matrix)
                minor.rows = dimension - 1
                minor.cols = dimension - 1
                minor.data = submatrix
                cofactor = ((-1) ** col) * self.data[0][col] * minor.determinant()
                determinant += cofactor
            return determinant

    def transpose(self):
        #Description: Function that displays the transpose of a matrix
        #Parameters - self
        #Returns - null
        transpose = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        print("Transpose of Matrix:")
        for row in transpose:
            print(row)

    def REF(self):
        #Description: Function that displays the Row Echelon Form (REF) of a matrix
        #Parameters - self
        #Returns - REF of matrix, True/False Boolean that represents if the REF was found

        #On TI-84 Calculator, REF of any matrix where rows > columns returned an Invalid Dimension Error message
        if self.rows > self.cols:
            print("Error: Invalid Dimension. REF cannot be found.")
            return None, False
        #Creates a copy of the inputted matrix that will be modified to be the REF of the original matrix
        rows = self.rows
        cols = self.cols
        ref = [row[:] for row in self.data]
    
        #Starts with column index 0 and iterates through each row
        start_index = 0 
        for row in range(rows):
            if start_index >= cols:
                break
            row_to_modify = row
            #Finds a row with a non-zero element in the current column by going through each row
            while abs(ref[row_to_modify][start_index]) < 1e-10:   
                row_to_modify += 1
                if row_to_modify == rows:
                    row_to_modify = row
                    start_index += 1    
                    if start_index == cols:
                        break
            if start_index == cols:
                break
            #Swaps the current row with the row to modify to bring the largest element value to the top
            if row_to_modify != row:
                ref[row], ref[row_to_modify] = ref[row_to_modify], ref[row]
            #Divides the row to modify by the largest absolute element value to make the first element equal to 1
            element = ref[row][start_index]
            #Avoid division by 0
            if abs(element) > 1e-10:
                for j in range(cols):
                    ref[row][j] /= element
            #Makes all rows below the current row have 0 (lower triangular form)
            for i in range(row + 1, rows):
                factor = ref[i][start_index]
                if abs(factor) > 1e-10:  # Only eliminate if the factor is not zero
                    for j in range(cols):
                        ref[i][j] -= factor * ref[row][j]
            #Iterates to the next index value
            start_index += 1
        #Eliminates any non-zero elements after transformation to follow lower triangular form
        for i in range(rows):
            for j in range(cols):
                if abs(ref[i][j]) < 1e-10:
                    ref[i][j] = 0.0
        return ref, True
    
    def integer_power(self, n):
        #Description: Function that calculates and displays the results of a matrix raised up to the integer power n
        #Parameters - self, n
        #Returns - Matrix raised to integer power n
        if self.rows != self.cols:
            print("Matrix power does not exist as the entered matrix is not a square matrix.")
            return None
        if n < 0:
            print("Matrix cannot be raised to a negative power.")
            return None
        #Any square matrix raised to power of 0 is the Identity Matrix of same dimensions of original matrix
        if n == 0:
            identity_matrix = Matrix.__new__(Matrix)
            identity_matrix.rows = self.rows
            identity_matrix.cols = self.cols
            identity_matrix.data = [[1 if i == j else 0 for j in range(self.cols)] for i in range(self.rows)]
            print("Matrix raised to power 0 (Identity Matrix):")
            identity_matrix.print()
            return identity_matrix
        if n == 1:
            print("Matrix raised to power 1:")
            self.print()
            return self
        #Uses recursive case that matrix A^n = A * A^(n - 1) and prints matrix power up to the integer n
        partial_answer = self.integer_power(n-1)
        answer = Matrix.__new__(Matrix)
        answer.rows = self.rows
        answer.cols = self.cols
        answer.data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(self.cols):
                    answer.data[i][j] += self.data[i][k] * partial_answer.data[k][j]
        print(f"Matrix raised to the power {n}:")
        answer.print()
        return answer

    def rank(self, ref, valid_answer):
        #Description: Function that calculates and displays the rank of a matrix
        #Parameters - self, ref, valid_answer
        #Returns - Rank of Matrix
        if valid_answer == True:
            rank = 0
            for row in ref:
                if any(abs(x) > 1e-10 for x in row):
                    rank +=1
            print(f"Rank of matrix: {rank}")
            return rank
        #For simplicity sake, assumes rank of matrix does not exist for row > columns as REF cannot be found on TI-84 Calculator
        print("Rank of the matrix does not exist as REF cannot be found.")

    def orthogonal_check(self):
        #Description: Function that checks if a matrix is orthogonal
        #Parameters - self
        #Returns - True/False boolean for if the matrix is orthogonal
        if self.rows != self.cols:
            print("Matrix is not a square matrix so it cannot be orthogonal.")
            return False
        #Creates the transpose of the matrix A
        transpose = Matrix.__new__(Matrix)
        transpose.rows = self.cols
        transpose.cols = self.rows
        transpose.data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        #Multiplies transpose A^T by matrix A
        product = Matrix.__new__(Matrix)
        product.rows = self.rows
        product.cols = self.cols
        product.data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(self.cols):
                    product.data[i][j] += transpose.data[i][k] * self.data[k][j]
        #Checks if the product of matrix A times transpose A^T is the Identity Matrix
        #1e-10 expression is a Tolerance Value that helps avoid rounding errors in program
        is_orthogonal = True
        for i in range(self.rows):
            for j in range(self.cols):
                if (i == j and abs(product.data[i][j] - 1) > 1e-10) or \
                   (i != j and abs(product.data[i][j]) > 1e-10):
                    is_orthogonal = False
                    break
        if is_orthogonal:
            print("Matrix is orthogonal.")
            return is_orthogonal
        else:
            print("Matrix is not orthogonal.")
            return is_orthogonal

    def dot_product(self, matrix2):
        #Description: Function that calculates and displays the dot product of two matrices
        #Parameters - self, matrix2
        #Returns - Dot Product of the two matrices
        if self.cols != matrix2.cols or self.rows != matrix2.rows:
            print("Dot Product cannot be calculated as the matrices do not have the same dimensions.")
            return None
        dot_product = 0
        for i in range(self.rows):
            for j in range(self.cols):
                dot_product += self.data[i][j] * matrix2.data[i][j]
        print(f"Dot Product: {dot_product}")

    def hadamard_product(self, matrix2):
        #Description: Function that calculates and displays the Hadamard product of two matrices
        #Parameters - self, matrix2
        #Returns - Hadamard Product of the two matrices
        if self.rows != matrix2.rows or self.cols != matrix2.cols:
            print("Hadamard Product cannot be calculated as the matrices do not have the same dimensions.")
            return None
        hadamard_product = [[self.data[i][j] * matrix2.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        print("Hadamard Product:")
        for row in hadamard_product:
            print(row)

    def frobenius_norm(self):
        #Description: Function that calculates and displays the Frobenius Norm of a matrix
        #Parameters - self
        #Returns - Frobenius Norm of the matrix
        frobenius_norm = 0
        for i in range(self.rows):
            for j in range(self.cols):
                frobenius_norm += self.data[i][j] ** 2
        frobenius_norm = frobenius_norm ** 0.5
        print(f"Frobenius Norm: {frobenius_norm}")
