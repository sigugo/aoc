from tools import *
from os import system


def enhance(image: list[list[str]], enhancer: str, ip: str = ".") -> list[list[str]]:
    xlen = len(image[0]) + 2
    tempimage: list[list[str]] = []
    tempimage.append(xlen * [ip])
    for xline in image:
        tempimage.append([ip] + xline + [ip])
    tempimage.append(xlen * [ip])
    image = []
    for y in range(len(tempimage)):
        outline: list[str] = []
        for x in range(len(tempimage[y])):
            # print("\nEnhancing Pixel", x, y)
            scanstring: str = ""
            for yscan in range(-1, 2):
                for xscan in range(-1, 2):
                    scanstring += (
                        "1"
                        if get_2d_matrix_value_at_x_y_safe(
                            tempimage, x + xscan, y + yscan, ip
                        )
                        == "#"
                        else "0"
                    )
            outline.append(enhancer[int(scanstring, 2)])
        image.append(outline)

    return image


def print_image(image: list[list[str]]) -> None:
    output = ""
    for xline in image:
        outline = ""
        for xpixel in xline:
            outline += xpixel
        output += outline + "\n"
    system("clear")
    print(output)


def image_from_input(input: list[str]) -> list[list[str]]:
    image: list[list[str]] = []
    for inputline in input:
        image.append(list(inputline))
    return image


def main() -> None:
    input_file = "../inputs/20/data.input"
    # input_file = "../inputs/20/data.example"
    input_data: list[str] = file_to_list(input_file)

    enhancer = input_data[0]

    image: list[list[str]] = image_from_input(input_data[2:])

    # enhance count = 1     # part 1
    enhance_count = 25  # part 2

    for _ in range(enhance_count):
        image = enhance(image, enhancer, enhancer[-1])
        print_image(image)
        image = enhance(image, enhancer, enhancer[0])
        print_image(image)

    count = 0
    for line in image:
        for c in line:
            if c == "#":
                count += 1
    print(count)


if __name__ == "__main__":
    main()
