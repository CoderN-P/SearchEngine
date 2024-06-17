from concordance import concordance
from VectorComparison import VectorComparison

string1 = "Robotics uses linear algebra and calculus"
string2 = "robotics linear algebra"

print(VectorComparison(concordance(string1), concordance(string2)).similarity())