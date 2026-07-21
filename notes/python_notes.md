# python_notes

## 02
### 函数
1. 了解必须参数、关键字参数、默认参数和不定长可变参数
2. 尤其了解不定长可变参数 *var_args_tuple,返回元组，**var_args_dict,返回字典。
3. 再不定长可变参数中，*可以单独出现，但后面的参数一定要使用关键字参数。
4. 匿名函数，lambda：lamdba arg1,arg2...:expression
5. 函数本质：输入数据-执行逻辑-返回结果
6. 位置参数：按照固定顺序插入，不可混乱
7. 关键字参数：一一对应起来，不容易混乱
8. 默认参数：提前配对，但也可以通过关键字进行修改，在函数中有默认值的参数通常放在没有默认值的参数后面
9. 变量作用域
    - 局部变量：函数内部定义的变量，一般只能在函数内部使用
    - 全局变量：函数外部定义的变量
    - 修改全局变量：global
10. 函数类型注解
    ```
    def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
    ```
11. 文档字符串，函数应说明它做什么、接受什么、返回什么。
    ```
    def calculate_total(price: float, quantity: int) -> float:
    """
    计算商品总价。

    Args:
        price: 商品单价。
        quantity: 商品数量。

    Returns:
        商品总价。

    Raises:
        ValueError: 当价格或数量小于 0 时抛出。
    """
    if price < 0 or quantity < 0:
        raise ValueError("价格和数量不能小于 0")

    return price * quantity
    ```
12. 好的函数的特点
    - 名称能说明用途
    - 只负责一件明确的事
    - 参数和返回值清晰
    - 尽量减少对全局变量的依赖
    - 能处理异常输入
    - 核心业务逻辑使用return，而不是只用print
### 模块
1. 导入模块 import 模块名，但在使用过程中要利用模块名.函数()
2. 导入指定函数，from 模块名 import 函数
3. 给模块起别名 import 模块名 as 别名， 别名.函数()
4. name程序
    ```
    def add(a, b):
        return a + b

    if __name__ == "__main__":
        print(add(1, 2))
    ```
    此时，在导入模块时不会自动执行，只有当处罚if语句时才会执行
5. init的作用：统一暴露接口
6. 不是越多越好，而是根据职责划分   
### 数据结构
列表是一种栈，先进后出。

 
