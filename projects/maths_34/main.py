import projects.maths_34.math_formulae as formulas

OPTION_FORMULA = ["Surface Area", "Area", "Volume", "Trigonometry"]
OPTION_SHAPE_3D = ["cube", "rectangular prism", "cylinder",
                             "cone", "sphere", "hemisphere"]
OPTION_SHAPE_2D = ["square", "rectangle", "trapezoid", "triangle",
                   "circle", "ellipse"]
OPTION_TRIGONOMETRY = ["cosine rule", "triangle"]


def display_items(options: list[str]) -> int:
    selected = -1
    while selected != -1:
        for i,v in enumerate(options):
            print(f"{i + 1}) {v.title()}")
        selected = int(input("Please select an option: "))
        if 1 <= selected <= len(options):
            return selected


def main():
    print("Math-a-matics\n" + "-" * 20)


if __name__ == "__main__":
    main()