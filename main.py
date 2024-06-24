import random

class Field:
    def __init__(self,size,ships):
        self.size = size
        self.ships_alive = ships
        self.grid = []

        for i in range(self.size):
            # Добавим в grid пустой список
            self.grid.append([None]*10)

    def display(self,show_ships=False):
        letters_string = "      A B C D E F G H I J"
        print(letters_string)
        
        counter=1

        for row in self.grid:
            

            display_row = ""
              
            for cell in row:
                if cell == "S" and show_ships:
                    display_row +="■ "    
                elif cell == "X":
                    display_row +="X "
                else:
                    display_row += "0 "
        
            print(f"{counter:2d}    {display_row}")
            counter+=1


class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                coords = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True
    
    def player_turn(self):
        x = input("Введите координату выстрела x (A-J) ")
        y = int(input("Введите координату выстрела y (1-10) "))
    
    # Переводим значения от 0 до 9

        x = "ABCDEFGHIJ".index(x.upper())
        y -= 1

        print(x, y)
    # Проверяем ход
        if self.computer_field.grid[y][x] == "S":
            print("Вы попали!")
            self.computer_field.grid[y][x] = "X"
            self.computer_field.ships_alive -=1
        
        else:
            print("Промах!")

    def computer_turn(self):
        x = random.randint(0,9)
        y = random.randint(0,9)
        if self.player_field.grid[y][x] == "S":
            print("Компьютер попал!")
            self.player_field.grid[y][x] = "X"
            self.player_field.ships_alive -=1
        else:
            print(f"Компьютер промахнулся!")
    def play(self):
        # Создать поле игрока
        self.player_field = Field(self.size, self.ships)
        # Создаем поле компьютера
        self.computer_field = Field(self.size, self.ships)
        
        # Расставляем корабли игрока
        self.place_ships_randomly(self.player_field,self.ships)
        # Расставляем корабли компьютера
        self.place_ships_randomly(self.computer_field,self.ships)

        
        while True:

            print("Расстановка кораблей компьютера:")
            self.computer_field.display(show_ships=False)
            print("Ваша расстановка кораблей:")
            self.player_field.display(show_ships=True)


        #Ход игрока


            self.player_turn()
            # Выход из игры если все корабли умерли
            if self.computer_field.ships_alive == 0:
                print("Вы победили! Все корабли компьютера потоплены")
                break 

            self.computer_turn()
            if self.player_field.ships_alive == 0:
                print("Вы проиграли! Все ваши корабли потоплены")
                break 

if __name__ == "__main__":
    game = BattleshipGame()  
    game.play()
    