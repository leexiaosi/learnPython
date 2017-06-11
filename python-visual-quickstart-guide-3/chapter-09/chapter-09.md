# 9 异常处理

- 抛出异常 `raise`
- `try-except-finally`
 - `except` 捕获异常
    - except ValueError: `ValueError`异常
    - except (ValueError, TypeError) : 两种异常
    - except: 所有异常
 - finally 一定会执行
- `with`语句，即便发生异常，也尽早执行清理操作
