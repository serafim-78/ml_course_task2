import pandas as pd
import re
data = pd.read_csv('titanic.csv', index_col='PassengerId')
print "Task #1: Count of male and female"
print "Male =",data[data['Sex']=='male'].shape[0], "; Female =", data[data['Sex']=='female'].shape[0]
print "Task #2: % of survived"
print "Survived =", "{:.2f}".format(100*float(data[data['Survived']==1].shape[0])/float(data.shape[0])), "%"
print "Task #3: % of 1st class passengers"
print "1st class passangers =", "{:.2f}".format(100*float(data[data['Pclass']==1].shape[0])/float(data.shape[0])), "%"
print "Task #4: average and median of age"
print "Average =", "{:.2f}".format(data['Age'].sum()/data.shape[0]),"; Median =",data['Age'].median()
print "Task #5: correlation of SibSp and Parch"
print data.loc[:, ['SibSp', 'Parch']].corr()
print "Task #6: most popular female name"
fn=pd.DataFrame(columns=['Name'])
for i in range(0, data.shape[0]):
    try:
        name=data[data['Sex']=='female'].loc[:,'Name'][i]
    except:
        continue
    if name.find('(') != -1:
        name = name[name.find('(') + 1:name.find(' ', name.find('('))]
    else:
        name = name[name.find('.') + 2:len(name)]
        if name.find(' ') != -1:
            name = name[0:name.find(' ')]
    fn = fn.append(pd.DataFrame({'Name': name}, index=[0]), ignore_index=True)
fn=fn.groupby(['Name'])['Name'].count()
fn=fn.sort_values(ascending=False)
print fn.keys()[0]