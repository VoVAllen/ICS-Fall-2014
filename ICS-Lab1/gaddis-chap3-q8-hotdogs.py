from math import ceil

people = int(input("How many people are attending the cookout? - "))
hotdogs_per_person = int(input("How many hotdogs per person? - "))

hotdogs_required = people * hotdogs_per_person

print( "Hotdog packages (x10) required =", ceil(hotdogs_required / 10.0) )
print( "Hotdog bun packs (x8) required =", ceil(hotdogs_required / 8.0) )

print( "Leftover hotdogs =", 10 - (hotdogs_required % 10) )
print( "Leftover buns =", 8 - (hotdogs_required % 8) )
