from uuid import UUID


def is_uuid_valid(uuid_to_test):
    """
    This function validate if the user id is a uuid
    :param uuid_to_test:
    :return:
    """
    try:
        uuid_obj = UUID(uuid_to_test, version=4)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test
