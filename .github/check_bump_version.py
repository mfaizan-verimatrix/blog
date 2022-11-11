import sys

def main(old_version, new_version):
    old_major, old_minor, old_patch = old_version.split(".", 2)
    new_major, new_minor, new_patch = new_version.split(".", 2)

    old_major = int(old_major)
    old_minor = int(old_minor)
    new_major = int(new_major)
    new_minor = int(new_minor)

    if new_major < old_major:
        sys.exit(1)

    if new_minor < old_minor:
        sys.exit(1)

    if new_patch == old_patch:
        sys.exit(1)

    if new_major > old_major:
        sys.exit(0)

    if new_minor > old_minor:
        sys.exit(0)

    if new_patch != old_patch:
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
