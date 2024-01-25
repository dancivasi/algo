from pprint import pprint
def solution(dishes):
    ingredients_their_dishes = {}
    result = []
    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredient in ingredients_their_dishes:
                ingredients_their_dishes[ingredient].append(dish[0])
            else:
                ingredients_their_dishes[ingredient] = [dish[0]]
    for key, values in sorted(ingredients_their_dishes.items()):
        if len(values) >= 2:
            result.append([key] + sorted(values))
    return result

if __name__ == "__main__":
    assert solution(
        [
            ["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"],
        ]
    ) == [
        ["Cheese", "Quesadilla", "Sandwich"],
        ["Salad", "Salad", "Sandwich"],
        ["Sauce", "Pizza", "Quesadilla", "Salad"],
        ["Tomato", "Pizza", "Salad", "Sandwich"],
    ]
    assert solution(
        [
            ["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"],
        ]
    ) == [
        ["Cheese", "Quesadilla", "Sandwich"],
        ["Chicken", "Chicken Curry", "Quesadilla"],
        ["Nuts", "Fried Rice", "Salad"],
        ["Onions", "Fried Rice", "Pasta"],
    ]
