# 启动停止和恢复mongodb数据库服务
# sudo service mongod(mongodb) stop|restart|start
# mongo  进入客户端

# 查看数据库
# show databases | show dbs
# 切换数据库
# use dbname(数据库名称)
# 删除数据库
# db.dropDatabase()
# 创建数据
# use dbname(如果数据库下没有任何内容，则不显示)

# 创建集合
# db.createCollection('students')
# 不固定大小的集合：
# capped=True，
# size（设置能够存储的最大内容量，单位为字节）
# max （设置集合下能存储的最大的文档数量）
# # 如果size和max都存在，size的优先级更改
# db.createCollection(
#     'students1',
#     {
#         capped:true,
#         size:10000,
#         max:100
#     }
# )

# 删除集合
# db.student1.drop()

# 查看数据库下所有的集合
# show collections

# 关于数据的操作
# 增
# db.dbname.insert({})
# db.dbname.insert([{},{},...])

# 查
# db.dbname.find()   查询所有
# db.dbname.find().pretty()   查询所有(格式化输出)

# 条件查询
# db.students.find({info:'睡觉'})
# db.students.find({info:'睡觉',name:'zhengchangfeng'})

# 统计集合下的文档数量
# db.students.find().count() => db.students.count()

# 删除
# db.students.remove()  #删除所有
# db.students.remove({info:'睡觉'}) 根据条件删除
# db.students.remove({info:'睡觉'},1) 删除一条数据，1表示的是true，0表示false

# 改
# update:
# * upsert : 可选，这个参数的意思是，如果不存在update 的记录，是否插入objNew,true为插入，默认是false，不插 入。
# * multi : 可选，mongodb 默认是false,只更新找到的第 一条记录，如果这个参数为true,就把按条件查出来多条记录 全部更新。
# 全文档更新，新的文档覆盖之前的文档，但是 id不变
# db.students.update(
# ... {age:17},
# ... {name:'xyk',age:16,info:'small boy'}
# ... )
#
# 局部更新（指点属性更新）
# db.students.update(
# ... {age:16},
# ... {$set:{info:'big boy',age:18}}
# ... )


# save()同样可以更新数据(全文档更新)
# 如果要跟新的文档
# 如果不存在集合下,则添加一条新的文档
