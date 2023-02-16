def format_linter_error(error: dict) -> dict:
    return ({
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    })


def format_single_linter_file(file_path: str, errors: list) -> dict:
    print({
        "errors": format_linter_error({key: [i[key] for i in errors] for key in errors[0]}),
        "path": file_path,
        "status": "failed"
    })


def format_linter_report(linter_report: dict) -> list:
    pass


format_single_linter_file(
              "./source_code_2.py",
              [
                  {
                      "code": "E501",
                      "filename": "./source_code_2.py",
                      "line_number": 18,
                      "column_number": 80,
                      "text": "line too long (99 > 79 characters)",
                      "physical_line": '    return f"I like to filter, rounding, doubling, '
                                       "store and decorate numbers: {', '.join(items)}!\"",
                  },
                  {
                      "code": "W292",
                      "filename": "./source_code_2.py",
                      "line_number": 18,
                      "column_number": 100,
                      "text": "no newline at end of file",
                      "physical_line": '    return f"I like to filter, rounding, doubling, '
                                       "store and decorate numbers: {', '.join(items)}!\"",
                  },
              ],
          )
