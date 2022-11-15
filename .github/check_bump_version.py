import sys

def main(old_version, new_version):
    '''
    format of pyproject.toml version
    major.minor.patch[-alpha.[1-9]]

    ex:
    1.4.0-alpha.1, 1.4.0

    1.4.1 > 1.4.0

    1.4.0 > 1.4.0-alpha.1

    1.4.0-alpha.2 > 1.4.0-alpha.1
    '''

    # fail, new and old versions are equal
    if old_version == new_version:
        sys.exit(1)

    old_major, old_minor, old_patch = old_version.split(".", 2)
    new_major, new_minor, new_patch = new_version.split(".", 2)

    old_major = int(old_major)
    old_minor = int(old_minor)
    new_major = int(new_major)
    new_minor = int(new_minor)
    old_patch_version = int(old_patch[0])
    new_patch_version = int(new_patch[0])

    # fail, new major version cannot be lower than the current major version
    if new_major < old_major:
        sys.exit(1)

    # fail, new minor version cannot be lower than the current minor version
    if new_minor < old_minor:
        sys.exit(1)

    # fail, new patch version cannot be lower than the current patch version
    if new_patch_version < old_patch_version:
        sys.exit(1)

    # pass, major version bumped
    if new_major > old_major:
        sys.exit(0)

    # pass, minor version bumped
    if new_minor > old_minor:
        sys.exit(0)

    # pass, patch version bumped
    if new_patch_version > old_patch_version:
        sys.exit(0)


    if (new_major == old_major) and \
        (new_minor == old_minor) and \
        (new_patch_version == old_patch_version):

        # pass, new patch > old patch
        if ("-" in old_patch) and ("-" not in new_patch):
            sys.exit(0)

        # fail, new patch < old patch
        if ("-" not in old_patch) and ("-" in new_patch):
            sys.exit(1)

        old_dev_version = int(old_patch[-1])
        new_dev_version = int(new_patch[-1])

        # fail, new patch < old patch
        # pass otherwise new patch > old patch
        if new_dev_version < old_dev_version:
            sys.exit(1)
        else:
            sys.exit(0)

    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print('Bump versions not provided')
        sys.exit(1)

    try:
        main(sys.argv[1], sys.argv[2])
    except Exception as e:
        sys.exit(1)
