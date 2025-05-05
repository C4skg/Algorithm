from typing import Union

class RPN:
    def __init__(self, equation:list) -> None:
        self.equation = equation;

    def get(self) -> Union[int, float]:
        stack = []
        for token in self.equation:
            if token.isdigit():
                stack.append(int(token));
                continue;

            right = stack.pop();
            left  = stack.pop();
            if token == '+':
                imm_value = left + right;
            elif token == '-':
                imm_value = left - right;
            elif token == '*':
                imm_value = left * right;
            elif token == '/':
                imm_value = left / right;
            
            stack.append(imm_value);

        return stack.pop();

if __name__ == '__main__':
    result = RPN(["2", "1", "+", "3", "*"]);

    print(
        result.get()
    )