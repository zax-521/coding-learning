"""
    Json数据结构(JavaScript Object Notation)：是一种轻量级数据交换格式，核心结构分为两类，且遵循「键值对」核心规则

    Python中使用json主要完成：
        1.将Python字典、列表转换为json字符串
        2.读取json字符串，转换为Python字典或列表
    主要使用Python内置的json库
        1.将字典或列表转换为json字符串：json.dumps(字典或列表, ensure_ascii=False)
            ensure_ascii参数确保中文能正常显示
            返回值：Json字符串
        2.将json字符串转换为Python字典或列表：json.loads(json字符串)
            返回值：python字典或列表
"""