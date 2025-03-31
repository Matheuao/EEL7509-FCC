''' Escreva um programa que funcione como um mini gerenciador
     de notas para uma turma de uma disciplina. O programa 
     deve oferecer três opções ao usuário: 
     a) incluir nota,
     b) excluir nota,
     c) mostrar média da turma,
     d) sair do programa. 
     
     Se o usuário selecionar a opção a), o programa deve solicitar o
     nome do aluno e a nota, armazenando esses valores em um dicionário.
     Para opção b), o programa deve solicitar o nome do aluno e fazer a 
     exclusão do registro correspondente no dicionário. No caso da opção
     escolhida ser c), o programa deve calcular e imprimir a média da 
     turma. Finalmente, para opção d), o programa deve ser finalizado.
'''

class grade_maneger:
    
    def __init__(self):
        self.class_grades ={}
    
    def run(self):
        while(1):
            choise = input()

            if choise == "include":
                name = input()
                grade = input()

                self.include_grades(name, grade)

            elif choise == "exclude":
                name = input()
                self.exclude_grades(name)

            elif choise == "average":
                self.print_avg()

            elif choise == "exit":
                exit()

            elif choise == "print":
                self.print_class()

    def include_grades(self, name, grade):
        self.class_grades[name] = grade
    
    def exclude_grades(self, name):
        self.class_grades.pop(name);
    
    def print_avg(self):
        num_students = int()
        total = int()

        for i in self.class_grades:
            num_students +=1
            total = total + int(self.class_grades[i])
        
        print(f"média da turma:{total/num_students}")

    def print_class(self):
        for name in self.class_grades:
            print(f"{name} : {self.class_grades[name]}")

        
obj = grade_maneger()

obj.run()

    
    



