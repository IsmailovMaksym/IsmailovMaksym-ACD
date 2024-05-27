class Footwear:
    def __init__(self, brand, type, color, size, category):
        self.brand = brand
        self.type = type
        self.color = color
        self.size = size
        self.category = category
        self.season = self.determine_season()

    def determine_season(self):
        # Define type-season relationships
        summer_only = ['Сандалії', 'Босоніжки', 'Шльопанці']
        all_but_summer = ['Черевики', 'Чоботи']
        all_but_winter = ['Кеди', 'Мокасини', 'Туфлі']
        all_seasons = ['Кросівки', 'Інші']

        # Define category constraints
        category_constraints = {
            'Босоніжки': ['Жіноча', 'Дитяча'],
            'Сандалії': ['Чоловіча', 'Дитяча']
        }

        # Check for invalid type/category combinations
        if self.type in category_constraints and self.category not in category_constraints[self.type]:
            return None

        # Determine the season based on type
        if self.type in summer_only:
            return 'Літній'
        elif self.type in all_but_summer:
            return 'Весняний, Демісезонний, Зимовий, Осінній'
        elif self.type in all_but_winter:
            return 'Весняний, Демісезонний, Осінній'
        elif self.type in all_seasons:
            return 'Весняний, Демісезонний, Зимовий, Осінній, Літній'
        else:
            return None

    def availability_message(self):
        if self.season:
            return f"{self.type} від {self.brand} в розмірі {self.size} доступні для сезону {self.season}"
        else:
            return f"Нажаль {self.type} бренду {self.brand} немає в наявності"


# Example usage:
footwear = Footwear(brand="Nike", type="Сандалії", color="Чорний", size="42", category="Чоловіча")
print(footwear.availability_message())

footwear2 = Footwear(brand="Adidas", type="Босоніжки", color="Білий", size="38", category="Чоловіча")
print(footwear2.availability_message())

footwear1 = Footwear(brand="Adidas", type="Сандалії", color="Синій", size="30", category="Дитяча")
print(footwear1.availability_message())

footwear2 = Footwear(brand="Gucci", type="Босоніжки", color="Червоний", size="37", category="Жіноча")
print(footwear2.availability_message())

footwear3 = Footwear(brand="Nike", type="Кросівки", color="Чорний", size="43", category="Чоловіча")
print(footwear3.availability_message())

footwear4 = Footwear(brand="Timberland", type="Чоботи", color="Коричневий", size="39", category="Жіноча")
print(footwear4.availability_message())

footwear5 = Footwear(brand="Puma", type="Шльопанці", color="Білий", size="32", category="Дитяча")
print(footwear5.availability_message())

footwear6 = Footwear(brand="Lacoste", type="Туфлі", color="Чорний", size="42", category="Чоловіча")
print(footwear6.availability_message())

footwear7 = Footwear(brand="Prada", type="Босоніжки", color="Синій", size="44", category="Чоловіча")
print(footwear7.availability_message())

footwear8 = Footwear(brand="Geox", type="Мокасини", color="Бежевий", size="35", category="Дитяча")
print(footwear8.availability_message())

footwear9 = Footwear(brand="Dr. Martens", type="Черевики", color="Чорний", size="45", category="Чоловіча")
print(footwear9.availability_message())