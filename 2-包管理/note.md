# 1. 模块
    - 用的人多,出现问题的概率很少
    - 复用方便
    - 一个模块就是一个包含python代码的文件
        - 测试代码
        
- 如何使用模块
    - 模块直接导入
        - 假如模块名称直接以数字开头,需要借助importlib帮助
        
    -  import 模块 as 别名
    
    -  form 模块 import func_name, class_name (从模块里导入想要的方法名或者类名)
    
    -  form 模块 import *  (导入所有内容, 就是不用使用前缀了)
    
    -  直接运行这个文件的时候才会执行 if __name__ == '__main__':
    
-  if __name__ == '__main__': 的使用
    - 直接运行这个文件的时候才会执行
    - 准确的说每个模块的程序都是以这句话为入口
    
# 2. 模块的存储路径和加载
- 什么是模块的搜索路径:
    - 加载模块的时候,系统会在那些地方寻找此模块
- 系统默认的模块加载路径:
        import sys
        sys.path    可以获取所有路径的列表
        
- 模块的加载顺序
    1. 搜索内存中加载好的模块
    2. 搜索python的内置模块  (比如 print)
    3. 搜索python的外置模块 (sys.path)
    
# 包
- 包是大于模块的,包里放的是模块
- 模块就是python文件
- 包里还可以嵌套包
- 每个包里都有个__init__.py 文件

- 包的导入操作
    - import package_name
        - 直接导入一个包, 可以使用_init__.python 里的内容
        - 使用方式:
            - package_name.func_name
            - package_name.class_name.func_name()
        
            - improt package_name as p    
        - 注意 这种方式的访问是默认对__init__.py内容的导入
        
        
        - import package.module
            - 导入包中某一个具体的模块
            
            
- from  ... import 导入
    
    - from package import mudule
    - 此种导入方式不执行__init__.py的内容 (忽略了这个)
    
    - from package improt *
        - 这个只是导入了 __init__.py文件中的所有内容 (要的是其他文件)
        
        
        
        
            
            
    
- 在开发环境中经常会使用其他模块,可以在当前包中直接导入其他模块的内容
    - import 完整的包或者模块的路径
    
- '__all__'的使用  (配合  from package import *  这个使用的)
    - 在使用from package import * 的时候, * 可以导入的内容
    - '__init__.py'中如果文件为空,或者也没有__all__内容,就什么都不导入了
    - 设置了__all__, 就值按这里面的内容载入, 其他__init__的文件就不管了
        - __all__ = ['p01','包名02']   (这样这个包里的其他模块就可以使用)
        
         
# 命名空间
- 用不同的包当做前缀
- 防止命名冲突