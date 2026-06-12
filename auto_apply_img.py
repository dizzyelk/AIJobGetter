import time
import random

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
        if count == len(current_jobs):
            time.sleep(1)
            page.scroll.down(100)
            continue
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
            more_job = page.ele('.more-job-btn')
            time.sleep(random.uniform(2, 5))
            more_job.click()
            time.sleep(random.uniform(2, 5))
            new_tab = page.latest_tab
            startchat = new_tab.ele('立即沟通')
            startchat.click()
            time.sleep(random.uniform(2, 5))
            new_tab.ele('.dialog-footer').ele('继续沟通').click()
            time.sleep(random.uniform(2, 5))
            target = new_tab.ele('xpath://div[@aria-label="发送图片"]')
            target.click.to_upload(r'image.png')
            while True:
                image = new_tab.eles('.message-content')[-1]
                child = image.child(1)
                if child and 'item-image' in child.attr('class'): break
                time.sleep(1)
            time.sleep(1)
            new_tab.close()
            print(f"当前共 {len(current_jobs)} 个职位，已投递 {applied_count} 个")
            applied_count += 1
            time.sleep(random.uniform(2, 5))

    print('已完成投递目标')
