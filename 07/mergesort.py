def einlesen():
    strings = []
    try:
        with open("strings.txt", 'r' ) as k:
            data = k.read()
            for word in data.split("\n"):
                word = word.strip()
                if not word == "":
                    strings.append(word)
            return strings
    except FileNotFoundError:
        print("Die Datei konnte nicht gefunden werden")

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left,right):
    combined_arr = []
    left_idx, right_idx = 0,0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            combined_arr.append(right[right_idx])
            right_idx += 1
            continue
        if left[left_idx] <= right[right_idx]:
            combined_arr.append(left[left_idx])
            left_idx += 1
    
    # the left or right list is now completely merged
    # check which list is now completely empty
    # left list is not empty
    if left_idx < len(left):
        combined_arr.extend(left[left_idx:])

    if right_idx < len(right):
        combined_arr.extend(right[right_idx:])

    print(f"left {left}")
    print(f"right {right}")
    print(f"combined {combined_arr}")
    print("-" * 20)

    return combined_arr

daten = einlesen()

print("-" * 20)

print(f"Unsortiert {daten}")

print("-" * 20)

sortierte_daten = merge_sort(daten)

print(f"Sortiert {sortierte_daten}")


