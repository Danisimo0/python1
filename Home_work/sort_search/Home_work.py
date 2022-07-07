import re
import string
import unicodedata
str = \
    " Lorem ipsum dolor sit amet, consectetur adipiscing Etiam elit. Mauris eu magna sit amet neque lobortis dignissim. " \
    "Mauris vehicula lacinia bibendum. Phasellus elementum ipsum et mi mollis, sed eleifend elit pharetra. Donec " \
    "interdum tempus ligula non vulputate. Cras mollis rhoncus facilisis. Fusce at viverra magna, id tempor nulla. " \
    "Quisque at felis eget arcu gravida efficitur eget ac enim. Etiam quisque efficitur lorem at lorem dictum, a " \
    "sagittis ipsum pulvinar. Maecenas elit nisi, iaculis a dolor id, tempor molestie dolor. " \
    "Pellentesque aliquet non " \
    "orci at convallis. Donec laoreet nisl quam. Ut accumsan, dui ut mattis ultricies, est nulla semper est, eget " \
    "pulvinar magna lacus ut risus." \
    " Duis sed hendrerit odio. Etiam scelerisque nunc quis placerat interdum." \
    "Nam condimentum enim ac justo fermentum, et" \
    "imper-diet purus finibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Mauris bibendum" \
    "urna vitae ullamcorper"\
    "pellentesque. Aenean in est vitae felis semper vulputate convallis eu quam. Nullam feugiat elementum libero. " \
    "Donec scelerisque finibus laoreet. Nam eu risus facilisis, iaculis urna vitae, aliquam neque. " \
    "Donec elementum ipsum in pretium maximus."\
    "Integer id nulla commodo elit ultricies sollicitudin vel vitae augue. Proin commodo, magna at bibendum rutrum," \
    " odio risus dictum nisi, ac commodo ipsum dolor vitae purus. Maecenas posuere, est id vulputate porta, " \
    "erat lacus efficitur purus, a mattis justo ligula eu felis. Suspendisse potenti. Mauris commodo " \
    "libero ut dui efficitur malesuada. Donec ultricies vel purus vel pellentesque. Etiam fusce a ex in" \
    " libero rutrum placerat suscipit ac tellus. Etiam dignissim ullamcorper tincidunt." \
    " Proin tempor lorem eu nulla euismod, id sollicitudin massa ultricies.^%$$%@%!!% "


substring = "Etiam"
# не понял как преобразовал, (переобразовал ли вообще в юникод) и не понял как вернуть,
# если не сложно, можете пожалуйста написать в телеграмме в чем была ошибка

# count = str.count(substring)
# print(count)
#
# print(len(re.findall("Etiam", str)))
print(str.count("Etiam"))
pass
# uncode = []
# for i in str:
#       uncode.append(i)
#
#
#
# print(str.encode())
def to_ascii(str):
    ascii_values = [ord(character) for character in str]
    return ascii_values
    # unicodedata.normalize()

print(to_ascii(str))

# someString = str
# someString.encode('utf-8')
# print(someString)
#encode: почему то ничего не менялось, было тоже самое
# unicodestr = unicode(bytestr, encoding) unicodestr = unicode(bytestr, "utf-8")
# u = unicode(str, "utf-8")
# str.decode('utf-8', 'ignore')
# def make_unicode(str):
#     if type(str) != unicode:
#         input =  str.decode('utf-8')
#         return input
#     else:
#         return str