import copy

# data structures
class Interval:
    def __init__(self, b=0, e=0):
        self.begin = b
        self.end = e
    
    def __str__(self):
        return "[" + str(self.begin) + ", " + str(self.end) + "]"

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end

def serial(root):
    if root == None: return "# "
    ret = str(root.val) + ' '
    ret += serial(root.left)
    ret += serial(root.right)
    return ret

class TreeNode:
    def __init__(self, v=0):
        self.val, self.left, self.right = v, None, None
    
    def __str__(self):
        return serial(self)
    
    def __repr__(self):
        return self.__str__()

############################################################

def test_wiggle(arr):
    if not arr:
        return False
    test_flag = True
    for i in range(len(arr)-1):
        if test_flag:
            if arr[i] > arr[i+1]:
                return False
        else:
            if arr[i] < arr[i+1]:
                return False
        test_flag = not test_flag
    return True

# test anagram
def test_anagram(a0, a1):
    if len(a0) != len(a1) : return False
    t0, t1 = copy.deepcopy(a0), copy.deepcopy(a1)
    t0.sort()
    t1.sort()
    return cmp(t0, t1) == 0

# loaders
def read_tree(f, nums):
    if nums == 0: return None
    cur = f.readline().rstrip('\r|\n')
    if(cur == "#"): return None
    
    root = TreeNode(int(cur))
    nums -= 1
    root.left = read_tree(f, nums)
    nums -= 1
    root.right = read_tree(f, nums)
    return root

def read_tree_array(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        n = int(f.readline())
        ret.append(read_tree(f, n))
    return ret

def read_tree_matrix(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_tree_array(f))
    return ret

def read_interval_array(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        b = int(f.readline())
        e = int(f.readline())
        ret.append(Interval(b,e))
    return ret

def read_interval_matrix(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_interval_array(f))
    return ret

def read_interval_matrix_arr(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_interval_matrix(f))
    return ret

def read_int_array(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(int(f.readline()))
    return ret

def read_int_matrix(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_int_array(f))
    return ret

def read_int_matrix_arr(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_int_matrix(f))
    return ret

def read_double_array(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(float(f.readline()))
    return ret

def read_double_matrix(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_double_array(f))
    return ret

def read_double_matrix_arr(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_double_matrix(f))
    return ret

def read_string_array(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(f.readline().rstrip('\r|\n'))
    return ret

def read_string_matrix(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_string_array(f))
    return ret

def read_string_matrix_arr(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_string_matrix(f))
    return ret

def read_bool_array(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        val = int(f.readline())
        if val == 1: ret.append(True)
        else: ret.append(False)
    return ret

def read_bool_matrix(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_bool_array(f))
    return ret

def read_bool_matrix_arr(f) :
    num = int(f.readline())
    ret = []
    for i in range(num):
        ret.append(read_bool_matrix(f))
    return ret