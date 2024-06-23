# 安装 lxml模块
# pip install lxml

from lxml import etree

xml = """
    <book>
        <id>1</id>
        <name>退后</name>
        <price>1.11</price>
        <nick>椒麻鸡</nick>
        <author>
            <nick id="joy">周杰伦</nick>
            <nick id="jolin">蔡依林</nick>
            <nick id="jj">林俊杰</nick>
            <nick id="chow">周星驰</nick>
            <nick id="liudaqiang">刘大强</nick>
            <div>
                <nick>算了</nick>
            </div>
            <div>
                <nick>算了2</nick>
                <div>
                    <nick>test3</nick>
                </div>
            </div>
        </author>
        <partner>
            <nick id="aaa">hello</nick>
            <nick id="bbb">world</nick>
        </partner>
    </book>
    """
tree = etree.XML(xml)

name = tree.xpath("/book/name/text()")
print(name)

nick = tree.xpath("/book/author/nick/text()")
print(nick)

nickall = tree.xpath("/book/author//nick/text()") # //用法
print(nickall)

nick2 = tree.xpath("/book/author/*/nick/text()") # * 用法 通配符
print(nick2)