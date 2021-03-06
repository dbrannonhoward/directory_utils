from minimalog.minimal_log import MinimalLog
from os.path import exists
from os import getcwd
from os import makedirs
from os import name
from os import walk
from pathlib2 import Path
ml = MinimalLog(__name__)


def append_path_to_filename(path: Path, filename: str) -> str:
    full_file_path = Path(path, filename)
    return full_file_path


def build_full_path_to_filename(path: Path, filename: str) -> Path:
    full_path = Path(path, filename)
    return full_path


def build_home_paths(destination: str) -> Path:
    event, known_path, built_path = 'returning {} as {}', get_project_home(), Path()
    assert (isinstance(known_path, Path)), '{} is invalid object type {}'.format(known_path, type(known_path))
    ml.log_event('building path to {} using {}'.format(destination, known_path))
    for part_depth, part in enumerate(known_path.parts):
        if part_depth > 2:
            built_path = Path(built_path, destination)
            break
        built_path = Path(built_path, part)
        if destination == 'root' and part_depth == 0:
            break
        if destination == 'home' and part_depth == 1:
            break
        if destination == 'user' and part_depth == 2:
            break
    if not destination_in_path(destination, built_path):
        return None
    assert (exists(built_path)), 'requested path does not exist'
    event.format(destination, built_path)
    return built_path


def create_directory_at_path(path: Path, directory: str) -> bool:
    event = 'create directory {}'
    ml.log_event(event.format(directory), event_completed=False)
    full_path = Path(path, directory)
    if exists(full_path):
        ml.log_event(event + '.. but it already existed!'.format(directory))
        return True
    try:
        makedirs(full_path)
        if exists(full_path):
            ml.log_event(event.format(directory), event_completed=True)
            return True
        ml.log_event(event + '.. failure!'.format(directory))
        return False
    except OSError as o_err:
        ml.log_exception(o_err)


def destination_in_path(destination: str, path: Path) -> bool:
    for part in path.parts:
        if destination in part:
            return True
    return False


def filter_files_by_ext(files: list, valid_extensions: list) -> list:
    ml.log_event('get all files with valid extensions {}'.format(valid_extensions), event_completed=False)
    files_with_extension = list()
    try:
        for file in files:
            for extension in valid_extensions:
                if extension in file:
                    files_with_extension.append(file)
        if len(files_with_extension) < 1:
            raise OSError('no files found with extensions {} in files {}'.format(valid_extensions, files))
        ml.log_event('get all files with valid extensions {}'.format(valid_extensions), event_completed=True)
        return files_with_extension
    except IndexError as i_err:
        ml.log_exception(i_err)


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


def get_common_posix_folders() -> list:
    return ['Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Videos']


def get_common_posix_paths() -> list:
    common_built_paths = list()
    try:
        for common_folder in get_common_posix_folders():
            common_built_paths.append(build_home_paths(common_folder))
        return common_built_paths
    except OSError as o_err:
        ml.log_exception(o_err)


def get_cwd_as_path() -> Path:
    path = Path(getcwd())
    if not is_path(path):
        raise TypeError('{} object is not of type {}'.format(path, Path))
    return Path(getcwd())


def get_data_path() -> Path:
    path = get_cwd_as_path()
    ml.log_event('get data path', event_completed=False)
    try:
        data_path = Path(str(path), DATA_PATH)
        ml.log_event('get data path {}'.format(data_path), event_completed=True)
        return data_path
    except OSError as os_err:
        ml.log_exception(os_err)


def get_linux_home_path() -> Path:
    path = get_cwd_as_path()
    try:
        ml.log_event('get linux home path', event_completed=False)
        home_path = path.parts[1]
        ml.log_event('get linux home path {}'.format(home_path), event_completed=True)
        return home_path
    except OSError as o_err:
        ml.log_exception(o_err)


def get_linux_root_path() -> Path:
    event = 'get linux root path '
    path = get_cwd_as_path()
    try:
        ml.log_event(event, event_completed=False)
        root_path = path.root
        ml.log_event(event + '{}'.format(root_path), event_completed=True)
        return Path(root_path)
    except OSError as o_err:
        ml.log_exception(o_err)


def get_linux_user_path() -> Path:
    event = 'get linux user path '
    path = get_cwd_as_path()
    try:
        ml.log_event(event, event_completed=False)
        user_dir = path.parts[2]
        ml.log_event(event + '{}'.format(user_dir), event_completed=True)
        return user_dir
    except OSError as o_err:
        ml.log_exception(o_err)


def get_linux_username() -> Path:
    event = 'get linux username '
    path = get_cwd_as_path()
    try:
        ml.log_event(event, event_completed=False)
        username = str(path.parts[2])
        ml.log_event(event + '{}'.format(username), event_completed=True)
        return username
    except OSError as o_err:
        ml.log_exception(o_err)


def get_os_downloads_path() -> Path:
    event = 'get downloads path '
    ml.log_event(event, event_completed=False)
    path = get_cwd_as_path()
    try:
        downloads_parent = Path()
        downloads_path = build_home_paths('Downloads')
        downloads_path = Path(downloads_parent, DOWNLOADS_PATH)
        ml.log_event(event + '{}', event_completed=True)
        return downloads_path
    except OSError as o_err:
        ml.log_exception(o_err)


def get_os_name() -> str:
    return name  # from imports


def get_path_at_cwd() -> Path:
    event = 'get path object '
    ml.log_event(event, event_completed=False)
    try:
        path = Path(getcwd())
        ml.log_event('returning path object as {}'.format(path))
        ml.log_event(event + '{}'.format(path), event_completed=True)
        return path
    except OSError as os_err:
        ml.log_exception(os_err)


def get_project_home() -> Path:
    event = 'get project home '
    path = get_cwd_as_path()
    ml.log_event(event + '{}'.format(path), event_completed=False)
    try:
        ml.log_event(event + '{}'.format(path), event_completed=True)
        return Path(str(path.parent), path.parts[-1])
    except OSError as os_err:
        ml.log_exception(os_err)


def is_path(path: Path) -> bool:
    if path is None:
        ml.log_event('path is none', level=ml.ERROR)
        raise Exception('object {} is not of type {}'.format(path, Path))
    try:
        if isinstance(path, Path):
            return True
        return False
    except OSError as o_err:
        ml.log_exception(o_err)


def move_files(files: dict(), dest_path: Path) -> bool:
    # TODO
    ml.log_event('moving files {} to {}'.format(files.keys(), dest_path), event_completed=False)
    for file in files:
        pass


def os_is_posix(force_compliance=False) -> bool:
    sub, os_name = 'six', get_os_name()
    if force_compliance:
        assert (sub in os_name), 'unsupported operating system'
    if sub in os_name:
        return True
    return False


def os_is_windows(force_compliance=False) -> bool:
    sub, os_name = 'nt', get_os_name()
    if force_compliance:
        assert (sub in os_name), 'unsupported operating system'
    if sub in os_name:
        return True
    return False


def __debug():
    pass


if __name__ == '__main__':
    from data_src.CONSTANTS import *
    if DEBUG:
        __debug()
else:
    from .data_src.CONSTANTS import *
    if not os_is_posix(force_compliance=True):
        event = 'unsupported OS, may be unstable'
        print(event)
        ml.log_event(event, level=ml.WARNING, announce=True)
