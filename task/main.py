from task.rectangle import Rectangle


def main():
    # TODO: 1. Prepare example Rectangle data
    rect1 = Rectangle(0, 0, 10, 10)
    rect2 = Rectangle(5, 5, 15, 15)  # intersect with rect1
    rect3 = Rectangle(10, 10, 20, 20)  # shares edges with rect1, but no intersection
    rect4 = Rectangle(1, 1, 9, 9)  # inside rect1
    rect5 = Rectangle(11, 11, 21, 21)  # outside rect1, no intersection

    # TODO: 2. Verify implemented methods
    print("Is rect1 contains rect2?")
    print(rect1.contains(rect2))

    print("Is rect2 contains rect1?")
    print(rect2.contains(rect1))

    print("Is rect1 contains rect3?")
    print(rect1.contains(rect3))

    print("Is rect1 contains rect4?")
    print(rect1.contains(rect4))

    print("Is rect1 contains rect5?")
    print(rect1.contains(rect5))

    print("Is rect1 intersect with rect2?")
    print(rect1.intersect(rect2))

    print("Is rect2 intersect with rect1?")
    print(rect2.intersect(rect1))

    print("Is rect1 intersect with rect3?")
    print(rect1.intersect(rect3))

    print("Is rect1 intersect with rect4?")
    print(rect1.intersect(rect4))

    print("Is rect1 intersect with rect5?")
    print(rect1.intersect(rect5))


if __name__ == "__main__":
    main()
