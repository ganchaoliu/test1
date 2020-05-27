from common.models import *

c1 = Country.objects.create(name='中国')
c2 = Country.objects.create(name='美国')
c3 = Country.objects.create(name='印度')
c4 = Country.objects.create(name='巴勒斯坦')
c5 = Country.objects.create(name='埃及')

Student.objects.create(name='小明', grade=1, country=c1)
Student.objects.create(name='小度', grade=2, country=c2)
Student.objects.create(name='小爱', grade=1, country=c3)
Student.objects.create(name='小花', grade=2, country=c4)
Student.objects.create(name='小黑', grade=3, country=c5)
Student.objects.create(name='小白', grade=3, country=c1)

s2 = Student.objects.filter(grade=2, country__name='美国')\
    .values('name', 'country__name')

cn = Country.objects.get(name='中国')
a = cn.student_set.all()

