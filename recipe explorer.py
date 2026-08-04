pasta=("pasta arabiata","italian","20","medium")
biryani=("chicken biryani","indian","45","hard")

print("recipe 1",pasta)
print("name",pasta[0])
print("cuisine",pasta[1])
print("difficulty",pasta[3])
all_recipes=(pasta,biryani)
print(all_recipes)
print("second recipe name",all_recipes[1][0])
print("first recipe name",all_recipes[0][0])
print("pasta recipe details")
for detail in pasta:
    print("-",detail)


pasta_ingredients={"tomato","garlic","olive oil","chilli","pasta","garlic"}
biryani_ingredients={"rice","chicken","garlic","onion","tomato","spices"}
print(pasta_ingredients)
print("\n",biryani_ingredients)
pasta_ingredients.add("parmasean")
print(pasta_ingredients)
pasta_ingredients.discard("chilli")
print(pasta_ingredients)
all_ingredients=pasta_ingredients.union(biryani_ingredients)
common_ingredients=pasta_ingredients.intersection(biryani_ingredients)
only_pasta=pasta_ingredients.difference(biryani_ingredients)
only_biryani=biryani_ingredients.difference(pasta_ingredients)
uniquetoeach=pasta_ingredients.symmetric_difference(biryani_ingredients)
print("\nAll ingredients (union):", all_ingredients)

print("Common ingredients (intersection):", common_ingredients)

print("Only in Pasta (difference):", only_pasta)

print("Not shared (sym. difference):", uniquetoeach)

print("Only in biryani (difference):", only_biryani)