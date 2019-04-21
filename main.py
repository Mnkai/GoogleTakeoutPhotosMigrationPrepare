import os

import ArrayUtils
import GoogleMetadataUtils
from objects.ExportedObject import ExportedObject
from objects.Image import Image

counter = 0


def directory_walk(start_path, extension):
    to_return = []

    for (dirpath, dirnames, filenames) in os.walk(start_path):
        for filename in filenames:
            if filename.lower().endswith(extension.lower()):
                to_return.append(os.sep.join([dirpath, filename]))

    return to_return


def exif_process(image):
    if image.get_exif_creation_time() is None:
        googlemetadata_file = GoogleMetadataUtils.get_googlemetadata_filename(image.filepath)
        googlemetadata_timestamp = GoogleMetadataUtils.get_googlemetadata_timestamp(googlemetadata_file)

        if googlemetadata_timestamp is not None:
            image.set_exif_creation_time(googlemetadata_timestamp)
            image.set_modified_time(googlemetadata_timestamp)
            global counter
            counter += 1
            print("Change " + str(image.filepath) + " exif and modification time to " + str(
                googlemetadata_timestamp))

    else:
        # Set image modification date to exif data
        if image.modified_time is not image.get_exif_creation_time():
            image.set_modified_time(image.get_exif_creation_time())

            print("Change " + str(image.filepath) + " modification time to " + str(
                image.get_exif_creation_time()))
            return


def other_process(object):
    googlemetadata_file = GoogleMetadataUtils.get_googlemetadata_filename(object.filepath)
    if googlemetadata_file is not None:
        googlemetadata_timestamp = GoogleMetadataUtils.get_googlemetadata_timestamp(googlemetadata_file)
        if googlemetadata_timestamp is not None:
            # If possible, try to nuke exif data to avoid confusion
            if object.modified_time is not googlemetadata_timestamp:
                object.set_modified_time(googlemetadata_timestamp)
                global counter
                counter += 1
                print(
                    "Changed " + str(object.filepath) + " modification time to " + str(googlemetadata_timestamp))


def main():
    directory_walk_array = []

    directory_walk_array = ArrayUtils.concat(directory_walk_array, directory_walk(".", ".jpg"))
    directory_walk_array = ArrayUtils.concat(directory_walk_array, directory_walk(".", ".jpeg"))
    directory_walk_array = ArrayUtils.concat(directory_walk_array, directory_walk(".", ".tiff"))

    directory_walk_array = ArrayUtils.concat(directory_walk_array, directory_walk(".", ".png"))
    directory_walk_array = ArrayUtils.concat(directory_walk_array, directory_walk(".", ".avi"))
    directory_walk_array = ArrayUtils.concat(directory_walk_array, directory_walk(".", ".mp4"))
    directory_walk_array = ArrayUtils.concat(directory_walk_array, directory_walk(".", ".mov"))

    file_array = []

    for filepath in directory_walk_array:
        try:
            file_array.append(Image(filepath))
        except:
            file_array.append(ExportedObject(filepath))

    for object in file_array:
        if isinstance(object, Image):
            exif_process(object)
        else:
            other_process(object)

    print("Total " + str(counter) + " files processed")


if __name__ == "__main__":
    main()
