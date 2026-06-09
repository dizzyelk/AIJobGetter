import time

from DrissionPage._pages.chromium_page import ChromiumPage

exp_list = ['在校/应届', '经验不限', '1年以内', '1-3年']
# 投递数量
max_applies = 10

if __name__ == '__main__':
    page = ChromiumPage()
    page.get(f'https://www.zhipin.com/web/geek/jobs')
    print("准备登陆")
    input("登陆完成后回车继续任务")

    time.sleep(2)
    page.ele('.text-content').click()
    time.sleep(2)

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
        if tag_list[0] in exp_list:
            print(f'正在投递 [公司]{company} {job_name} [地点]{city}')
            job.click()
            time.sleep(2)
            page.ele('立即沟通').click()
            time.sleep(2)
            page.ele('留在此页').click()
            print(f"当前共 {len(current_jobs)} 个职位，已投递 {applied_count} 个")
            applied_count += 1
            time.sleep(2)

    print('已完成投递目标')