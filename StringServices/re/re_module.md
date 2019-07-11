1.语法规则

在Python里，定义正则表达式的字符串，在字符串前加`r`，表示原始字符串，可以免去很多烦人的转义，如`r'\'`与`'\\'`是表示同一个字符串。

| 语法| 说明 | 实例 | 完整匹配的字符串 |
| - | - | - | - |
| 一般字符 | 匹配字符自身 | abc | abc |
| . | 匹配除换行外的字符，如果指定`re.DOTALL`模式，则包括换行也会匹配 | a.c | abc，adc，aac等 |
| \ | 转义字符，即把特殊字符还原本身 | a\.c | a.c，这里`.`不再是匹配任意字符，而是`.`本身 |
| [...] | 1.指定可匹配的字符集，可以匹配字符集中的任一字符，如`[abc]`匹配`a`，`b`或`c`。<br> 2.字符集也可以通过范围给出，如`[a-z]`表示从`a`到`z`的所有小写字母。<br> 3.如果要取反，即指定排除的字符集，则第一个字符用`^`，如`[^abc]`表示匹配非`a`非`b`非`c`的其它字符。<br> 4.特殊字符在中括号中不再具有特殊意义（即还原特殊字符本身），如`[(+*)]`，`(,+,*,)`都是匹配自身，不再有特殊意义。<br> 5.对于三个特殊字符`],^,-`，则要用`\`转义，如`[\^]`，则匹配`^`自身。 | a[bcd]e | abe, ace, ade |
| \d | 匹配数字，即`[0-9]` | a\dc | a1c, a2c, a3c等 |
| \D | 匹配非数字，即`[^\d]` | a\Dc | abc, aac, acc等 |
| \s | 匹配空白字符，即`[ \t\r\n\f\v]` | a\sc | a c等 |
| \S | 匹配非空白字符，即`[^\s]` | a\Sc | abc, aac, acc等 | 
| \w | 匹配单词的字符，即`[A-Za-z0-9_]` | a\wc | abc, aBc, a9c等 |
| \W | 匹配非单词的字符，即`[^\w]` | a\Wc | a c, a$c等 |
| * | 匹配前一字符0次或无限次 | ab* | a, ab, abb, abbb等 |
| + | 匹配前一字符1次或无限次 | ab+ | ab, abb, abbb等 |
| ? | 匹配前一字符0次或1次 | ab? | a或ab |
| {m} | 匹配前一字符`m`次 | ab{3}c | abbbc |
| {m,n} | 匹配前一字符`m`至`n`次，如不指定`n`，则为`m`至无限次 | ab{2,3}c | abbc或abbbc |
| *?, +?, ?? | 把`*`，`+`，`?`变为非贪婪模式，如对于字符串`abbbc`，正则表达式`ab?`会匹配到`abbb`，而`ab??`则匹配到`a`。 |  |  |
| {m,n}? | 把`{m,n}`变为非贪婪模式，如对于字符串`aaaaa`，正则表达式`a{3,5}`会匹配5个`a`，而正则表达式`a{3,5}?`只匹配3个`a`。 |  |  |
| ^ | 匹配字符串开头，如指定`re.MULTILINE`模块，则匹配每一行开头 | ^abc | abc |
| $ | 匹配字符串结尾，如指定`re.MULTILINE`模块，则匹配每一行结尾 | abc$ | abc |
| \A | 只匹配字符串开头 | \Aabc | abc |
| \Z | 只匹配字符串结尾 | abc\Z | abc |
| \b | 匹配空字符，这样的空字符仅在词的开头或结尾，即介于`\w`和`\W`之间。<br>如`\bfoo\b`可以匹配到`foo`，`foo.`，`(foo)`，`bar foo baz`，而不能匹配`foobar`，`foo3`。 | a\b!bc | a!bc |
| \B | 匹配空字符，这样的空字符不能在词的开头或结尾，即`[^\b]`。<br>如`py\B`可以匹配到`python`，`py3`，`py2`，但不能匹配`py`，`py`，`py!`。 | a\Bbc | abc |
| \| | 匹配`|`左右任意一个。总是先匹配左边，如果成功，则跳过匹配右边。如果没有括号括着，它的范围是整个正则表达式。 | abc\|def | abc, def |
| (...) | 被括起来的表达式作为分组，从左至右，每遇到一个分组括号，编号加1。分组作为一个整体，如遇`|`，则仅在该组有效，而不是整个正则表达式。 | a(123\|456)c | a123c |
| \\<number\> | 引用编号为\<number\>的分组匹配到的字符串。组编号从1开始。 | (.+) \1 | the the, 55 55等 |
| (?P\<name\>...) | 括号分组，除了原来的编号外，再指定一个为<name>的名字。 | (?P\<id\>abc){2} | abcabc |
| (?P=name) | 引用名字为\<name\>的分组匹配到的字符串。 | (?P\<id\>\d)cc(?P=id) | 2cc2, 3cc3等 |
| (?:...) | 括号分组，但不提供编号，不能引用。 | (?:abc){2} | abcabc |
| (?#...) | 注释 | aa(?#comment)11 | aa11 |
| (?=...) | 之后的字符串内容需要匹配表达式才算成功匹配。不消耗字符串内容。 | a(?=\d) | a的后面是数字 |
| (?!...) | 之后的字符串内容需要不匹配表达式才算成功匹配。不消耗字符串内容。 | a(?!\d) | a的后面不能是数字 |
| (?<=...) | 之前的字符串内容需要匹配表达式才算成功匹配。不消耗字符串内容。 | (?<=abc)def | abcdef |
| (?<!...) | 之前的字符串内容需要不匹配表达式才算成功匹配。不消耗字符串内容。 | (?<!\d)a | a的前面不能是数字 |
| (?(id/name)yes-pattern\|no-pattern) | 如果编号为id或名字为name的组匹配到字符，则需要匹配yes-pattern，否则需要匹配no-pattern。no-pattern可以不指定。 | (\d)abc(?(1)\d\|ddd) | 2abc1, abcddd等 |
| (?iLmsux) | iLmsux每个字母代表一个匹配模式，用在正则表达式开头，可选多个。<br>i --> `re.I, re.IGNORECASE`，忽略大小写。<br>L --> `re.L, re.LOCALE`，依赖语言环境。<br>m --> `re.M, re.MULTILINE`，多行模式。<br>s --> `re.S, re.DOTALL`，`.`可以匹配换行。<br>u --> `re.U, re.UNICODE`，依赖Unicode。<br>x --> `re.X, re.VERBOSE`，详细模式。 | (?i)abc | ABC |

2.re模块（https://docs.python.org/2/library/re.html）

```
re.compile(pattern, flags=0)：编译正则表达式，返回pattern对象。flags可以是以下的一些值，多个一起用`|`。
re.DEBUG：显示调试信息。
re.I：re.IGNORECASE：忽略大小写。
re.L：re.LOCALE：`\w, \W, \b, \B, \s, \S`依赖本地语言环境。
re.M：re.MULTILINE：多行模式。
re.S：re.DOTALL：`.`包括换行。
re.U：re.UNICODE：`\w, \W, \b, \B, \d, \D, \s, \S`依赖Unicode。
re.X：re.VERBOSE：详细模式。

re.search(pattern, string, flags=0)：搜索string，找到第一个匹配pattern的位置，返回re.MatchObject对象。没有匹配，则返回None。
re.match(pattern, string, flags=0)：从string的开头开始匹配pattern，如果遇到无法匹配的，返回None，如果匹配未完但到了string的结尾，返回None，返回None就是匹配失败。匹配成功，匹配终止，不再向后匹配，返回re.MatchObject对象。
re.split(pattern, string, maxsplit=0, flags=0)：pattern作为分隔符来分割string，maxsplit指定最大的分割次数，不指定则全部分割。
re.findall(pattern, string, flags=0)：搜索string，以列表的形式返回全部匹配pattern的子串。
re.finditer(pattern, string, flags=0)：搜索string，返回一个re.MatchObject对象的迭代器。
re.sub(pattern, repl, string, count=0, flags=0)：用repl替代匹配的子串，并返回替代后的字符串。repl可以是字符串，也可以是一个函数。当为字符串时，可以使用\<number>或\g<number>或\g<name>来引用分组。当为函数时，接受一个re.MatchObject对象的参数，返回的是用于替换的字符串，返回的字符串不能再引用分组。count是指定最多替换的次数。
re.subn(pattern, repl, string, count=0, flags=0)：作用与re.sub()相同，只是返回值是一个元组，(替代后的字符串, 替换次数)。
re.escape(pattern)：除了ASCII的字母和数字，转义其它的字符。
re.purge()：清除正则表达式缓存。

exception re.error：异常。
```

```
class re.RegexObject

方法和属性：
search(string[, pos[, endpos]])：同re.search(), pos指定从string的哪个索引位置开始，endpos指定结束位置。
match(string[, pos[, endpos]])：同re.match()。
split(string, maxsplit=0)：同re.split()。
findall(string[, pos[, endpos]])：同re.findall()。
finditer(string[, pos[, endpos]])：同re.finditer()。
sub(repl, string, count=0)：同re.sub()。
subn(repl, string, count=0)：同re.subn()。
flags：正则表达式的模式组合标识。
groups：正则表达式中的组数。
groupindex：分组名字与对应组ID的字典。
pattern：正则表达式字符串。
```

```
class re.MatchObject

方法和属性：
expand(template)：功能类似于re.sub()，把匹配到的分组代入template中，返回代入后的字符串。
group([group1, ...])：返回一个或多个匹配的组。group1默认值为0，即返回整个匹配字符串。
groups([default])：返回所有匹配的组，不包括第0组。
groupdict([default])：返回指定了名字的所有组的字典。
start([group])：end([group])：返回指定匹配组的起始索引。group的默认值为0，即为整个匹配的子串。如果group存在，但对匹配没有贡献，则返回-1。
span([group])：返回元组，(start([group]), end([group]))。
pos：传给re.RegexObject.match()或re.RegexObject.search()的pos。
endpos：传给re.RegexObject.match()或re.RegexObject.search()的endpos。
lastindex：最后匹配组的编号，如果没有匹配组，返加None。
lastgroup：最后匹配组的名字，如果组没有名字，或没有匹配组，返加None。
re：由re.RegexObject.match()或re.RegexObject.search()产生此re.MatchObject实例的re.RegexObject对象。
string：传给re.RegexObject.match()或re.RegexObject.search()的字符串。
```
