#__author__ = 'lintao'
#coding=utf-8
import re
import socket
import msvcrt
import time
import datetime
import time
import conceptnet5
import sys
reload(sys)
sys.setdefaultencoding('utf8')


a = '1kjdisllsldiwq'
print(a[2])
print(a.replace('l','嘿哟'))


#import datetime
#starttime = datetime.datetime.now()
a = 2
b = 'wori'
c = str(a)+b
print (c)
errornumber = 2
error = {
  1: lambda x: 'error:1'+x,
  2: lambda x: 'error:2'+x,
  3: lambda x: 'error:3'+x
}[errornumber]
print error('嘿哟哈')
x = 2
test = {1:'first',2:'second',3:'third'}[3][2]
print test




#p1 = re.compile('检索到 <strong.*?>(.*?)</strong>')
#m1 = p1.findall('检索到 <strong class="red">56197</strong> 条  索书号')
#print m1


from xml.dom import minidom
import types
iii = ['worinima',2,3,4,5,7,3,5,2]
print(iii)
j = [i for i in ['worinima',2,3,4,5,7,3,5,2]]
print(j)
arr = list()
for i in j:
    if type(i) is types.IntType:
        i = str(i)
    arr.append(i)
print(arr)
print(type(j[0]))


s = 'wo<sdkj>c<sjsjsj>ao<2>>>nima'
def stripTags(s):
    ''' Strips HTML tags. 打星号好好看
    '''
    intag = [False]
    def chk(c):
        if intag[0]:
            intag[0] = (c != '>')
            return False
        elif c == '<':
            intag[0] = True
            return False
        return True
    return ''.join(c for c in s if chk(c))
print(stripTags(s))

print (type(0))
def GetAllSequence():
    arr = []
    i = 0
    while i<10:
       cn=chr(ord('0')+i)
       arr.append(cn)
       i = i + 1
    i = 0
    while i<26:
       cn=chr(ord('A')+i)
       arr.append(cn)
       i = i + 1
    return arr
print GetAllSequence()

#正则表达式的使用分两步，先把编程语言写到正则表达模块中，再用模块进行匹配
#基本上遇到'\\\\'和r'\\'这种情况r才有意义 看到1.3   好好看，看分步导入文档
import re
s = r'aaa111aaa , bbb222 , 333ccc'
print(re.findall(r'\d+?(?![a-z]+)', s))
print('\n\n\n')





def stripTags(s):
    ''' Strips HTML tags.
    '''
    intag = [False]
    def chk(c):
        if intag[0]:
            intag[0] = (c != '>')
            return False
        elif c == '<':
            intag[0] = True
            return False
        return True
    return ''.join(c for c in s if chk(c))
def GetInfoFromFile(filename):#file是python的一个类，open返回一个file对象，两者几乎可以替换。
    a=0
    try:
        finfo = file(filename,"r")
        a = 1
    except Exception, e:
        print e
    info = ' '
    if a:
        for line in finfo:
            line = line.replace('\r',' ')
            line = line.replace('\n',' ')
            info +=  line
    finfo.close()
    return info
c = GetInfoFromFile('D:\\python\\crawler\\lib.dlut.htm')
reg1='<h3><span>.*?</span><a\shref="(.*?)"\s+>\d+.(.*?)</a>\s*(.*?)</h3>.*?</span>\s*(.*?)<br\s/>\s*(.*?)&nbsp;(.*?)\s*<br />'
p1 = re.compile(reg1)
m = p1.findall(c)
print 'lib.dlut.htm：'+str(m)
print '长度：'+str(len(m))
print ''

info = GetInfoFromFile('D:\\python\\crawler\\dlut_detail.htm')
regC = '<a\shref="([a-zA-Z0-9._?=]*?)"\stitle="marc_format">'
pC = re.compile(regC)
nC = pC.findall(info)
print 'dlut_detail.htm：'+str(nC)
print '长度：'+str(len(nC))
print ''

info = GetInfoFromFile('D:\\python\\crawler\\dlut_marc.htm')
print info
print info.find("(MARC)")
marc = info[info.find("(MARC)")+6:]
print marc
marc = marc.replace('</li>',chr(30))
print marc
hssh = stripTags(marc)
print hssh
hsshs = hssh.split()
print hsshs
marc = " ".join(hsshs)
print marc
p=marc.replace(';','')
print p
k = p.replace('&#x','\u')
print k
k1 = k.decode('unicode-escape')
print k1


print('----------我是分割线------------------------------------------------------------------')

f = open('D:\\python\\txtfiles\\test2.txt.', 'r')
#print(f.tell())
line = f.readlines(16)
print line
#print(f.tell())
f.close()

#--------------------------文件读取读入演示----------------------------------------
f = open('D:\\python\\txtfiles\\test1.txt.', 'r')
fgg = open('D:\\python\\txtfiles\\result2.txt.', 'w')
for line in f.readlines():
    fgg.write(line)
f.close()
fgg.close()



print ''






print sys.getdefaultencoding()


#---------------------------------------------------------------------------------------------------

f = open("D:\\python\\txtfiles\\test1.txt")
for line in f.readlines():
    print line.decode('gbk', 'ignore').encode('utf-8', 'ignore'),
print ''
print '----------------------------------------------test----------------------------------------------------------------------'


testt = ['xxxx\n', 'xxxx\n', 'xxxx\n', 'zzz\n', 'yy yyyy\n', 'yy yyyy\n', 'xxxx\n', 'aaa\n', 'yy yyyy\n', 'xxxx\n']#this is hownet
ddd = ['xxxx', 'yy yyyy', 'zzz', 'heiyou', 'aaa', 'made']#'a little' 'a lot of flowers' ''sksk    This is senticnet
information_list = list()
for i in range(len(ddd)):
    information_list.append([])

#define entry class
class testt_class:
    entry = ''
    number = 0
    def __init__(self, n, a):
        self.entry = n
        self.number = a

#obtain the list of entry class
class_information_list = list()
for i in range(len(testt)):
    class_information_list.append(testt_class(testt[i], i))
print class_information_list[3].entry
for i in range(len(ddd)):
    count = 0
    j = 0
    while j != len(class_information_list):
        if re.match(ddd[i]+'\n', class_information_list[j].entry):
            information_list[i].append(str(class_information_list[j].number))
            class_information_list.pop(j)
            count += 1
            j -= 1
        j += 1
    information_list[i].insert(0, str(count))
    print 'after '+str(i+1)+' time(s) '+'lenth of the rest testt list: '+str(len(class_information_list))
print information_list




'''
testttt = ['W_E=phoenix\n', 'W_E=Feng\n', 'W_E=image of Buddha\n', 'W_E=many a little makes a mickle\n', 'W_E=a little\n', 'W_E=a\n']
regg = re.compile('W_E=(.*?)$')
for i in range(len(testttt)):
    testttt[i] = (regg.findall(testttt[i]))[0]
print testttt
'''





print '--------------------------------------------------------------我又是分割线:哈希字典------------------------------------------------'
testt = ['xxxx\n', 'xxxx\n', 'xxxx\n', 'zzz\n', 'yy yyyy\n', 'yy yyyy\n', 'xxxx\n', 'aaa\n', 'yy yyyy\n', 'xxxx\n']#this is hownet
ddd = ['xxxx\n', 'yy yyyy\n', 'zzz\n', 'heiyou\n', 'aaa\n', 'made\n']#'a little' 'a lot of flowers' ''sksk    This is senticnet
d = dict()
senticnet = [1,2]
hownet = [(1, 'a'), (2, 'b'), (3, 'c'), (1, 'fycj')]
for k, v in hownet:
    d.setdefault(k, []).append(v)
print d
testlist = list()
for w in senticnet:
    ch = d.get(w, [])
    testlist.append((w, ';'.join(ch)))
print testlist
print testlist[0][1]
'''
e -- w
en2ch = {}
for e, ch in hownet:
    en2ch.setdefault(E, []).append(ch)

resList = []
for w in senet:
    ch = en2ch.get(w, ["xxxx",])
    resList.append((w, ";".join(ch)))

for w, transRes in resList:
    line = w + \t + transRes + "\n";
    write(line)

testList = [("a", 1), ("a", 2), ("b", 3)]
for k, v in testList:
    d.setdefault(k, []).append(v)
print d
'''



print 'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
test = [ '\xe5\x92\x95\xe5\x92\x9a\xe5\x92\x9a', '\xe5\x92\x95\xe5\x93\x9d', '\xe5\x92\x95\xe5\x93\x9d']
f = open('D:\\internship in tsinghua\\Natural Language Processing\\codes\\extraction\\senticnet_information_list___.txt', 'w')
f.writelines(test)
f.close()




class people(object):
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s is speaking: I am %d years old" %(self.name,self.age))
p = people('tom',10,30)
p.speak()
print p.name
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s is speaking: I am %d years old,and I am in grade %d"%(self.name,self.age,self.grade))
s = student('ken',20,60,3)
s.speak()


print '---------------------------------------我又又是分割线：conceptnet中文----------------------------------'
s = "点;点点滴滴;几分;略;略微;稍;稍微;稍为;稍许;少量;些;些微;些须;些许;一点;一点;一点儿;一丁点儿;一些;有点儿"
s = s.decode("utf-8")
print s
r = r"([^;]{2,})"
list = re.findall(r, s)
for i in list:
    print i

s = r'aaa111aaa , bbb222 , 333ccc'
print(re.findall(r'\d+?(?![a-z]+)', s))
