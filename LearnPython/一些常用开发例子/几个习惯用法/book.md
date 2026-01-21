

## 1. 测试代码的通用模板  总是把执行放在main中

```python
def download():...

def main() -> None:
    print(download(url="http://www.baidu.com"))

if __name__ == '__main__':
    main()
```


## 2. 函数的入参出参都写上类型列表，方便使用

```python
def 
```