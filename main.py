import heapq

def min_cost_to_connect_cables(cables):
    if not cables:
        return 0
    
    heapq.heapify(cables)  
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)  
        second = heapq.heappop(cables)  
        
        cost = first + second  
        total_cost += cost
        
        heapq.heappush(cables, cost)  
    
    return total_cost

def merge_k_lists(lists):
    min_heap = []
    
    for lst in lists:
        for num in lst:
            heapq.heappush(min_heap, num)

    merged_list = [heapq.heappop(min_heap) for _ in range(len(min_heap))]
    return merged_list

# Приклад 
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print("Відсортований список:", merge_k_lists(lists))