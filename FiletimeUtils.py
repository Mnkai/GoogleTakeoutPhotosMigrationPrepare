import os.path


# Returns modified time in epoch
def get_modified_time(filepath):
    return int(os.path.getmtime(filepath))


# Returns creation time in epoch
def get_creation_time(filepath):
    return int(os.path.getctime(filepath))


def set_modified_time(filepath, time_in_epoch):
    os.utime(filepath, (-1, int(time_in_epoch)))


def set_creation_time(filepath, time_in_epoch):
    assert False;
    return None
