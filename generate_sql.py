import time
from datetime import date
import random
from datetime import timedelta

import sys
d = date(2013, 1, 1)

group_indexs = [1, 2, 3]

for i in range(365 * 3):
	for group_index in group_indexs:
		sys.stdout.write("INSERT INTO DActual (THEDATE,REGION,IGROUP,SDAY,EVENTS,WEATHER, interval1,interval2,interval3,interval4,interval5,interval6,interval7,interval8,interval9,interval10,interval11,interval12,interval13,interval14,interval15,interval16,interval17,interval18,interval19,interval20,interval21,interval22,interval23,interval24,interval25,interval26,interval27,interval28,interval29,interval30,interval31,interval32,interval33,interval34,interval35,interval36,interval37,interval38,interval39,interval40,interval41,interval42,interval43,interval44,interval45,interval46,interval47,interval48) VALUES (" )
		sys.stdout.write("STR_TO_DATE('"+d.isoformat()+"', '%Y-%m-%d')")
		sys.stdout.write(',')
		sys.stdout.write('0')
		sys.stdout.write(',')
		sys.stdout.write(str(group_index))
		sys.stdout.write(',')
		sys.stdout.write('0')
		sys.stdout.write(',')
		sys.stdout.write('0')
		sys.stdout.write(',')
		sys.stdout.write('0,')

		for j in range(47):
			sys.stdout.write(str(random.randint(0, 50)))
			sys.stdout.write(',')
		sys.stdout.write(str(random.randint(0, 50)))

		sys.stdout.write(');\n')

	d = d + timedelta(days=1)


'''

	CREATE TABLE DActual (id int auto_increment not null, THEDATE DATE, REGION int, IGROUP int, SDAY int, EVENTS int, WEATHER int, interval1 int, interval2	int, interval3	int,interval4	int,interval5	int,interval6	int,interval7	int,interval8	int,interval9	int,interval10	int,interval11	int,interval12	int,interval13	int,interval14	int,interval15	int,interval16	int,interval17	int,interval18	int,interval19	int,interval20	int,interval21	int,interval22	int,interval23	int,interval24	int,interval25	int,interval26	int,interval27	int,interval28	int,interval29	int,interval30	int,interval31	int,interval32	int,interval33	int,interval34	int,interval35	int,interval36	int, interval37	int,interval38	int,interval39	int,interval40	int,interval41 int,	interval42 int,	interval43	int, interval44	int,interval45	int,interval46	int,interval47	int,interval48 int, PRIMARY KEY(id) );

'''



	
