# -*- coding:utf-8 -*-
# Author : Longhai
""""
    元素封装类
"""


# 公共元素
class LocationURL:
        URL_base = "https://customer-uat.transtalent.cn/"   # 登录页地址
        URL_channel = "https://customer-uat.transtalent.cn/#/channel"  # 渠道管理地址
        URL_company = "https://customer-uat.transtalent.cn/#/customer"  # 客户管理地址
        URL_order = "https://customer-uat.transtalent.cn/#/orderV2List"  # 订单管理地址
        URL_student = "https://customer-uat.transtalent.cn/#/studentListNew"  # 学员管理地址
        URL_study = "https://customer-uat.transtalent.cn/#/studyDataDashboard"  # 学习数据看板地址
        URL_report = "https://customer-uat.transtalent.cn/#/reportManagement"  # 报告管理地址
        URL_user = "https://customer-uat.transtalent.cn/#/userListNew"  # 用户管理地址
        URL_clear = "https://customer-uat.transtalent.cn/#/cleanStudyData"  # 学员数据管理地址
        URL_password = "https://customer-uat.transtalent.cn/#/updataPassword"  # 密码地址
        URL_company_new = "https://customer-uat.transtalent.cn/#/NewCustomer"  # 新增客户地址


# 菜单元素
class LocationMenu:
        menu_channel = "//i[@class='icon iconfont icon-qudao']/.."  # 渠道管理菜单
        menu_company = "//i[@class='icon iconfont icon-kehu']/.."  # 客户管理菜单
        menu_order = "//i[@class='icon iconfont icon-dingdan']/.."  # 订单管理菜单
        menu_student = "//i[@class='icon iconfont icon-xueyuan']/.."  # 学员管理菜单
        menu_study = "//i[@class='icon iconfont icon-jindu']/.."  # 学习数据看板菜单
        menu_report = "//i[@class='icon iconfont icon-baogao']/.."  # 报告管理菜单
        menu_user = "//i[@class='icon iconfont icon-yonghu']/.."  # 用户管理菜单
        menu_clear = "//i[@class='icon iconfont icon-cleanstudy']/.."  # 学员数据管理菜单
        menu_password = "//i[@class='icon iconfont icon-mima']/.."  # 密码菜单


# 公共元素
class LocationPublic:
        public_title = "//div[@class='title']"  # 页面title


# 登录模块元素
class LocationLogin:
        login_URL = "https://customer-uat.transtalent.cn/#/login"  # 登录网址
        login_userName = "//input[@placeholder='用户名']"  # 用户名输入框
        login_password = "//input[@placeholder='密码']"  # 密码输入框
        login_button = "//button"  # 登录按钮


# 权限校验模块
class LocationPermission:
        permission_user_info = "//span[@class='el-dropdown-link el-dropdown-selfdefine']"  # 右上角角色信息
        permission_menu = "(//li[@class='el-menu-item']//i)[{}]"  # 菜单个数


# 渠道管理模块元素
class LocationChannel:
        channel_add = "//button[@class='el-button el-button--primary']"  # 新增渠道按钮
        channel_name = "//textarea[@placeholder='请输入渠道名称']"  # 渠道名称输入框
        channel_tag = "//li[text()='自动化']"  # 选择指定名称标签
        channel_save = "//button[@class='el-button el-button--primary']"  # 保存渠道按钮
        channel_first_line = "(//tr[@class='el-table__row'])[1]"  # 获取第一行数据
        channel_edit = "//*[@id='out-table']/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/button[1]"  # 编辑渠道按钮
        delete_first_tag = "(//div[@class='close el-icon-close'])[1]"  # 删除已选择的第一个标签
        channel_delete = "//*[@id='out-table']/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/button[2]"  # 渠道删除按钮
        delete_ok = "//button[@class='el-button el-button--default el-button--small el-button--primary ']"  # 渠道确认删除按钮
        delete_cancel = "//button[@class='el-button el-button--default el-button--small']"  # 新增渠道取消按钮


# 客户管理模块元素
class LocationCompany:
        company_add = "//button[@class='el-button el-button--primary']"  # 新增客户按钮
        company_name = "//textarea[@placeholder='请输入公司名称']"  # 公司名称输入框
        company_alias = "//textarea[@placeholder='请输入公司别名']"  # 公司别名输入框
        company_abbreviation = "//textarea[@placeholder='请输入公司缩写']"  # 公司缩写输入框
        company_type = "//input[@placeholder='请选择']"  # 选择公司类型下拉框
        company_public = "(//li[@class='el-select-dropdown__item'])[1]"  # 选择公开课虚拟公司
        company_experience = "(//li[@class='el-select-dropdown__item'])[2]"  # 选择体验课虚拟公司
        company_description = "//textarea[@placeholder='请输入备注信息']"  # 备注输入框
        company_save = "//span[text()='保存']"  # 新增客户保存按钮
        company_cancel = "(//button[@class='el-button el-button--default'])[1]"  # 新增客户取消按钮
        company_first_line = "(//tr[@class='el-table__row'])[1]"  # 获取第一行数据
        company_error = "//div[@class='el-message el-message--error']"  # 新增失败提示框
        error_class_name = "el-message el-message--error"  # 新增失败提示框className
        success_class_name = "el-message el-message--success"  # 新增成功提示框


# 订单管理模块元素
class LocationOrder:
        order_add = "//button[@class='el-button el-button--primary']"  # 新增订单按钮
        order_other = "rightArrow rightArrowActive"  # 特定元素--》每个页面的该元素个数不同，断言用
        order_channel = "//input[@placeholder='请选择渠道名称']"  # 选择渠道名称下拉框
        order_company = "//input[@placeholder='请选择客户名称']"  # 选择客户名称下拉框
        order_description = "//textarea[@placeholder='请输入备注信息']"  # 备注输入框
        order_next = "//span[text()='下一步']/.."  # 下一步按钮
        order_search = "//input[@placeholder='根据商品编号/商品名称/商品类型/课程搜索商品']"  # 商品搜索框
        order_courseAdd = "//div[@class='div-add']"  # 添加商品至详情按钮
        order_courseNum = "//input[@placeholder='请输入正整数']"  # 人课数输入框
        order_starTime = "//input[@placeholder='开始日期']"  # 选择开始日期
        order_overTime = "//input[@placeholder='结束日期']"  # 选择结束日期
        order_submit = "//button[@style='margin-right: 10px;']"  # 提交订单按钮
        order_sure = "(//span[text()='确 定'])[3]"  # 确认订单按钮
        order_success = "//div[@class='el-message el-message--success']"  # 订单添加成功提示框
        order_preview = "//*[@id='out-table']/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[1]"  # 订单预览按钮
        order_detail = "//div[@id='tab-订单明细']"  # 切换至订单明细页
        order_edit = "//button[@class='el-button icon_padding el-button--primary is-plain']"  # 编辑订单按钮
        order_save = "(//span[text()='保存'])[2]"  # 编辑保存订单按钮


# 学员管理模块元素
class LocationStudent:
        stu_choice_course = "//div[text()='{}']"  # 切换课程按钮
        stu_choice_company = "//input[@placeholder='所有公司']"  # 选择公司下拉框
        stu_nx_add = "(//span[text()='新增学员'])[1]"  # 新增学员按钮(内训课)
        stu_other_add = "(//span[text()='新增学员'])[2]"  # 新增学员按钮(公开课和体验课)
        stu_choice_channel = "//input[@placeholder='所有渠道']"  # 选择渠道
        stu_company_name = "(//label[text()='公司名称']/..//span)[1]"  # 新增学员页-当前公司名称
        stu_company_abbr = "//div[@class='emo_number']"  # 新增学员页-当前公司缩写
        stu_name = "//textarea[@placeholder='请输入姓名']"  # 姓名输入框
        stu_num = "//textarea[@placeholder='请输入员工号']"  # 员工号输入框
        stu_random_sex = "//label[@tabindex='{}']"  # 选择性别
        stu_phone = "//input[@placeholder='请输入手机号码']"  # 手机号码输入框
        stu_department = "//textarea[@placeholder='请输入部门']"  # 部门输入框
        stu_position = "//textarea[@placeholder='请输入职位']"  # 职位输入框
        stu_experience = "//input[@placeholder='请输入数字（支持小数点后一位）']"  # 经验年限输入框
        stu_close = "//input[@placeholder='选择日期']"  # 选择学员关闭日期
        stu_description = "//textarea[@placeholder='请输入备注信息']"  # 备注输入框
        stu_choice_tag = "(//div[@class='tabs_li']//li)[1]"  # 选择第一个标签
        stu_choice_all = "//span[text()='全选']/.."  # 选择全部课程
        stu_save = "//span[text()='保存']"  # 新增学员保存按钮
        stu_first_account = "//*[@id='out-table']/div[3]/table/tbody/tr/td[4]/div"  # 获取第一行的学员账号
        stu_search = "(//input[@placeholder='根据姓名/手机号/账号搜索学员'])[1]"  # 学员搜索输入框
        stu_page_num = "//li[@class='number active']"  # 页码元素，断言用
        stu_check_box = "(//span[@class='el-checkbox__inner'])[2]"  # 勾选搜索到的第一个学员
        stu_menu = "//button[@aria-haspopup='list']"  # 学员功能菜单按钮
        stu_import = "(//div[text()='导入学员'])[1]"  # 导入学员按钮
        stu_upload = "//div[@class='el-upload-dragger']"  # 点击上传框
        stu_import_ok = "//span[text()='确定']/."  # 上传成功确认按钮
        stu_export = "(//div[text()='导出学员'])[1]"  # 导出学员按钮
        stu_activate = "//div[text()='批量激活']"  # 批量激活按钮
        stu_disable = "//div[text()='批量关闭']"  # 批量关闭按钮
        stu_status = "//*[@id='out-table']/div[3]/table/tbody/tr[1]/td[9]/div/span"  # 第一行学员状态
        stu_disable_ok = "(//span[text()='确 定'])[4]/.."  # 确认关闭学员按钮
        stu_edit = "(//i[@class='el-icon-edit'])[2]/.."  # 学员编辑按钮
        stu_choice_sex = "(//label[@tabindex='0'])[1]"  # 选择学员性别
        stu_course_all = "el-checkbox__label"  # 学员编辑页面--所有课程的勾选框
        stu_course_able = "el-checkbox is-checked"  # 可勾选的课程框
        stu_course_box = "(//label[@class='el-checkbox'])[1]"  # 勾选课程
        stu_preview = "(//i[@class='el-icon-view'])[2]/.."  # 学员预览按钮
        stu_preview_title = "//label[text()='预览学员']"  # 学员预览页title
        stu_shut = "(//span[text()='关闭'])[1]/.."  # 学员关闭按钮
        stu_home_company_name = "//*[@id='out-table']/div[3]/table/tbody/tr/td[5]/div"  # 获取第一行学员公司名称
        stu_first_line = "(//tr[@class='el-table__row'])[1]"  # 获取第一行学员信息(内训课和公开课)
        stu_ty_first_line = "(//tr[@class='el-table__row'])[4]"  # 获取第一行学员信息(体验课)
        stu_nx_course = "领导力DNA，辅导，打造高效团队，计划与组织，协作，授权，影响力，决策，领导力启程，驱动变革，达至最佳绩效，解决冲突，目标选才，领导力精要"
        stu_ty_course = "领导力DNA，辅导，打造高效团队，领导力精要，计划与组织，协作，授权，影响力，决策，领导力启程，驱动变革，达至最佳绩效，目标选材（旧版），解决冲突"
        stu_gk_course = "领导力DNA，辅导，打造高效团队，领导力精要，计划与组织，协作，授权，影响力，决策，领导力启程，驱动变革，达至最佳绩效，目标选材（旧版），解决冲突，影响力专业版"
        

# 学习数据看板模块元素
class LocationStudy:
        study_team_company = "(//input[@placeholder='请选择公司'])[1]"  # 团队选择公司下拉框
        study_team_query = "//button[@class='el-button search-btn el-button--default']"  # 团队查询按钮
        study_time = "//div[@id='tab-学习时长']"  # 切换至学习时长页
        study_team_download = "//div[@class='download_button']"  # 下载全部数据按钮
        study_single = "//div[text()='个人数据']"  # 切换至个人数据页
        study_single_company = "(//input[@placeholder='请选择公司'])[3]"  # 个人选择公司下拉框
        study_single_search = "//input[@type='search']"  # 查询输入框
        study_unfold = "//a[@class='btn-text']"  # 展开/收拢按钮
        study_single_download = "//div[@class='f_r']"  # 下载个人数据按钮


# 报告管理模块元素
class LocationReport:
    pass


# 用户管理模块元素
class LocationUser:
    pass


# 学习数据管理模块元素
class LocationClean:
    pass


# 修改密码模块元素
class LocationPassword:
    pass
