def remove_duplicates(lijst):
    current_index = len(lijst) - 1
    while current_index >= 0:
        current_element = lijst[current_index]
        i = lijst.index(current_element)
        if current_index != i:
            del lijst[current_index]
        current_index -= 1