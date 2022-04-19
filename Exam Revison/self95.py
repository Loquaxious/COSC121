def make_frequencies(data):
    """L"""
    
    plate_dict = {}
    for plate in data:
        if plate not in plate_dict:
            plate_dict[plate] = 1
        
        else:
            plate_dict[plate] += 1
        
    return plate_dict

plates = ['AAA123', 'AAA123', 'BBB111', 'FOO833', 'AAA123', 'FOO833']
count_dict = make_frequencies(plates)
for plate, count in sorted(count_dict.items()):
    print(plate,'->', count)