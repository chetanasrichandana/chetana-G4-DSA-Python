class Commonelement:
    def common_member(a, b, c):
        a_li = set(a)
        b_li = set(b)
        c_li = set(c)
     
        if (a_li & b_li & c_li):
            print(a_li & b_li & c_li)
          
    a = [1, 2, 3, 4]
    b = [2, 3, 4, 5]
    c = [3, 4, 5, 6]
    common_member(a, b, c)

