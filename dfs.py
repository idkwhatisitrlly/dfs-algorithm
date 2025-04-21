def build_graph(edges):

    graph = {}
    for u, v in edges:
        # Добавляем обе вершины в граф, если их еще нет
    if u not in graph:
            graph[u] = []
     if v not in graph:
            graph[v] = []
        # Добавляем ребро от У К В
        graph[u].append(v)
    return graph

def dfs(graph, start):

    visited = set()  # Множество посещенных вершин
    path = []        # Путь обхода
    
    def dfs_recursive(vertex):
        # Отмечаем вершину как посещенную
        visited.add(vertex)
        # Добавляем вершину в путь
        path.append(vertex)
        
        # Рекурсивно обходим всех непосещенных соседей
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Начинаем обход с указанной вершины
    dfs_recursive(start)
    return path

def find_path_length(graph, start, end):
    # Проверка наличия вершин в графе
    if start not in graph or end not in graph:
        raise ValueError(f"Вершины {start} и/или {end} отсутствуют в графе")
    
    visited = set()  
    path_length = -1 # Длина пути (по умолчанию -1, если путь не найден)
    found = False    # Флаг нахождения пути
    
    def dfs_path(vertex, length):
        nonlocal path_length, found
        
        # Если нашли конечную вершину, сохраняем длину пути
        if vertex == end:
            path_length = length
            found = True
            return
        
     
        visited.add(vertex)
        
        # Перебираем всех соседей текущей вершины
        for neighbor in graph.get(vertex, []):
            # Если путь еще не найден и сосед не посещен
            if not found and neighbor not in visited:
                dfs_path(neighbor, length + 1)
    
    # Начинаем поиск пути с начальной вершины
    dfs_path(start, 0)
    return path_length

def main():
    """
    Основная функция программы.
    Считывает ввод пользователя и выполняет соответствующие операции с графом.
    """
    # Чтение входных данных
    edge_list = []
    print("Введите рёбра графа в формате 'u v', по одному на строку.")
    print("Для завершения ввода введите пустую строку.")
    
    # Считываем список рёбер
    while True:
        edge = input()
        if not edge:
            break
        u, v = map(int, edge.split())
        edge_list.append((u, v))
    
    # Выбор режима работы
    mode = input("Выберите режим (1 - обход в глубину, 2 - поиск длины пути): ")
    graph = build_graph(edge_list)
    
    if mode == '1':
        try:
         # Режим обхода в глубину
            start_vertex = int(input("Введите стартовую вершину: "))
            if start_vertex not in graph:
              raise ValueError(f"Вершина {start_vertex} отсутствует в графе")
            
            path = dfs(graph, start_vertex)
        except ValueError as e:
            print(f"Ошибка: {e}")
    elif mode == '2':
        try:
            # Режим поиска длины пути
        start_vertex = int(input("Введите начальную вершину: "))
            end_vertex = int(input("Введите конечную вершину: "))
            
            path_length = find_path_length(graph, start_vertex, end_vertex)
        
            if path_length != -1:
              print(f"Длина пути от {start_vertex} до {end_vertex}: {path_length}")
            else:
                print(f"Путь от {start_vertex} до {end_vertex} не найден")
        except ValueError as e:
           print(f"Ошибка: {e}")
    else:        print("Неправильный режим")

if __name__ == "__main__":
    main() 
