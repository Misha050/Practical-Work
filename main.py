import math

class Classifier:
    def __init__(self, data):
        self.data = data

    def classify(self, unknown, k):
        distances = []
        for class_name, points in self.data.items():
            for point in points:
                distance = math.sqrt((point[0] - unknown[0])**2 + (point[1] - unknown[1])**2)
                distances.append((distance, class_name))
        distances.sort()
        classes = [class_name for _, class_name in distances[:k]]
        return max(classes, key=classes.count)

def main():
    data = {}
    while True:
        x = float(input("Введите координаты точки по значению x: "))
        y = float(input("Введите координаты точки по значению y: "))
        class_name = input("Введите класс объекта: ")
        if class_name not in data:
            data[class_name] = []
        data[class_name].append((x, y))
        more = input("Хотите ли Вы еще добавить точку? Если «да», то введите «y», если нет, то нажмите любую другую клавишу. ")
        if more.lower() != 'y':
            break
    unknown_x = float(input("Введите координаты точки неизвестного класса по значению x: "))
    unknown_y = float(input("Введите координаты точки неизвестного класса по значению y: "))
    k = int(input("Задайте величину радиуса ближайших соседей: "))
    classifier = Classifier(data)
    class_name = classifier.classify((unknown_x, unknown_y), k)
    print(f"Точка ({unknown_x}, {unknown_y}) принадлежит классу {class_name}")

if __name__ == "__main__":
    main()
