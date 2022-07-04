#country_obj.py
from country_subclass import *

#create europe object
eu = Europe("Norway",5505859)
eu.location = "60.4720° N, 8.4689° E"
eu.capital = "Oslo"
eu.show_detail()

#create asia object
a = Asia("Malaysia",33181072)
a.gdp = 336.7
a.show_detail()