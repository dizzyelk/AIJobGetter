import time
import random
import openai

from DrissionPage._pages.chromium_page import ChromiumPage

# 工作经验
exp_list = ['在校/应届', '经验不限', '1年以内', '1-3年']
# 工作岗位
job_name_list = ['web', '前端']
# 投递数量
max_applies = 50

if __name__ == '__main__':
    page = ChromiumPage()
    page.get(f'https://www.zhipin.com/web/geek/jobs')

    time.sleep(1)
    login = page.ele('@ka=header-login')
    if login:
        login.click()
        time.sleep(1)
        while 'user' in page.url:
            time.sleep(1)
            print('请登录!')

    page.ele('.text-content').click()
    time.sleep(random.uniform(2, 5))

    count = 0
    applied_count = 1
    job_list = page.ele('.rec-job-list')
    while applied_count <= max_applies:
        current_jobs = job_list.eles('.job-card-box')
        job = current_jobs[count]
        count += 1
        job_name = job.ele('.job-name').text
        company = job.ele('.boss-name').text
        city = job.ele('.company-location').text
        tag_list = job.ele('.tag-list').text.split('\n')
        exists = any(keyword in job_name for keyword in job_name_list)
        if exists and tag_list[0] in exp_list:
            print(f'正在投递 [公司]{company} {job_name} [地点]{city}')
            job.click()
            time.sleep(random.uniform(2, 5))
            detail_box = page.ele('.job-detail-box')
            # hr活跃度
            active = detail_box.ele('.name').text.split(' ')[0]
            # 岗位描述
            desc = detail_box.ele('.desc').text
            more_job = detail_box.ele('.more-job-btn')
            time.sleep(random.uniform(2, 5))
            more_job.click()
            time.sleep(random.uniform(2, 5))
            new_tab = page.latest_tab
            # 薪资范围
            salary = new_tab.ele('.salary').text
            company = new_tab.ele('.sider-company').text.split('\n')
            # 融资情况
            financing = company[2]
            # 公司人数
            peoples = company[3]
            # 行业
            industry = company[4]
            startchat = new_tab.ele('立即沟通')
            time.sleep(random.uniform(2, 5))
            startchat.click()
            # time.sleep(random.uniform(2, 5))
            # new_tab.ele('.input-area').input('你好')
            # time.sleep(random.uniform(2, 5))
            # new_tab.ele('.send-message').click()
            time.sleep(100)

    print('已完成投递目标')
