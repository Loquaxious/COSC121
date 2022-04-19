def stringy(s1, s2, s3):
    if s1.startswith(s3) and s2.endswith(s3):
        print(s1 + s2 + s3)

stringy("hatonhead?w", "hat", "hat")