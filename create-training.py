def main():
    import sys
    from pathlib import Path

    category, problem_name = sys.argv[1], sys.argv[2]

    path_name = f'training/{category}'
    Path(path_name).mkdir(parents=True, exist_ok=True)

    problem_file_name = f'{problem_name}.py'
    Path(f'{path_name}/{problem_file_name}').touch()


if __name__ == "__main__":
    main()
