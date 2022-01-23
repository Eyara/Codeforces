def main():
    import sys
    from pathlib import Path

    contest_name, division_name, number_of_problem = sys.argv[1], sys.argv[2], int(sys.argv[3])

    problems = ['A', 'B', 'C', 'D', 'E']

    if number_of_problem > 5:
        raise Exception(f"There were gotten more than {len(problems)} problems. Creating will be canceled.")

    folder_name = f'{contest_name} {division_name}'
    path_name = f'contests/{folder_name}'
    Path(path_name).mkdir(parents=True, exist_ok=True)

    for i in range(0, number_of_problem):
        problem_folder_name = f'{path_name}/{problems[i]}'
        problem_file_name = f'Problem {problems[i]}.py'
        Path(problem_folder_name).mkdir(parents=True, exist_ok=True)
        Path(f'{problem_folder_name}/{problem_file_name}').touch()


if __name__ == "__main__":
    main()
