import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
from tests.test_utils import load_articles_data
from bs4 import BeautifulSoup

articles = load_articles_data()

print("Guide 1 FAQ section:")
soup1 = BeautifulSoup(articles[0]['contentHtml'], 'html.parser')
faq_sec1 = soup1.find(class_='ctl-faq-section')
print(faq_sec1.prettify()[:600] if faq_sec1 else "NO FAQ SECTION")

print("\nGuide 6 FAQ section:")
soup6 = BeautifulSoup(articles[5]['contentHtml'], 'html.parser')
faq_sec6 = soup6.find(class_='ctl-faq-section')
print(faq_sec6.prettify()[:600] if faq_sec6 else "NO FAQ SECTION")

for idx, a in enumerate(articles, 1):
    soup = BeautifulSoup(a['contentHtml'], 'html.parser')
    faq_items = soup.find_all(class_='ctl-faq-item')
    details_items = soup.find_all('details')
    questions = soup.find_all(class_='ctl-faq-question') + soup.find_all('summary')
    answers = soup.find_all(class_='ctl-faq-answer')
    print(f"Guide {idx:02d}: {len(faq_items)} .ctl-faq-item, {len(details_items)} <details>, {len(questions)} questions/summaries, {len(answers)} .ctl-faq-answer")
