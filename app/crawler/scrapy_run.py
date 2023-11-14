import logging
import subprocess

def run(start_date: str = '20231104', end_date: str ='20231104') -> bool:
    path: str = './img_search_project'
    cmd: str = f'scrapy crawl hsmoa -a start_date={start_date} -a end_date={end_date}'

    try:
        print('* Start Crawling *')
        process = subprocess.Popen(cmd, shell=True, cwd=path)
        process.communicate()
        return_code = process.returncode
        result = True if return_code==0 else False
        return result
    
    except Exception as e:
        logging.error(e)
        raise SystemError(status_code=e.status_code, detail=e.detail)
    

if __name__ == '__main__':
    
    start_date = str(input('크롤링 :: 시작 날짜를 입력하세요. ex) 20231104 : '))
    end_date = str(input('크롤링 :: 종료 날짜를 입력하세요. ex) 20231104 : '))

    result = run(start_date, end_date)
    
    if result:
        print('크롤링 완료.')