# -*- coding:utf-8 -*-
# Author : Longhai


API_URL = "https://customer-uat.transtalent.cn/#/login"

# 浏览器驱动
DRIVER_PATH = "D:\myproject\yy_ui_bms\chrome_driver\chromedriver.exe"

# 课程名称
C1 = "领导力DNA"
C2 = "领导力启程"
C3 = "领导力精要"
C4 = "目标选材（旧版）"
C5 = "授权"
C6 = "辅导"
C7 = "打造高效团队"
C8 = "驱动变革"
C9 = "协作"
C10 = "影响力"
C11 = "计划与组织"
C12 = "决策"
C13 = "达至最佳绩效"
C14 = "解决冲突"
C15 = "影响力专业版"
C16 = "目标选才"
C17 = "领导力精要"
LIST_COURSE = [C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17]

# 模块名称
M1 = "能力诊断"
M2 = "课程学习"
M3 = "情景模拟"
M4 = "能力考核"
M5 = "引导"

# 授权课程情景模拟 ==》 选择题选项
Y = "choice1"   # 要交代
N = "choice2"   # 先不说
options = [Y, Y, Y, Y, Y, N, N, N, N, N]

# 授权课程情景模拟 ==》 决策树选项 tree_option
T1 = "option_1"
T2 = "option_2"
T3 = "option_3"
T4 = "option_4"


# 运营者后台  ==》 开发DEV
BS_DEV_URL = 'https://customer-dev.transtalent.cn/#/login'

# 运营者后台  ==》 测试UAT
BS_UAT_URL = 'https://customer-uat.transtalent.cn/#/login'

# 运营者后台  ==》 预生产M-1
BS_M1_URL = 'https://customer-1.transtalent.cn/#/login'

# 运营者后台  ==》 生产
BS_CUSTOMER_URL = 'http://customer.transtalent.cn/#/login'

# 运营者后台  ==》 管理员登录账号&密码
USER = "longhai"
PASSWORD = "q123456"

# 运营者后台  ==》 其他角色权限账号
LIST_OTHER_USER = {
             # "longhai": "q123456",      # 管理员 channel
             # "RT_LEAFQD": "q1234561",    # LEAF渠道负责人  channel
             # "RT_QD": "q123456",        # 渠道负责人   channel
             # "RT_XMJL": "q1234561",      # 项目经理  customer
             # "RT_GKK": "q123456",       # 公开课项目负责人    studentListNew
             # "RT_WBQDYY": "q123456",    # 外部渠道运营  studyDataDashboard
             "RT_HR": "q123456"         # HR    studyDataDashboard
             }

# 运营者后台  ==》菜单总权限
R = [
    'icon iconfont icon-qudao',         # 渠道管理
    'icon iconfont icon-kehu',          # 客户管理
    'icon iconfont icon-dingdan',       # 订单管理
    'icon iconfont icon-xueyuan',       # 学员管理
    'icon iconfont icon-jindu',         # 学习数据看板
    'icon iconfont icon-baogao',        # 报告管理
    'icon iconfont icon-yonghu',        # 用户管理
    'icon iconfont icon-cleanstudy',    # 学习数据管理
    'icon iconfont icon-mima']           # 修改密码

# 配置角色权限
def get_role(li):
    NEW_R = []
    for i in li:
        NEW_R.append(R[i])
    return NEW_R
# 管理员权限
ADMIN_ROLE = R
# LEAF渠道负责人权限
LEAF_QD_ROLE = get_role([0, 1, 2, 3, 4, 5, 7, 8])
# 渠道负责人权限
QUDAO_ROLE = get_role([0, 1, 2, 3, 4, 5, 7, 8])
# 项目经理权限
XMJL_ROLE = get_role([1, 2, 3, 4, 5, 7, 8])
# 公开课项目负责人权限
GKK_ROLE = get_role([3, 4, 5, 7, 8])
# 外部渠道运营权限
WBQD_ROLE = get_role([5, 7, 8])
# HR权限
HR_ROLE = get_role([4, 8])
