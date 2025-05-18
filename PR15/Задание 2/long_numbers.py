class LongNumber:
    def __init__(self, number_str):
        self.digits = [int(d) for d in str(abs(int(number_str)))[::-1]]  # Храним цифры в обратном порядке
        self.sign = 1 if int(number_str) >= 0 else -1

    def __str__(self):
        if not self.digits:
            return "0"
        result = ''.join(str(d) for d in self.digits[::-1])
        return f"-{result}" if self.sign == -1 else result

    def add(self, other):
        result = []
        carry = 0
        max_len = max(len(self.digits), len(other.digits))

        a_digits = self.digits + [0] * (max_len - len(self.digits))
        b_digits = other.digits + [0] * (max_len - len(other.digits))

        for i in range(max_len):
            digit_sum = a_digits[i] + b_digits[i] + carry
            result.append(digit_sum % 10)
            carry = digit_sum // 10

        if carry:
            result.append(carry)

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result_num = LongNumber("0")
        result_num.digits = result
        return result_num

    def subtract(self, other):
        result = []
        borrow = 0
        max_len = max(len(self.digits), len(other.digits))

        a_digits = self.digits + [0] * (max_len - len(self.digits))
        b_digits = other.digits + [0] * (max_len - len(other.digits))

        for i in range(max_len):
            digit = a_digits[i] - b_digits[i] - borrow
            if digit < 0:
                digit += 10
                borrow = 1
            else:
                borrow = 0
            result.append(digit)

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result_num = LongNumber("0")
        result_num.digits = result
        return result_num

    def multiply(self, other):
        result = [0] * (len(self.digits) + len(other.digits))

        for i in range(len(self.digits)):
            carry = 0
            for j in range(len(other.digits)):
                product = self.digits[i] * other.digits[j] + result[i + j] + carry
                result[i + j] = product % 10
                carry = product // 10
            result[i + len(other.digits)] += carry

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result_num = LongNumber("0")
        result_num.digits = result
        result_num.sign = self.sign * other.sign
        return result_num


def power(base, exponent):
    if not exponent.digits or exponent.digits == [0]:
        return LongNumber("1")
    result = LongNumber("1")
    base_copy = LongNumber(str(base))
    exp_copy = LongNumber(str(exponent))

    while exp_copy.digits != [0]:
        if exp_copy.digits[0] % 2 == 1:
            result = result.multiply(base_copy)
        base_copy = base_copy.multiply(base_copy)
        exp_digits = []
        carry = 0
        for d in exp_copy.digits[::-1]:
            d = d + carry * 10
            exp_digits.append(d // 2)
            carry = d % 2
        exp_digits = exp_digits[::-1]
        while len(exp_digits) > 1 and exp_digits[0] == 0:
            exp_digits.pop(0)
        exp_copy.digits = exp_digits

    return result
