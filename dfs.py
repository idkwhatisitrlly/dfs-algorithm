def build_graph(edges):
    """
    Строит граф из списка рёбер
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
    """
    # Проверка на корректность входного параметра
    if start not in graph:
        raise ValueError(f"Вершина {start} отсутствует в графе")
    
    visited = []
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            # Добавляем соседей в обратном порядке, чтобы обход происходил в порядке возрастания
            if vertex in graph:
                neighbors = sorted(graph[vertex], reverse=True)
                stack.extend(neighbors)
    
    return visited

def find_path_length(graph, start, end):
    """
    Находит длину пути от вершины start до вершины end
    """
    # Проверка на корректность входных параметров
    if start not in graph:
        raise ValueError(f"Начальная вершина {start} отсутствует в графе")
    if end not in graph:
        raise ValueError(f"Конечная вершина {end} отсутствует в графе")
    
    if start == end:
        return 0
    
    visited = set()
    queue = [(start, 0)]  # (вершина, длина пути до неё)
    
    while queue:
        vertex, length = queue.pop(0)
        
        if vertex == end:
            return length
        
        if vertex not in visited:
            visited.add(vertex)
            
            if vertex in graph:
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, length + 1))
    
    return -1  # Путь не найден

def main():
    # Считываем рёбра графа
    edges_input = input("Введите рёбра графа в формате 'вершина1 вершина2' (по одному ребру на строку, пустая строка для завершения):\n")
    edges = []
    
    while edges_input:
        try:
            u, v = map(int, edges_input.split())
            edges.append((u, v))
        except ValueError:
            print("Ошибка: введите два целых числа, разделенных пробелом")
        edges_input = input()
    
    # Строим граф
    graph = build_graph(edges)
    
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