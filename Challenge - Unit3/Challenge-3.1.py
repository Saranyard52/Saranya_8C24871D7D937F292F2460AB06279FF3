def linearsearchproduct(productlist, targetproduct):
    indices = []
    for index, product in enumerate(products):
        if product == targetproduct:
            indices.append(index)
    return indices

products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target1 = "shoes"
target2 = "apple"
result = linearsearchproduct(products, target1)
print(result)

