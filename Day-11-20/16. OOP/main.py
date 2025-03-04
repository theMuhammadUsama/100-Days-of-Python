# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)
# timmy.bk(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)

table2 = PrettyTable()
table2.field_names = ["Name OS", "Type"]
table2.add_row(["Ubuntu", "Debian"])
table2.add_divider()
table2.add_row(["Kali", "Debian"])
table2.add_divider()
table2.add_row(["CentOS", "RPM"])
table2.add_divider()
table2.add_row(["Rocky", "RPM"])

print(table2)