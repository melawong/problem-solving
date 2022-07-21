# Given current directory and change directory path, return final path.

# For Example:

# Curent                 Change            Output

# /                    /facebook           /facebook
# /facebook/anin       ../abc/def          /facebook/abc/def
# /facebook/instagram   ../../../../.      /
# /facebook/anin        ../../abc          /abc
# /facebook/anin        ../../             /
# /facebook/anin        ../abc/../../facebook/anon  /facebook/anon

# var root_list [ root, facebook, anin ]
# split change into list, loop over,
# if !len(split_root) continue
# if the currentitem is .., pop off the root_list,
# if it's a ., continue
# else add that to root_list
# return joined root_list "/"

def directory_change(curr_dir, change_dir):
    split_root = curr_dir.split("/")    #["", ""]
    split_change = change_dir.split("/") #[facebook]

    for dir in split_change:
        if not len(split_root) and dir == "..":
            continue
        elif dir == "..":
            split_root.pop()
        elif dir == ".":
            continue
        else:
            split_root.append(dir)

    return "/" + "/".join(split_root)   #/facebook