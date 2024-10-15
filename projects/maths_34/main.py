import projects.maths_34.math_formulae as formulas


def main():
    options = ["square", "triangle"]
    selected = -1
    while selected != -1:
        for i,v in enumerate(options):
            print(f"{i + 1}) {v.title()}")
        selected = int(input("Please enter one of the options"))
        if not(1 <= selected <= len(options)):
            continue
        elif selected == 1:
            side_length = int(input("Please enter the length of one side: "))
            formulas.square_area(side_length)
        elif selected == 2:
            base_length = int(input("Enter the length of the base of the triangle: "))
            height_length = int(input("Enter the length of the height of the triangle: "))
            formulas.triangle_area(base_length, height_length)


if __name__ == "__main__":
    main()