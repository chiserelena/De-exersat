from student_grades import Catalog


def main():
    catalog = Catalog()
    catalog.adauga_elev("Ana")
    catalog.adauga_nota("Ana", 9)
    catalog.adauga_nota("Ana", 10)
    print(catalog.elevi["Ana"].note)


if __name__ == "__main__":
    main()
