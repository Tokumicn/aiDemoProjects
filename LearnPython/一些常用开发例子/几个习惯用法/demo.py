import requests

def download(url: str) -> str:
    res = requests.get(url)
    return res.text

def main() -> None:
    print(download(url="http://www.baidu.com"))

if __name__ == '__main__':
    main()



## 入参出参写上类型列表，方便调用人查看
def to_uppercase(l: list[str]) -> list[str]:
    return [s.upper() for s in l]


## 使用enumerate迭代器循环list
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)


## 函数注释插件