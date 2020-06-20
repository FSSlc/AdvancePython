#!/usr/bin/env python
# coding: utf-8

a = {'a': 1}
# 1. clear，清空内容
a.clear()

a = {
    "user1": {"company1": "c1"},
    "user2": {"company2": "c2"}
}

# 2. copy 返回浅拷贝
new_dict = a.copy()
new_dict["user1"]["company1"] = "c3"

# 深拷贝 deepcopy
import copy

a_dict = copy.deepcopy(a)
a_dict["user1"]["company1"] = "ca"
print("a = ", a, "\n", "a_dict = ", a_dict)

# 3. fromkeys
new_list = ["user1", "user2"]
a_dict = dict.fromkeys(new_list, {"key": "value"})
print(a_dict)

# 4. get
value = new_dict.get("user", {})
print(value)

# 5. items
for k, v in new_dict.items():
    print(k, v)

# 6. setdefault
value = new_dict.setdefault("user", "abc")
print(value)

# 7. update
new_dict.update({"user": "def"})
new_dict.update(user="ghi")
new_dict.update([("user", "book")])
print(new_dict)
