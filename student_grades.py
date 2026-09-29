class Student:
    def __init__(self, nume: str, prenume: str):
        self.nume = nume
        self.prenume = prenume
        self.note = []

    def adauga_nota(self, nota: float):
        if not 1 <= nota <= 10:
            raise ValueError("Nota trebuie să fie între 1 și 10.")
        self.note.append(nota)

    def __str__(self):
        return f"{self.nume} {self.prenume}"


class Catalog:
    def __init__(self):
        self.elevi = {}

    def adauga_elev(self, nume: str, prenume: str = ""):
        if nume in self.elevi:
            raise ValueError(f"Elevul {nume} există deja în catalog.")
        self.elevi[nume] = Student(nume, prenume)

    def adauga_nota(self, nume: str, nota: float):
        if nume not in self.elevi:
            raise KeyError(f"Elevul {nume} nu există în catalog.")
        self.elevi[nume].adauga_nota(nota)


if __name__ == "__main__":
    catalog = Catalog()
    print("Adaugă note elevilor. Scrie 'exit' pentru a termina.")

    while True:
        nume = input("Numele elevului: ").strip()
        if nume.lower() == "exit":
            break

        prenume = input("Prenumele elevului: ").strip()
        if nume not in catalog.elevi:
            catalog.adauga_elev(nume, prenume)

        nota = float(input("Nota elevului: "))
        catalog.adauga_nota(nume, nota)
        print(f"Nota {nota} a fost adăugată pentru {nume} {prenume}.")
