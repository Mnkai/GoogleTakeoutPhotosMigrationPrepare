import json


def get_googlemetadata_timestamp(image_fullpath):
    try:
        metadata_content = json.load(open(image_fullpath, "r"))

        # if photoTakenTime exists - use that field. Else, use creationTime field
        # if none of them exists, return None

        try:
            return metadata_content["photoTakenTime"]["timestamp"]
        except KeyError:
            try:
                return metadata_content["creationTime"]["timestamp"]
            except KeyError:
                return None
    except FileNotFoundError:
        return None


def get_googlemetadata_filename(image_fullpath):
    last_index_of_point = image_fullpath.rfind(".")
    imagefile_extension = image_fullpath[last_index_of_point:]
    assert len(imagefile_extension) <= 5

    # Metadata uses JSON format...
    json_filepath = image_fullpath + ".json"

    assert json_filepath[json_filepath.rfind("."):] == ".json"
    return json_filepath
