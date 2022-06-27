from documentary_private import Documentary

m = Documentary('Mulan',2020,'action')
#m.__get_movie() #เรียก private method ไม่ได้
#print(m.__genre) #เรียก private attribute ไม่ได้
m.print_detail()
print(f'year: {m._Movie__year}')
#obj._ClassName__privateattribute