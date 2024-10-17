import math_formulae


# basic option library contaning each possibility
#stage 1
OPTION_FORMULA = ["Surface Area", "Volume", "Area", "Trigonometry"]
#stage 2
OPTION_SHAPE_3D = ["cube", "rectangular prism", "cylinder",
                             "cone", "sphere", "hemisphere"]
OPTION_SHAPE_2D = ["square", "rectangle", "trapezoid", "triangle",
                   "circle", "ellipse"]
OPTION_TRIGONOMETRY = ["cosine rule", "triangle"]
#accessiblity libraries (saves memory and speed with fast look ups)
OPTIONS = [OPTION_SHAPE_3D, OPTION_SHAPE_2D, OPTION_TRIGONOMETRY]
OPTIONS_CALLBACK = [[cube_surface_area, rectangular_prism_surface_area],
                    [],
                    [square_area, rectangle_area, trapezoid_area,
                     triangle_area, circle_area, ellipse_area],
                    [cosine_rule_side, triangle_area_trigonometric]]

def display_items(options: list[str]) -> int:
    selected = -1
    for i,v in enumerate(options):
            print(f"{i + 1}) {v.title()}")
    while not(1 <= selected <= len(options)):
        selected = int(input("Please select an option: "))

    return selected


def main():
    print("Math-a-matics\n" + "-" * 20)
    sub_section_choice = display_items(OPTION_FORMULA)
    sub_section = 0
    match sub_section_choice:
        case 1 | 2:
            sub_section = OPTIONS[0]
        case 3:
            sub_section = OPTIONS[2]
        case 4:
            sub_section = OPTIONS[3]
    


if __name__ == "__main__":
    main()
