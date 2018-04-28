import re

m = re.match("foo", "food is awesome food is nice!")

print(re.match("foo", "food is Right!").group())

print(re.search("foo", "this really is a footmat!").group())

bt = "bat|bet|but|bot"

print(re.search(bt, "please bet bat bot!").group())

anyend = ".end"

print(re.match(anyend, "BendenfBend").group())
print(re.search(anyend, "BBenenf9end").group())

patt = "3.+14"

print(re.match(patt, "3e14").group())
print(re.search(patt, "asE33fas14").group())

part = "3\.+.+14"

print(re.search(part, "asd3.ggh144sss").group())

strn = "[DE][at][h][i][cr][au][l ]"

print(re.match(strn, "Dahiru ").group())
print(re.search(strn, "sdsaDahicalasd").group())

print(re.match("Ethical|Dahir", "Dahir").group())

print(re.match("\w+@(\w+\.)?\w+\.com", "dahirmuhammad3@www.gmail.com").group())
print(re.search("\w+@(\w+\.)*\w+\.com", "This is the Email: dahir@demo.majorstation.com Please don't SPAM!").group())

m = re.search("(\w\w\w)-(\d\d\d)", "abc-123")
print m.group(2)

m = re.search("^The \w+", "The Boy is not")
print(m.group())

m = re.search(r"\bThe", "She Boy is not The")
m = re.search(r"\BThe", "ShTheBoy is not")

m.group()

len(re.findall("in", "Some times i feel like nothin can become somthin writin nothin cos of ratin"))

#print re.findall(r"(th\w+)", "this that those they them theirs thy thou")

m = re.finditer(r"(th\w+)", "this that those they them theirs thy thou")

m = re.subn("[^aeiou]", "X", "A legend is Born!")

re.subn(r"(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})", r"\2/\1/\3", "10/12/1995")

re.subn(r"(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})", r"\2/\1/\3", "10/12/95")

DATA = ('Mountain View, CA 94040','Sunnyvale, CA','Los Altos, 94023','Cupertino 95014','Palo Alto CA')

for DATUM in DATA:
	re.split(", |(?= (?:\d{5}|[A-Z]{2})) ", DATUM)

re.findall(r"(?i)yes", "Yes this yes YES")

print re.findall(r"(?i)Th\w+", "This is the Quick Through")
txt = """
This Line is the best, 
like the way it is,
now and there time is up!, 
time rules all That Breath. 
"""
print re.findall(r"(?im)(^th[\w]+)", txt)

txt = """
The first line thes
the second line
the third line
"""

print re.findall(r"(?is)th\w+", txt)

txt = """Guido van Rossum
Tim Peters
Alex Martelli
Just van Rossum
Raymond Hettinger"""

print re.findall(r"\w+(?= van Rossum)", txt)

txt = """
 sales@phptr.com
 postmaster@phptr.com
 eng@phptr.com
 noreply@phptr.com
 admin@phptr.com
"""

print re.findall(r"(?m)^\s+(?!noreply|postmaster)(\w+)", txt)

print bool(re.search(r"(?:(x)|y)(?(1)y|x)", "yyxx"))

txt = """
$ who 
wesley       console      Jun 20 20:33 
wesley       pts/9        Jun 22 01:38    (192.168.0.6) 
wesley       pts/1        Jun 20 20:33    (:0.0) 
wesley       pts/2        Jun 20 20:33    (:0.0) 
wesley       pts/4        Jun 20 20:33    (:0.0) 
wesley       pts/3        Jun 20 20:33    (:0.0) 
wesley       pts/5        Jun 20 20:33    (:0.0) 
wesley       pts/6        Jun 20 20:33    (:0.0) 
wesley       pts/7        Jun 20 20:33    (:0.0) 
wesley       pts/8        Jun 20 20:33    (:0.0) 
"""
print re.split(r"\s\s+", txt)
