# coding:utf-8
# re.sub(pattern, repl, string[, count])
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串
import re

p = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)') # 使用名称引用
s = 'i say, hello world!'
# re.sub(pattern, repl, string[, count])
# == pattern.sub(repl, string[, count]) #tang
print p.sub(r'\g<word2> \g<word1>', s)
p = re.compile(r'(\w+) (\w+)') # 使用编号
print p.sub(r'\2 \1', s)
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print p.sub(func, s)



# re.subn(pattern, repl, string[, count])


s = 'i say, hello world!'
p = re.compile(r'(\w+) (\w+)')
print p.subn(r'\2 \1', s)
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
print p.subn(func, s)



replacedStr = re.sub("\d+", "222", "hello 123 world 456")
print replacedStr



inputStr = "hello crifan, nihao crifan";
replacedStr = re.sub(r"hello (\w+), nihao \1", "crifanli", inputStr);
print "replacedStr=",replacedStr; #crifanli




inputStr = "hello crifan, nihao crifan";
replacedStr = re.sub(r"hello (?P<name>\w+), nihao (?P=name)", "\g<name>", inputStr);
print "replacedStr=",replacedStr; #crifan

inputStr = "hello crifan, nihao crifan";
replacedStr = re.sub(r"hello (\w+), nihao \1", "\g<1>", inputStr);
print "replacedStr=",replacedStr; #crifan


def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456";

    def _add111(matched):
        intStr = matched.group("number");  # 123
        intValue = int(intStr);
        addedValue = intValue + 111;  # 234
        addedValueStr = str(addedValue);
        return addedValueStr;

    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr);
    print "replacedStr=", replacedStr;  # hello 234 world 567


###############################################################################
if __name__ == "__main__":
    pythonReSubDemo();


inputStr = "摘要 tts nihao";
replacedStr = re.sub(r"摘要 (?P<name>\w+) nihao", "\g<name>", inputStr);
print "replacedStr=",replacedStr; #crifan
