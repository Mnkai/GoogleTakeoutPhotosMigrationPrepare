import FiletimeUtils


class ExportedObject:

    def __init__(self, filepath):
        self.filepath = filepath
        self.creation_time = FiletimeUtils.get_creation_time(filepath)
        self.modified_time = FiletimeUtils.get_modified_time(filepath)

    def set_creation_time(self, time_in_epoch):
        FiletimeUtils.set_creation_time(self.filepath, time_in_epoch)
        self.creation_time = time_in_epoch

    def set_modified_time(self, time_in_epoch):
        FiletimeUtils.set_modified_time(self.filepath, time_in_epoch)
        self.modified_time = time_in_epoch
