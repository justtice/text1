### 问题1 
### pycharm 如何同步git上 
- 已解决  [pycharm上使用git](https://blog.csdn.net/ywj_486/article/details/80705100)
    - 在github上创建项目的key , 使用相对路径打开 vi /Users/用户名/.ssh/id_rsa.pub,然后复制里面的key就OK了
- markdown support (在配置里搜索)

- [阅轩图书专营店](https://yuexuants.tmall.com/shop/view_shop.htm?spm=a230r.7195193.1997079397.2.Owdu7A)
    - python入门到实践
    
- 前端课程并行开课

#0. oop - python的面向对象
- python的面向对象
- 面向对象的编程
    - 基础
    - 共有私有
    - 继承
    - 组合,minxi
    
- 魔法函数
    - 魔法函数概念
    - 构造类魔法函数
    - 运算类魔法函数
    
# 1 面向对象概念(objectOriented OO)
- OOP 思想
    - 接触到任意一个任务,首先想到的是任务这个世界的构造,是由模型构成的
    
- 几个名词
    - OO :面向对象
    - OOA : 面向对象的拆分
    - OOD : 面向对象的设计
    - OOI : xxx的实现
    - OOP : xxx的编程
    - OOA -> OOD -> OOI : 面向对象的实现过程
    
- 类和对象的概念
    - 类: 抽象名词,代表一个集合,共性的事物
    - 对象: 具体的事物, 单个个体 ,  类的实例
    
- 类中的内容,应该具有两个内容
    - 表明事物的特征: 属性
    - 表明事物的功能或者动作: 称为成员方法(函数)
    
# 2. 类的基本实现
- 类的命名:
    - 遵守变量命名规范
    - 大驼峰
    - 尽量避开跟系统命名相似的命名

- 声明一个类:
    - 必须用class关键字
    - 类由属性跟方法构成,其他不允许出现
    - 成员属性定义可以直接使用变量赋值,如果没有只能使用None
    - 案例, 01.py
   
   查看成员的属性,或者类的属性 :  object.__dict__
   
# 3. anaconda 基本使用
- anaconda 只要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list : 显示anaconda安装的包
- conda env list :显示anaconda的虚拟环境列表
- conda creat -n xxx python=3.6: 创建python版本为3.6的虚拟环境.名称为xxx
- source activate oop 使用这个环境
- source deactivate 退出环境

# 4. 关于self 
- self在对象的方法中表示当前对象本身,如果通过对象调用一个方法,那么该对象会自动传入到当前方法的第一个对象
- self并不是关键字,只是一个用于接受对象的普通参数,理论上可以用任何一个普通变量名代替
- 方法中可以有self ,也可以没有,如果有self称为非绑定类的方法,可以通过对象来访问, 没有叫绑定类的方法,只能通过类来访问
- 使用类访问绑定类的方法时,如果类方法中需要访问当前类的成员,可以通过__class__ 来调用

# 5. 面向对象的三大特性
- 封装
- 继承
- 多态

## 5.1 封装
- 封装就是对对象的成员进行访问限制 
- 封装的三个级别:
    - 公开 : Public
    - 受保护的: protected
    - 私有的: private
    - public , protected, private 这三个不是关键字
    
- 判断对象的位置:
    - 对象内部
    - 对象外部
    - 子类中
- 私有
    - 是最高级别的封装,只能在当前类对象中访问
    - 在成员前面添加两个下划线  
    
            class Person():
                # name是共有的成员
                name = "liuling"
                # __age 就是私有变量
                __age = 18
                
    - python的私有不是真私有 , 检测到__的时候,把这个变量改了个名
    
          
- 受保护的封装 protected
    - 受保护的封装是将对象成员进行一定级别的封装,然后,在类中或者子类中都可以进行访问,
      但是在外部都不可以
    - 在成员前面添加一个下划线
    
   
    
## 3.2 继承  
- 不需要重新造轮子 (可以获得另一个类中的属性和方法)
- 作用: 减少代码,增加代码的复用功能. 同时是可以设置类与类直接的关系

- 继承的关系:
    - 所有的类都继承与object类,即所有的类都是object类的子类
    - 子类一旦被继承,则可以使用父类中除私有成员外的所有内容
    - 子类继承父类后并没有将父类成员完全赋值到子类中,而是通过引用关系访问调用
    - 子类中可以定义独有的成员属性和方法
    - 相同的成员优先使用子类
    - 子类如果想扩充父类的方法,可以定义新方法的同时访问父类成员来进行代码重用,可以使用
      [父类名,父类成员]的格式来调用父类成员,也可以使用super().父类成员的格式来调用
    
- 继承变量的查找顺序问题
     - 优先查找自己的变量
     - 没有则查找父类
     - 构造函数如果没有定义,则自动查找父类的构造函数
     - 如果本类有定义, 则不在继续向上查找
     
- 构造函数  __init__
    - 一种特需的函数,在类进行初始化的之前进行调用
    - 如果定义了构造函数则实例化的时候调用,不向上查找
    - 没有定义就自动向上查找
    - 如果构造函数带了参数, 则按参数构造
    
- super 
    - super 不是关键字.而是一个类   help(super) ..
    - super的作用是获取MRO(方法解析顺序)列表中的第一个类  
    - 他跟父类没任何关系, 但可以通过super调用到父类
    
- 单继承和多继承
    - 单继承:每个类只能继承一个类
    - 多继承:每个类允许继承多个类
    
- 单继承和多继承的优缺点:
    - 单继承:
        - 优点:有序逻辑清晰,简单隐患少
        - 缺点:功能不能无限扩展,只能在当前唯一的继承链中扩展
    - 多继承:
        - 优点: 类的功能扩展简单
        - 缺点: 继承关系混乱,不容易查找到问题
        
    - 事例见03 
    
- 菱形继承/钻石继承问题 (就是造成继承混乱)
    - 多个子类继承同一个父类,这些子类由被同一个类继承,于是继承关系图形成一个菱形图谱
    
 
 
## 3.3 多态
- 多态就是同一个对象在不同情况下有不同的状态出现
- 多态不是语法,是一种编程思想(在python里面)
- 多态性,一种调用方式,不同执行效果
- 多态: 同一事物的多种形态,动物分为人类,狗类
- [多态和多态性](https://www.cnblogs.com/luchuangao/p/6739557.html)
    - 多态性: 在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，
               不同的对象在接收时会产生不同的行为（即方法）
    - 多态: 多态指的是一类事物有多种形态
           （一个抽象类有多个子类，因而多态的概念依赖于继承）

- Minxin设计模式
    - 只要采用多继承方式对类的功能进行扩展    
    - [Mixin概念](https://www.zhihu.com/question/20778853)
    - [MRO and Mixin](http://blog.csdn.net/robinjwong/article/details/48375833)
    - [Mixin模式](https://www.cnblogs.com/xybaby/p/6484262.html)
    - [Mixin MRO](http://runforever.github.io/2014-07-19/2014-07-19-python-mixin%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)
    - [MRO](http://xiaocong.github.io/blog/2012/06/13/python-mixin-and-mro/)

## 问题2 找到图灵学院的资料地址,补全上面地址
   - 完成
   - [GITBOOK图灵学院](https://tulingxueyuan.gitbooks.io/python/content/docs/3%E3%80%81%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%92%8C%E7%AE%97%E6%B3%95/%E6%9F%A5%E6%89%BE%E6%A6%82%E8%BF%B0.html)
   - [课件下载](https://github.com/tulingxueyuan)
   
    
    
## 5. 类的成员属性 (property自己查找)
    - 使用property函数
        - property(fget, fset, fdel, doc)
        
    ## 类属性的property的应用场景, 在get,set的时候直接修改属性
    class A():
        def __init__(self):
            self.name= "网打哈"
            self.age = 18

        def fget(self):
            print("我被读取了")
            return self.name
        def fset(self,something):
            self.name = "图灵学院"+something

        def fdel(self):
            print("不能删除了")
            pass

    something = property(fget,fset,fdel,"这是说明文档")

## 6.类的内置属性
    - __dict__ : 以字典的方式显示类的成员组成
    - __doc__: 获取类的文档信息  -> "三引号"
    - __name : 获取类的名称,如果在模块中使用,获取模块的名称
    - __bases__: 获取某个类的所有父类,以元祖的方式显示
     
##  类的常用魔术方法
    - 魔术方法就是不需要人为调用的方法,基本是特定的时候自动触发
    - 魔术方法的同一的特征,方法名被前后各两个下划线包裹
    
    - 操作类:
        - __init__: 构造函数
        - __new__: 对象实例化方法,此函数比较特殊,一般不需要使用
        - __call__: 对象当函数使用的使用触发
        - __str__: 当对象被当做字符串使用的时候调用
        - __repr_: 也是返回字符串,如果有__str__ 就只会优先打印__str__的方法
     
    - 描述符相关:
        - __set__
        - __get__
        - __delete__
        
    - 属性操作相关:
        - __getattr__:访问一个不存在的属性时触发
        - __setattr__: 对成员属性进行设置的时候触发
            - self 用来获取当前对象
            - 被设置的属性名称,以字符串形式出现
            - 需要对属性名称设置值
            - 作用: 进行属性设置的时候进行验证或者修改
            - 注意: 在该方法中不能对属性直接进行赋值操作,否则进行死循环
     
    - 运算分类相关魔术方法
        - `__gt__`: 进行大于判断的时候触发的函数
            - 参数：
                - self
                - 第二个参数是第二个对象
                - 返回值可以是任意值，推荐返回布尔值
                - 案例
                
                
                
## 8. 类和对象的三种方法
    - 实例方法
        - 需要创建对象,用对象去调用
        
    - 类方法
        - 类和对象都可以调用
        
    - 静态方法
        - 类和对象都能调用
        - 主要是不需要操作的一些方法, 比如获取 当前时间
    
    
   
## 9. 抽象类  (需要百度下) 感觉也不怎么使用
    - 抽象方法:没有具体的方法, 就写个pass ,当接口用
    - 抽象类的使用需要借助模块 import abc
    
                import abc
                
    - 抽象类: 包含抽象方法的类叫抽象类,通常为abc 类
    - 抽象类的使用
        - 抽象类可以包含抽象方法,也可以包含具体方法
        - 抽象类中可以有方法,也可以有属性
        - 抽象类不允许直接实例化
        - 必须继承才可以使用,且继承的子类必须实现所有所有继承来的抽象方法
        - 抽象类的作用主要是设定类的标准,以便开发的时候具有统一的规范
     
     
     
     
     
     
## 10. 自定义类(感觉不怎么用)
- 类其实是一个类定义和各种方法的自由组合
- 可以定义类和函数，然后自己通过类直接赋值
- 可以借助于MethodType实现
- 借助于type实现
- 利用元类实现- MetaClass
    - 元类是类
    - 备用来创造别的类 