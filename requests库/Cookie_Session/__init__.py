"""
cookie与session对比:
    1 位置
        cookie保存在客户端
        session保存在服务器
    2 容量不同
            cookie比较小，session比较大，但是由于session的数据基本都是在服务器端，所以如果把大量的客户端数据保存在服务器的话，
        会导致服务器压力过大。所以，cookie和session需要灵活使用
    3 安全性不一样
        cookie不安全，session相对安全些
    4 有效时间不同
        cookie可以设置为永久不失效，就算session设置为永久不失效，单如果关闭了连接，session立刻失效
        cookie关闭连接后仍有效
    5 对浏览器的支持不一样
        比如cookie中，浏览器可以关闭cookie，但session在cookie被关闭后，还可以通过其他策略使用，比如通过url的请求参数使用

"""