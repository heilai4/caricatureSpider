from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if query:
        # 你自己的爬虫逻辑
        result = run_spider(query)
    else:
        result = "没有提供关键词。"
    return render_template('index.html', result=result)

def run_spider(keyword):
    # 示例爬虫逻辑：你可以替换为自己的
    import requests
    from bs4 import BeautifulSoup

    url = f"https://www.example.com/search?q={keyword}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        # 示例：获取所有标题
        titles = soup.find_all('h2')
        return '\n'.join(t.get_text() for t in titles[:5]) or "没有找到内容。"
    else:
        return "请求失败。"

if __name__ == '__main__':
    app.run(debug=True)
