def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Herbert the Heffalump"""
    current_height = 0
    rushes = 0
    while current_height < slope_height:
        rushes += 1
        current_height += rush_height_gain
        rush_height_gain -= 0.05 * rush_height_gain
        if current_height >= slope_height:
            break
        current_height -= back_sliding
        back_sliding -= 0.05 * back_sliding

    return rushes

ans1 = num_rushes(100, 15, 7)
print(ans1)

ans = num_rushes(10, 10, 9)
print(ans)