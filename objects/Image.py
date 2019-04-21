import piexif

import EpochExifUtils
from objects.ExportedObject import ExportedObject


class Image(ExportedObject):

    def __init__(self, filepath):
        ExportedObject.__init__(self, filepath)

        self.exif_array = piexif.load(filepath)

    def set_exif_creation_time(self, time_in_epoch):
        original_file_modified_time = self.modified_time

        self.exif_array['Exif'][36867] = EpochExifUtils.epoch_to_exif_format(time_in_epoch)
        piexif.insert(piexif.dump(self.exif_array), self.filepath)
        self.set_modified_time(original_file_modified_time)

    def get_exif_creation_time(self):
        try:
            time_in_exif_format = self.exif_array['Exif'][36867]
            time_in_epoch = EpochExifUtils.exif_format_to_epoch(time_in_exif_format)
            return time_in_epoch
        except KeyError:
            return None
