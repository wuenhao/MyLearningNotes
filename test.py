import os
import re
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_zhihu_images(url):
    # 设置桌面路径和图片保存目录
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    image_dir = os.path.join(desktop, '知乎图片')
    
    # 创建图片目录（如果不存在）
    os.makedirs(image_dir, exist_ok=True)
    
    # 设置更真实的请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.zhihu.com/',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    
    try:
        print(f"正在访问: {url}")
        
        # 添加随机延迟
        time.sleep(random.uniform(1.5, 3.5))
        
        # 获取网页内容
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=10)
        
        if response.status_code == 403:
            print("遇到403错误，尝试使用Cookie...")
            # 尝试添加常见Cookie绕过简单防护
            session.cookies.update({
                'd_c0': 'ABC123abc456def789ghi000xyz',
                'q_c1': 'xyz123abc456|1234567890000|1234567890000'
            })
            response = session.get(url, headers=headers, timeout=10)
        
        response.raise_for_status()
        
        # 检查是否被重定向到验证页面
        if "安全验证" in response.text or "unhuman" in response.text:
            print("遇到知乎安全验证，无法继续访问。请手动打开页面确认。")
            return
        
        print(f"成功获取页面 (状态码: {response.status_code})")
        
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有图片 - 知乎图片通常在noscript标签内的高清版本
        img_tags = []
        
        # 尝试查找noscript标签内的图片（高清图）
        noscript_tags = soup.find_all('noscript')
        for tag in noscript_tags:
            img = tag.find('img')
            if img and img.get('src'):
                img_tags.append(img)
        
        # 如果没找到，尝试普通img标签
        if not img_tags:
            print("未找到noscript标签内的图片，尝试普通img标签...")
            img_tags = soup.find_all('img', src=re.compile(r'https?://'))
        
        print(f"找到 {len(img_tags)} 个可能的图片")
        
        downloaded_count = 0
        for i, img_tag in enumerate(img_tags):
            img_url = img_tag.get('src') or img_tag.get('data-src') or img_tag.get('data-original')
            
            if not img_url:
                continue
                
            # 处理相对URL
            if not img_url.startswith('http'):
                img_url = urljoin(url, img_url)
                
            # 过滤非图片URL
            if not any(img_url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']):
                # 尝试从URL中提取图片格式
                if '?' in img_url:
                    img_url = img_url.split('?')[0]
                    if not any(img_url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']):
                        continue
                else:
                    continue
            
            # 添加Referer头
            img_headers = headers.copy()
            img_headers['Referer'] = url
            
            try:
                # 随机延迟避免请求过快
                time.sleep(random.uniform(0.5, 2.0))
                
                # 下载图片
                img_response = session.get(img_url, headers=img_headers, timeout=15)
                img_response.raise_for_status()
                
                # 从URL中提取文件名
                img_name = os.path.basename(urlparse(img_url).path)
                if not img_name or '.' not in img_name:
                    # 从Content-Type获取扩展名
                    content_type = img_response.headers.get('Content-Type', '')
                    if 'jpeg' in content_type or 'jpg' in content_type:
                        ext = 'jpg'
                    elif 'png' in content_type:
                        ext = 'png'
                    elif 'gif' in content_type:
                        ext = 'gif'
                    elif 'webp' in content_type:
                        ext = 'webp'
                    else:
                        ext = 'jpg'
                    img_name = f"zhihu_img_{i+1}.{ext}"
                else:
                    # 清理文件名
                    img_name = re.sub(r'[^\w\.-]', '_', img_name)
                
                # 保存图片
                save_path = os.path.join(image_dir, img_name)
                
                # 避免覆盖同名文件
                counter = 1
                while os.path.exists(save_path):
                    name, ext = os.path.splitext(img_name)
                    save_path = os.path.join(image_dir, f"{name}_{counter}{ext}")
                    counter += 1
                
                with open(save_path, 'wb') as f:
                    f.write(img_response.content)
                
                downloaded_count += 1
                print(f"已下载 ({downloaded_count}/{len(img_tags)}): {os.path.basename(save_path)}")
                
            except Exception as e:
                print(f"下载失败 {img_url}: {str(e)}")
        
        print(f"\n下载完成! 共保存 {downloaded_count} 张图片到: {image_dir}")
        
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    # 使用示例
    zhihu_url = "https://www.zhihu.com/question/20627581"  # 替换成你要爬取的知乎问题/文章URL
    download_zhihu_images(zhihu_url)