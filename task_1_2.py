#Загружает список рецептов из файла в словарь
def read_cook_book():
    import os
    
    file_path = os.path.join(os.getcwd(), 'files', 'recipes.txt')
    
    with open(file_path, 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            quantity_of_ingredients = int(file.readline())
            ingredients = []
            for _ in range(quantity_of_ingredients):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({'ingredient_name': ingredient_name, 
                                    'quantity': int(quantity), 
                                    'measure': measure})
            file.readline()
            cook_book[dish] = ingredients
        
    return cook_book


#Формирует словарь с названием ингредиентов и его количества для блюда
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book()
    ingredient_list = {}
    
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient_list.get(ingredient['ingredient_name']) == None:
                ingredient_list.setdefault(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count})
            else:
                ingredient_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count    
    
    return ingredient_list

    
            
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))
