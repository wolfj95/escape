with open('animals.txt', 'r') as reader:
    with open('animalPasswords.txt', 'w') as writer:
        for animal in reader.readlines():
            animal = animal.replace(" ", "-").lower().strip()
            p = f"<p>The password is: <span class=\"password\">{animal}</span>.</p>"
            # print(p)
            writer.write(p)


