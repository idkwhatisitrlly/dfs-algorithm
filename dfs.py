def build_graph(edges):
    """
    Строит граф из списка рёбер
    
    Параметры:
    edges -- список пар вершин, представляющих рёбра графа
    
    Возвращает:
    словарь, где ключи - вершины, а значения - списки смежных вершин
    """
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    return graph

def dfs(graph, start):
    """
    Выполняет обход графа в глубину и возвращает путь обхода
    
    Параметры:
    graph -- граф в виде словаря смежности
    start -- начальная вершина обхода
    
    Возвращает:
    список вершин в порядке обхода
    
    Исключения:
    ValueError -- если начальная вершина отсутствует в графе
    """
    # Проверка на корректность входного параметра
    if start not in graph:
        raise ValueError(f"Вершина {start} отсутствует в графе")
    
    visited = []  # Список посещенных вершин
    stack = [start]  # Стек вершин для обхода
    
    while stack:
        vertex = stack.pop()  # Извлекаем вершину из стека
        if vertex not in visited:
            visited.append(vertex)  # Отмечаем вершину как посещенную
            # Добавляем соседей в обратном порядке, чтобы обход происходил в порядке возрастания
            if vertex in graph:
                neighbors = sorted(graph[vertex], reverse=True)
                stack.extend(neighbors)  # Добавляем соседей в стек
    
    return visited

def find_path_length(graph, start, end):
    """
    Находит длину пути от вершины start до вершины end
    
    Параметры:
    graph -- граф в виде словаря смежности
    start -- начальная вершина
    end -- конечная вершина
    
    Возвращает:
    целое число - длина кратчайшего пути или -1, если путь не существует
    
    Исключения:
    ValueError -- если начальная или конечная вершина отсутствует в графе
    """
    # Проверка на корректность входных параметров
    if start not in graph:
        raise ValueError(f"Начальная вершина {start} отсутствует в графе")
    if end not in graph:
        raise ValueError(f"Конечная вершина {end} отсутствует в графе")
    
    if start == end:
        return 0
    
    visited = set()  # Множество посещенных вершин
    queue = [(start, 0)]  # Очередь (вершина, длина пути до неё)
    
    while queue:
        vertex, length = queue.pop(0)  # Извлекаем вершину и длину пути из очереди
        
        if vertex == end:
            return length  # Нашли конечную вершину
        
        if vertex not in visited:
            visited.add(vertex)  # Отмечаем вершину как посещенную
            
            if vertex in graph:
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, length + 1))  # Добавляем соседей в очередь
    
    return -1  # Путь не найден

def main():
    """
    Основная функция программы
    """
    # Считываем рёбра графа
    print("Введите рёбра графа в формате 'вершина1 вершина2' (по одному ребру на строку, пустая строка для завершения):")
    edges_input = input()
    edges = []
    
    # Парсим ввод пользователя
    while edges_input:
        try:
            u, v = map(int, edges_input.split())
            edges.append((u, v))
        except ValueError:
            print("Ошибка: введите два целых числа, разделенных пробелом")
        edges_input = input()
    
    # Строим граф
    graph = build_graph(edges)
    
    # Выбираем режим работы
    choice = input("Выберите режим (1 - обход графа, 2 - найти длину пути): ")
    
    if choice == "1":
        try:
            start_vertex = int(input("Введите стартовую вершину: "))
            path = dfs(graph, start_vertex)
            print(f"Путь обхода: {', '.join(map(str, path))}")
        except ValueError as e:
            print(f"Ошибка: {e}")
    elif choice == "2":
        try:
            start_vertex = int(input("Введите начальную вершину: "))
            end_vertex = int(input("Введите конечную вершину: "))
            path_length = find_path_length(graph, start_vertex, end_vertex)
            
            if path_length >= 0:
                print(f"Длина пути от вершины {start_vertex} до вершины {end_vertex}: {path_length}")
            else:
                print(f"Путь от вершины {start_vertex} до вершины {end_vertex} не существует")
        except ValueError as e:
            print(f"Ошибка: {e}")
    else:
        print("Некорректный выбор режима")

if __name__ == "__main__":
    main()