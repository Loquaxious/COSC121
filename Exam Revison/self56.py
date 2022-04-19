def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Hilda the Heffalump"""
    current_height = 0
    rushes = 0
    while current_height < slope_height:
        current_height += rush_height_gain
        rushes += 1
        if current_height >= slope_height:
            break
        current_height -= back_sliding
    return rushes

ans = num_rushes(10, 10, 9)
print(ans)

ans = num_rushes(100, 10, 0)
print(ans)