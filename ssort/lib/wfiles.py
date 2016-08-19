import os

def walk_dir(from_dir):
    "Walk directory from from_dir using generator."""
    try:
        ds_files = os.listdir(from_dir)
    except:
        # [1] if directory has no file, exception (errno 13) occurrs
        # [2] I am an generator, can not return with argument
        return
    real_dir = os.path.realpath(from_dir)
    for f in ds_files:
        fullpath = os.path.join(real_dir,f)
        if os.path.isdir(fullpath) and not os.path.islink(fullpath):
            for f2 in walk_dir(fullpath):
                yield f2
        else:
            yield fullpath


def wkdir(from_dir):
    "Walk directory from from_dir using generator."""
    try:
        ds_files = os.listdir(from_dir)
    except:
        # [1] if directory has no file, exception (errno 13) occurrs
        # [2] I am an generator, can not return with argument
        return
    real_dir = os.path.realpath(from_dir)
    for f in ds_files:
        fullpath = os.path.join(real_dir,f)
        if os.path.isdir(fullpath) and not os.path.islink(fullpath):
            for f2 in wkdir(fullpath):
                yield f2
        else:
            yield (f, real_dir)
