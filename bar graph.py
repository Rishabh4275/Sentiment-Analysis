import pylab as plt

DayOfWeekOfCall = [1,2,3]
DispatchesOnThisWeekday = [77, 32, 42]
print DayOfWeekOfCall
print DispatchesOnThisWeekday
LABELS = ['Monday', 'Tuesday', 'Wednesday']

plt.bar(DayOfWeekOfCall, DispatchesOnThisWeekday, align='center')
plt.xticks(DayOfWeekOfCall, LABELS)
plt.show()