# 短信验证码的过期时间单位秒
SMS_CODE_EXPIRES = 300

# 短信验证码发送时间周期
SMS_CODE_INTERVAL = 60

# 测试短信模板ID
SMS_TEMPLATE_ID = 1

# 测试用例常量
CASE = {
    'LEVEL': [("H", '高'), ("M", '中'), ("L", '低')]
}

# 测试任务常量
JOB = {
    'STATUS': [(0, '已创建'), (1, '待指派'), (2, '待测试'), (3, '测试中'), (4, '已完成'), (5, '已挂起')],
    'TYPE': [(0, 'DEV任务'), (1, 'PUB任务'), (2, '生产任务'), (3, '回归任务'), (4, '冒烟任务')],
    'LEVEL': [(0, '紧急'), (1, '重要'), (2, '一般'), (3, '普通')],
    'CASE_STATUS': [(0, 'WAIT'), (1, 'PASS'), (2, 'FAIL'), (3, 'BLOCK'), (4, 'BREAK')]
}