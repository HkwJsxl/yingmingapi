from application import jsonrpc
# PEP484规范: 给所有的变量、函数/方法的返回值、参数，必须指定他们的类型
from typing import Union, Any, List, Dict
from numbers import Real


def index():
    return "home.index"


def test():
    return "home.test"


@jsonrpc.method("Home.menu")
def menu(data0: Any, data1: int, data2: float, data3: str, data4: Union[int, bool], data5: bool, data6: List[Any],
         data7: List[int], data8: Dict[str, Real]) -> List[Any]:
    ret = [
        data0,  # 可以填写任意类型数据
        data1,  # 只能填写整型
        data2,  # 只能填写浮点型
        data3,  # 只能填写字符串
        data4,  # Union表示联合类型， Union[int, bool]表示只能填写 整型和布尔型
        data5,  # 只能填写布尔型
        data6,  # List[Any]，只能填写列表数据，列表中的成员可以是任意类型的数据
        data7,  # List[int]，只能填写列表数据，列表中的成员只能是整型，除此之外，还有 List[str]、List[Dict[str, Any]]
        data8,  # [str, Real]，只能填写字典数据，字典中的键必须是字符串，值必须是数值类型
    ]
    print(f"ret={ret}")
    return ret
