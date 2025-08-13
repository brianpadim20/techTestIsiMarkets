def minJumpCost(stones):
    def cycle_cost(path):
        full_path = path + path[-2:0:-1] + [path[0]]
        return max(abs(full_path[i+1] - full_path[i]) for i in range(len(full_path)-1))

    # Ruta 1: posiciones pares primero, luego impares al revés
    path1 = stones[::2] + stones[-2::-2]

    # Ruta 2: posiciones impares primero, luego pares al revés
    path2 = stones[1::2] + stones[-1::-2]

    # Ruta 3: alternando extremos hacia el centro (para cubrir casos como el de 22)
    left, right = 0, len(stones) - 1
    path3 = []
    while left <= right:
        path3.append(stones[left])
        if left != right:
            path3.append(stones[right])
        left += 1
        right -= 1

    return min(cycle_cost(path1), cycle_cost(path2), cycle_cost(path3))


# Pruebas
print(minJumpCost([0, 3, 9]))
print(minJumpCost([0, 2, 5, 6, 7]))
print(minJumpCost([0, 3, 8, 15, 20, 22, 31, 44, 52]))