from minimalog.minimal_log import MinimalLog
from os import getcwd
from os import name
from os import walk
from pathlib2 import Path
ml = MinimalLog(__name__)


def build_path(path_property: int) -> Path:
    path_to_build = Path()
    for path in path_to_build.parts[0:3]:
        path_to_build = Path(path_to_build, path)


def get_all_files_in(path: Path) -> list:
    ml.log_event('find all files in {}'.format(path), event_completed=False)
    files_in_path = list()
    try:
        for root, paths, files in walk(path):
            for file in files:
                files_in_path.append(file)
        ml.log_event('find all files in {}'.format(path), event_completed=True)
        return files_in_path
    except IndexError as i_err:
        ml.log_exception(i_err)


def get_all_files_with_valid_extensions(files: list, valid_extensions: list) -> list:
    ml.log_event('get all files with valid extensions {}'.format(valid_extensions), event_completed=False)
    files_with_extension = list()
    try:
        for file in files:
            for extension in valid_extensions:
                if extension in file:
                    files_with_extension.append(file)
        if len(files_with_extension) < 1:
            raise OSError
        ml.log_event('get all files with valid extensions {}'.format(valid_extensions), event_completed=True)
        return files_with_extension
    except IndexError as i_err:
        ml.log_exception(i_err)


def get_cwd_as_path() -> Path:
    return Path(getcwd())


def get_data_path() -> Path:
    path = get_cwd_as_path()
    ml.log_event('get data path', event_completed=False)
    if not is_path(path):
        raise TypeError
    try:
        data_path = Path(str(path), DATA_PATH)
        ml.log_event('get data path {}'.format(data_path), event_completed=True)
        return data_path
    except OSError as os_err:
        ml.log_exception(os_err)


def get_linux_root() -> Path:
    path = get_cwd_as_path()
    try:
        ml.log_event('get linux root path', event_completed=False)
        root_path = path.root
        ml.log_event('get linux root path {}'.format(root_path), event_completed=True)
        return root_path
    except OSError as o_err:
        ml.log_exception(o_err)


def get_linux_user_dir() -> Path:
    path = get_cwd_as_path()
    if not is_path(path):
        raise TypeError
    try:
        ml.log_event('get linux root path', event_completed=False)
        user_dir = str(path.parts[2])
        ml.log_event('get linux username {}'.format(user_dir), event_completed=True)
        return user_dir
    except OSError as o_err:
        ml.log_exception(o_err)


def get_linux_username() -> Path:
    path = get_cwd_as_path()
    if not is_path(path):
        raise TypeError
    try:
        ml.log_event('get linux root path', event_completed=False)
        username = str(path.parts[2])
        ml.log_event('get linux username {}'.format(username), event_completed=True)
        return username
    except OSError as o_err:
        ml.log_exception(o_err)


def get_os_downloads_path() -> Path:
    ml.log_event('get downloads path', event_completed=False)
    path = get_cwd_as_path()
    if not is_path(path):
        raise TypeError
    try:
        downloads_parent = Path()
        downloads_path = build_path("downloads")
        downloads_path = Path(downloads_parent, DOWNLOADS_PATH)
        ml.log_event('get downloads path as {}', event_completed=True)
        return downloads_path
    except OSError as o_err:
        ml.log_exception(o_err)


def get_os_name() -> str:
    return name


def get_project_home() -> Path:
    path = get_cwd_as_path()
    ml.log_event(event='get project home {}'.format(path), event_completed=False)
    if not is_path(path):
        raise TypeError
    try:
        ml.log_event(event='get project home {}'.format(path), event_completed=True)
        return Path(str(path.parent), path.parts[-1])
    except OSError as os_err:
        ml.log_exception(os_err)


def get_path_object_at_cwd() -> Path:
    ml.log_event('get path object', event_completed=False)
    try:
        path = Path(getcwd())
        ml.log_event('returning path object as {}'.format(path))
        ml.log_event('get path object {}'.format(path), event_completed=True)
        return path
    except OSError as os_err:
        ml.log_exception(os_err)


def is_path(path: Path) -> bool:
    if path is None:
        ml.log_event('path is none', level=ml.ERROR)
        raise IndexError
    try:
        if isinstance(path, Path):
            return True
        return False
    except OSError as o_err:
        ml.log_exception(o_err)


def move_files(files: list, src_path: Path, dest_path: Path) -> bool:
    # TODO work in progress
    ml.log_event('moving files {} from {} to {}'.format(files, src_path, dest_path), event_completed=False)
    if not is_path(src_path) or not is_path(dest_path):
        raise TypeError
    for file in files:
        pass


def os_is_posix() -> bool:
    if 'six' in get_os_name():
        return True
    return False


def __debug():
    os_name = get_os_name()
    linux_root = get_linux_root()
    username = get_linux_username()
    user_dir = get_linux_user_dir()
    proj_home = get_project_home()
    down_dir = get_os_downloads_path()
    data_path = get_data_path()
    pass


if __name__ == '__main__':
    from data_src.CONSTANTS import DATA_PATH, DEBUG, DOWNLOADS_PATH
    if DEBUG:
        __debug()
    pass
else:
    from .data_src.CONSTANTS import DATA_PATH, DOWNLOADS_PATH
    if not os_is_posix():
        event = 'unsupported OS, may be unstable'
        print(event)
        ml.log_event(event, level=ml.WARN, announce=True)
