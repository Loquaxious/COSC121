def activity_level_from_steps(steps):
    """Function determining activity level based on number of steps done"""
    if (steps == 0):
        state = 'alive?'
    elif (steps < 5000):
        state = 'sedentary'
    elif (steps < 7500):
        state = 'very low'
    elif (steps < 10000):
        state = 'low'
    elif (steps < 12500):
        state = 'active'
    else:
        state = 'very active'
    return state

def longest_run_at_level(step_records, activity_level):
    """Returns the length of then longest run of days in a row with 
    the given activity level"""
    run = []
    runs = []
    len_runs = []
    n = 0
    max_len_runs = []
    
    for line in step_records:
        date, steps = step_records[n]
        n += 1
        
        if activity_level == activity_level_from_steps(steps):
            run.append(steps)
            runs.append(run[:])            
        else:
            run = []
    for run in runs:
        len_runs.append(len(run))
        max_len_runs.append(max(len_runs))
    return max(max_len_runs, default=0)

step_records = [('2010-01-01',30),
                ('2010-01-02',20),
                ('2010-01-03',30),
                ('2010-01-04',60),
                ('2010-01-05',12000),
                ('2010-01-06',30),
                ('2010-01-07',30),
                ('2010-01-08',10000)]
run_length = longest_run_at_level(step_records, 'sedentary')
print(run_length)

step_records = [('2010-01-01',30),
                ('2010-01-02',20),
                ('2010-01-03',30),
                ('2010-01-04',60),
                ('2010-01-05',10000),
                ('2010-01-06',200),
                ('2010-01-07',40),
                ('2010-01-08',100),
                ('2010-01-09',400),
                ('2010-01-10',600),
                ('2010-01-11',12000)]
run_length = longest_run_at_level(step_records, 'sedentary')
print(run_length)

step_records = [('2010-01-01',30),
                ('2010-01-02',20),
                ('2010-01-03',30),
                ('2010-01-04',60),
                ('2010-01-05',10000),
                ('2010-01-06',15000),
                ('2010-01-07',16000),
                ('2010-01-08',200),
                ('2010-01-09',40),
                ('2010-01-10',100),
                ('2010-01-11',400),
                ('2010-01-12',600),
                ('2010-01-13',12000),
                ('2010-01-14',13000),
                ('2010-01-15',100),
                ('2010-01-16',600),
                ('2010-01-17',600),
                ('2010-01-18',12000),
                ('2010-01-19',10000),
                ('2010-01-20',11000),
                ('2010-01-21',11200)]
run_length = longest_run_at_level(step_records, 'active')
print(run_length)

step_records =  [('2009-03-31', 17202),
                ('2009-04-01', 29163),
                ('2009-04-02', 25869),
                ('2009-04-03', 20862),
                ('2009-04-04', 2566),
                ('2009-04-05', 22390),
                ('2009-04-06', 8248),
                ('2009-04-07', 2133),
                ('2009-04-08', 2336),
                ('2009-04-09', 13464),
                ('2009-04-10', 26315),
                ('2009-04-11', 22315),
                ('2009-04-12', 332),
                ('2009-04-13', 956),
                ('2009-04-14', 28141),
                ('2009-04-15', 17603),
                ('2009-04-16', 26733),
                ('2009-04-17', 9540),
                ('2009-04-18', 14076),
                ('2009-04-19', 10542),
                ('2009-04-20', 4821),
                ('2009-04-21', 940),
                ('2009-04-22', 29726),
                ('2009-04-23', 1753),
                ('2009-04-24', 9312),
                ('2009-04-25', 10882),
                ('2009-04-26', 17376),
                ('2009-04-27', 11827),
                ('2009-04-28', 25160),
                ('2009-04-29', 11753),
                ('2009-04-30', 18885),
                ('2009-05-01', 3133),
                ('2009-05-02', 3385),
                ('2009-05-03', 21480),
                ('2009-05-04', 28016),
                ('2009-05-05', 11578),
                ('2009-05-06', 848),
                ('2009-05-07', 25678),
                ('2009-05-08', 5021),
                ('2009-05-09', 26199),
                ('2009-05-10', 9135),
                ('2009-05-11', 28511),
                ('2009-05-12', 13725),
                ('2009-05-13', 10565),
                ('2009-05-14', 22015),
                ('2009-05-15', 28445),
                ('2009-05-16', 12989),
                ('2009-05-17', 18081),
                ('2009-05-18', 4510),
                ('2009-05-19', 9401),
                ('2009-05-20', 21597),
                ('2009-05-21', 18665),
                ('2009-05-22', 3878),
                ('2009-05-23', 1123),
                ('2009-05-24', 10531),
                ('2009-05-25', 13460),
                ('2009-05-26', 28274),
                ('2009-05-27', 15601),
                ('2009-05-28', 26606),
                ('2009-05-29', 7704),
                ('2009-05-30', 11407),
                ('2009-05-31', 19685),
                ('2009-06-01', 4733),
                ('2009-06-02', 16525),
                ('2009-06-03', 3702),
                ('2009-06-04', 8474),
                ('2009-06-05', 22825),
                ('2009-06-06', 8840),
                ('2009-06-07', 6511),
                ('2009-06-08', 23456),
                ('2009-06-09', 5208),
                ('2009-06-10', 13446),
                ('2009-06-11', 12497),
                ('2009-06-12', 6554),
                ('2009-06-13', 4958),
                ('2009-06-14', 1954),
                ('2009-06-15', 18345),
                ('2009-06-16', 7955),
                ('2009-06-17', 2239),
                ('2009-06-18', 12996),
                ('2009-06-19', 7706),
                ('2009-06-20', 20193),
                ('2009-06-21', 29956),
                ('2009-06-22', 16447),
                ('2009-06-23', 10233),
                ('2009-06-24', 22696),
                ('2009-06-25', 627),
                ('2009-06-26', 25029),
                ('2009-06-27', 5001),
                ('2009-06-28', 25583),
                ('2009-06-29', 26945),
                ('2009-06-30', 13494),
                ('2009-07-01', 1077),
                ('2009-07-02', 22760),
                ('2009-07-03', 14195),
                ('2009-07-04', 12669),
                ('2009-07-05', 15845),
                ('2009-07-06', 5848),
                ('2009-07-07', 29294),
                ('2009-07-08', 7769),
                ('2009-07-09', 10194),
                ('2009-07-10', 12209),
                ('2019-09-14', 9594),
                ('2019-09-15', 13158),
                ('2019-09-16', 7792),
                ('2019-09-17', 24552),
                ('2019-09-18', 14590),
                ('2019-09-19', 14456),
                ('2019-09-20', 6032),
                ('2019-09-21', 25401),
                ('2019-09-22', 13749),
                ('2019-09-23', 15711),
                ('2019-09-24', 8),
                ('2019-09-25', 4271),
                ('2019-09-26', 29118),
                ('2019-09-27', 8594),
                ('2019-09-28', 16809),
                ('2019-09-29', 16742),
                ('2019-09-30', 3196),
                ('2019-10-01', 22219),
                ('2019-10-02', 518),
                ('2019-10-03', 3243),
                ('2019-10-04', 26466),
                ('2019-10-05', 29037),
                ('2019-10-06', 27889),
                ('2019-10-07', 26852),
                ('2019-10-08', 7835),
                ('2019-10-09', 5067),
                ('2019-10-10', 3251),
                ('2019-10-11', 7454),
                ('2019-10-12', 28702),
                ('2019-10-13', 1486),
                ('2019-10-14', 17539),
                ('2019-10-15', 9028),
                ('2019-10-16', 709),
                ('2019-10-17', 16492),
                ('2019-10-18', 21464),
                ('2019-10-19', 6534),
                ('2019-10-20', 12564),
                ('2019-10-21', 16773),
                ('2019-10-22', 21271),
                ('2019-10-23', 11981),
                ('2019-10-24', 22556),
                ('2019-10-25', 1107),
                ('2019-10-26', 25287),
                ('2019-10-27', 3013),
                ('2019-10-28', 9005),
                ('2019-10-29', 7295),
                ('2019-10-30', 18958),
                ('2019-10-31', 15766),
                ('2019-11-01', 17654),
                ('2019-11-02', 16575),
                ('2019-11-03', 14799),
                ('2019-11-04', 18790),
                ('2019-11-05', 21437),
                ('2019-11-06', 11899),
                ('2019-11-07', 21719),
                ('2019-11-08', 12240),
                ('2019-11-09', 5205),
                ('2019-11-10', 20277),
                ('2019-11-11', 19765),
                ('2019-11-12', 14293),
                ('2019-11-13', 10836),
                ('2019-11-14', 16087),
                ('2019-11-15', 1895),
                ('2019-11-16', 18701),
                ('2019-11-17', 27652),
                ('2019-11-18', 17605),
                ('2019-11-19', 24313),
                ('2019-11-20', 15161),
                ('2019-11-21', 26715),
                ('2019-11-22', 8477),
                ('2019-11-23', 9337),
                ('2019-11-24', 15492),
                ('2019-11-25', 14692),
                ('2019-11-26', 29042),
                ('2019-11-27', 432),
                ('2019-11-28', 19359),
                ('2019-11-29', 26702),
                ('2019-11-30', 26109),
                ('2019-12-01', 21157),
                ('2019-12-02', 19994),
                ('2019-12-03', 24138),
                ('2019-12-04', 5171),
                ('2019-12-05', 26060),
                ('2019-12-06', 10768),
                ('2019-12-07', 22370),
                ('2019-12-08', 18601),
                ('2019-12-09', 12751),
                ('2019-12-10', 10681),
                ('2019-12-11', 28462),
                ('2019-12-12', 10680),
                ('2019-12-13', 10204),
                ('2019-12-14', 11200),
                ('2019-12-15', 10200),
                ('2019-12-16', 10001),
                ('2019-12-17', 11234),
                ('2019-12-18', 10003),
                ('2019-12-19', 11345),
                ('2019-12-20', 10200),]
for level in ['alive?', 'sedentary', 'very low', 
              'low', 'active', 'very active']:
    run_length = longest_run_at_level(step_records, level)
    print('{} = {}'.format(level,run_length))