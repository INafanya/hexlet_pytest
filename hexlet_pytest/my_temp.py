def make_validator():
    checks = []

    def validator(value):
        return all(check(value) for check in checks)

    def add_check(check_func):
        checks.append(check_func)
        return validator

    validator.add_check = add_check
    validator.is_valid = validator

    return validator


def test():
    checks = []
    checks.append(lambda x: x > 5)
    print(f'{checks=}')
    checks.append(lambda x: x % 2 == 0)
    print(f'{checks=}')
    print(all(check(8) for check in checks))
    checks = []
    print(f'{checks=}')
    checks[:] = ['first']
    print(f'{checks=}')
    checks[:] = ['second']
    print(f'{checks=}')

test()