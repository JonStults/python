def draw_stars(x):
    for i in x:
        a = ''
        for j in range(0,i):
            a += '*'
        print a

# print draw_stars([1,3,5,3])

# def stars(x):
#     star = '*'
#     for i in x:
#         num = ''
#         num = i * star
#         print num
#
# stars([3,4,3,3,5])

# Part 2

def stars2(x):
    star = '*'
    for i in x:
        newStr = ""
        if type(i) == str:
            for a in range(0, len(i)):
                newStr += i[0].lower()
        else:
            for b in range(0,i):
                newStr += star
        print newStr
stars2([4, "Tom", 1, "Jon", 8])
