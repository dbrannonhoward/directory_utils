from data_src.CONSTANTS import DATA_DIR
from minimalog.minimal_log import MinimalLog
from os import getcwd
from os import walk
from pathlib2 import Path
ml = MinimalLog(__name__)


def get_all_files_in(path: Path) -> list:
    ml.log_event('find all files in {}'.format(path))
    files_in_dir = list()
    try:
        for root, dirs, files in walk(path):
            for file in files:
                files_in_dir.append(file)
        return files_in_dir
    except IndexError as i_err:
        ml.log_exception(i_err)


def get_all_files_with_valid_extensions(files: list, valid_extensions: list) -> list:
    ml.log_event('get all files with valid extensions {}'.format(valid_extensions))
    files_with_extension = list()
    try:
        for file in files:
            for extension in valid_extensions:
                if extension in file:
                    files_with_extension.append(file)
        if len(files_with_extension) < 1:
            raise OSError
        return files_with_extension
    except IndexError as i_err:
        ml.log_exception(i_err)


def get_data_dir(path: Path) -> Path:
    ml.log_event(event='get project home full path', event_completed=False)
    if not isinstance(path, Path):
        raise TypeError
    try:
        return Path(str(path), DATA_DIR)
    except OSError as os_err:
        ml.log_exception(os_err)


def get_project_home(path: Path) -> Path:
    ml.log_event(event='get project home full path', event_completed=False)
    if not isinstance(path, Path):
        raise TypeError
    try:
        return Path(str(path.parent), path.parts[-1])
    except OSError as os_err:
        ml.log_exception(os_err)


def get_path_object_at_cwd() -> Path:
    ml.log_event(event='getting path object')
    try:
        path = Path(getcwd())
        ml.log_event('returning path object as {}'.format(path))
        return path
    except OSError as os_err:
        ml.log_exception(os_err)


if __name__ == '__main__':
    pass
